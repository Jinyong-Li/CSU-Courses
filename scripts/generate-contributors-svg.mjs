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

async function fetchAsDataUrl(url) {
  const res = await fetch(url, {
    headers: { "User-Agent": "contributors-svg-generator" },
    redirect: "follow",
  });

  if (!res.ok) {
    throw new Error(`Fetch failed: ${res.status} ${res.statusText} for ${url}`);
  }

  const ct = res.headers.get("content-type") || "";
  if (!ct.startsWith("image/")) {
    throw new Error(`Unexpected content-type: ${ct} for ${url}`);
  }

  const arrayBuffer = await res.arrayBuffer();
  const buf = Buffer.from(arrayBuffer);
  const b64 = buf.toString("base64");
  return `data:${ct};base64,${b64}`;
}

const args = parseArgs(process.argv);

const repo = args.repo;
const input = args.input; // contributors.json
const output = args.output;

const columns = Number(args.columns ?? 12);
const size = Number(args.size ?? 64);
const padding = Number(args.padding ?? 6);

if (!repo || !input || !output) {
  console.error(
    "Usage: node scripts/generate-contributors-svg.mjs --repo owner/name --input <contributors.json> --output <out.svg> [--columns N] [--size PX] [--padding PX]"
  );
  process.exit(1);
}

const contributors = JSON.parse(fs.readFileSync(input, "utf8"))
  .filter((c) => c && c.login && c.avatar_url && c.html_url);

// Keep GitHub API order (usually by contributions desc), but move bots to the end (stable).
const humans = [];
const bots = [];
for (const c of contributors) {
  if (String(c.login).endsWith("[bot]")) bots.push(c);
  else humans.push(c);
}
contributors.length = 0;
contributors.push(...humans, ...bots);

const rows = Math.max(1, Math.ceil(contributors.length / columns));
const width = columns * size + (columns - 1) * padding;
const height = rows * size + (rows - 1) * padding;
const radius = Math.floor(size / 6);

const items = [];
for (let idx = 0; idx < contributors.length; idx++) {
  const c = contributors[idx];
  const login = c.login;
  const profile = c.html_url;

  const col = idx % columns;
  const row = Math.floor(idx / columns);
  const x = col * (size + padding);
  const y = row * (size + padding);

  const clipId = `clip-${idx}`;

  // Use avatar_url from API (works better for bot accounts), request size via s=
  const avatarUrl = `${c.avatar_url}${c.avatar_url.includes("?") ? "&" : "?"}s=${size}`;

  let dataUrl;
  try {
    dataUrl = await fetchAsDataUrl(avatarUrl);
  } catch {
    // Fallback placeholder
    items.push(`
  <a xlink:href="${escAttr(profile)}" target="_blank" rel="noopener noreferrer">
    <rect x="${x}" y="${y}" width="${size}" height="${size}" rx="${radius}" ry="${radius}" fill="#ddd" />
    <text x="${x + 6}" y="${y + Math.floor(size / 2)}" font-size="10" fill="#555">${escAttr(login)}</text>
  </a>`);
    continue;
  }

  items.push(`
  <a xlink:href="${escAttr(profile)}" target="_blank" rel="noopener noreferrer">
    <defs>
      <clipPath id="${clipId}">
        <rect x="${x}" y="${y}" width="${size}" height="${size}" rx="${radius}" ry="${radius}" />
      </clipPath>
    </defs>
    <image
      x="${x}" y="${y}"
      width="${size}" height="${size}"
      href="${escAttr(dataUrl)}"
      preserveAspectRatio="xMidYMid slice"
      clip-path="url(#${clipId})"
    />
  </a>`);
}

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
console.log(`Wrote ${output} with ${contributors.length} contributors.`);
