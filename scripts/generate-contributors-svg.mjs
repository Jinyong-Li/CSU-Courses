#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";

function parseArgs(argv) {
  const args = {};
  for (let i = 2; i < argv.length; i++) {
    const a = argv[i];
    if (a.startsWith("--")) {
      const k = a.slice(2);
      const v = argv[i + 1];
      args[k] = v;
      i++;
    }
  }
  return args;
}

function escAttr(s) {
  return String(s)
    .replace(/&/g, "&amp;")
    .replace(/"/g, "&quot;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

const args = parseArgs(process.argv);

const repo = args.repo;
const input = args.input;
const output = args.output;

const columns = Number(args.columns ?? 12);
const size = Number(args.size ?? 64);
const padding = Number(args.padding ?? 6);

if (!repo || !input || !output) {
  console.error(
    "Usage: node scripts/generate-contributors-svg.mjs --repo owner/name --input <logins.txt> --output <out.svg> [--columns N] [--size PX] [--padding PX]"
  );
  process.exit(1);
}

const logins = fs
  .readFileSync(input, "utf8")
  .split(/\r?\n/)
  .map((s) => s.trim())
  .filter(Boolean);

const rows = Math.max(1, Math.ceil(logins.length / columns));
const width = columns * size + (columns - 1) * padding;
const height = rows * size + (rows - 1) * padding;

const items = logins.map((login, idx) => {
  const col = idx % columns;
  const row = Math.floor(idx / columns);
  const x = col * (size + padding);
  const y = row * (size + padding);

  // GitHub avatar URL is stable; s= controls requested size.
  const avatar = `https://github.com/${encodeURIComponent(login)}.png?size=${size}`;
  const profile = `https://github.com/${encodeURIComponent(login)}`;

  // Clip to rounded rect
  const clipId = `clip-${idx}`;
  return `
  <a xlink:href="${escAttr(profile)}" target="_blank" rel="noopener noreferrer">
    <defs>
      <clipPath id="${clipId}">
        <rect x="${x}" y="${y}" width="${size}" height="${size}" rx="${Math.floor(size / 6)}" ry="${Math.floor(size / 6)}" />
      </clipPath>
    </defs>
    <image
      x="${x}" y="${y}"
      width="${size}" height="${size}"
      href="${escAttr(avatar)}"
      preserveAspectRatio="xMidYMid slice"
      clip-path="url(#${clipId})"
    />
  </a>`;
});

const svg = `<?xml version="1.0" encoding="UTF-8"?>
<svg
  xmlns="http://www.w3.org/2000/svg"
  xmlns:xlink="http://www.w3.org/1999/xlink"
  width="${width}"
  height="${height}"
  viewBox="0 0 ${width} ${height}"
>
  <title>Contributors of ${escAttr(repo)}</title>
  ${items.join("\n")}
</svg>
`;

fs.mkdirSync(path.dirname(output), { recursive: true });
fs.writeFileSync(output, svg, "utf8");
console.log(`Wrote ${output} with ${logins.length} contributors.`);
