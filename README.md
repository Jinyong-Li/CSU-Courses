<h1 align="center">中南大学课程共享计划</h1>

<p align="center"><strong>CSU-Courses · 让课程资料更容易找到，也更容易被分享</strong></p>

<p align="center">课件 · 笔记 · 习题 · 复习资料 · 修读建议</p>

<p align="center">
  <a href="#课程导航">浏览课程</a> ·
  <a href="https://github.com/Jinyong-Li/CSU-Courses/issues/new?template=add-course.yml">新增课程</a> ·
  <a href="#参与贡献">上传资料</a> ·
  <a href="https://github.com/Jinyong-Li/CSU-Courses/issues">问题反馈</a>
</p>

<p align="center">
  <a href="https://github.com/Jinyong-Li/CSU-Courses/stargazers"><img src="https://img.shields.io/github/stars/Jinyong-Li/CSU-Courses?style=flat-square" alt="Stars"></a>
  <a href="https://github.com/Jinyong-Li/CSU-Courses/network/members"><img src="https://img.shields.io/github/forks/Jinyong-Li/CSU-Courses?style=flat-square" alt="Forks"></a>
  <a href="https://github.com/Jinyong-Li/CSU-Courses/commits/main"><img src="https://img.shields.io/github/last-commit/Jinyong-Li/CSU-Courses?style=flat-square" alt="Last Commit"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey?style=flat-square" alt="License: CC BY-NC-SA 4.0"></a>
</p>

欢迎查找和分享中南大学课程资料！点击下方课程名称即可浏览；没有对应课程，也欢迎添加。

## 课程导航

<!-- COURSE_INDEX_START -->

| 分类 | 课程与资源 |
| :--- | :--- |
| **数学与公共基础** | [高等数学](./高等数学/) · [大学物理](./大学物理/) · [英语](./英语/) |
| **计算机与工程基础** | [大计基](./大计基/) · [电工学](./电工学/) |
| **思想政治与国防** | [习概](./习概/) · [毛概](./毛概/) · [马克思主义基本原理](./马克思主义基本原理/) · [军事理论](./军事理论/) |
| **通识与心理健康** | [公选课](./公选课/) · [健康心理学](./健康心理学/) · [大学生心理健康教育](./大学生心理健康教育/) |
| **工程实践** | [制造工程训练](./制造工程训练/) · [金工实习](./金工实习/) |
| **实用模板** | [PPT 模板](./PPT模板/) · [简历模板](./简历模板/) |

<!-- COURSE_INDEX_END -->

[查看仓库全部目录](https://github.com/Jinyong-Li/CSU-Courses/tree/main)

## 参与贡献

### ① 新增课程（无需 Fork）

**[➕ 点击填写「新增课程」表单](https://github.com/Jinyong-Li/CSU-Courses/issues/new?template=add-course.yml)**

填写课程名称、分类和关键词（选填），选择一种方式：

- **仅创建课程目录**：自动生成课程文件夹和 `README.md`。
- **创建课程并上传资料**：直接在表单中上传文件，和课程目录一起提交。

提交后会自动创建 Pull Request（PR），由维护者审核合并。表单适合较小的资料；较大的文件可按下方方法提交。

### ② 补充已有课程资料（Fork + PR）

**Fork 仓库 → 创建分支 → 上传资料 → 提交 PR**。

<details>
<summary><strong>展开查看 GitHub 网页端上传流程</strong></summary>

1. 点击仓库右上角 **Fork**，复制仓库到自己的账号。
2. 在自己的 Fork 中从 `main` 新建分支，如 `add-math-notes`。
3. 进入对应课程目录，点击 **Add file → Upload files**，上传资料。
4. 点击 **Commit changes**，提交到刚才的新分支。
5. 点击 **Contribute → Open pull request**，确保目标是 `Jinyong-Li/CSU-Courses` 的 `main`。
6. 填写 PR 标题和说明，点击 **Create pull request**，等待审核。

**PR 仍处于 Open 状态时**，可以继续向对应分支上传文件并 Commit，新提交会自动追加到同一个 PR，无需重复创建。

如果需要新增一门尚未收录的课程，也可以在分支中创建 `课程名/README.md`，连同资料一起提交，不必先创建空目录。下方有课程 README 模板。

</details>

### ③ 大文件上传

| 单个文件大小 | 推荐方式 |
| :--- | :--- |
| **≤25 MiB** | GitHub 网页上传；新增课程也可使用表单上传小文件 |
| **25–100 MiB** | Fork 后通过 Git 命令行上传，再提交 PR |
| **>100 MiB** | 上传网盘，在课程 `README.md` 中添加分享链接并提交 PR |

<details>
<summary><strong>查看 25–100 MiB 文件上传方法</strong></summary>

先 Fork 本仓库并克隆到本地，在仓库目录中执行：

```bash
git switch -c add-large-course-file
# 将资料文件复制到对应课程目录后
git add .
git commit -m "docs: 补充课程资料"
git push -u origin add-large-course-file
```

然后在 GitHub 上向本仓库的 `main` 分支发起 PR。

</details>

<details>
<summary><strong>查看网盘资料的提交方法</strong></summary>

对于超过 100 MiB 的资料，可以先上传网盘，再在课程 `README.md` 中添加链接：

```markdown
### 网盘资料

- [期末复习资料合集（约 300 MB）](https://pan.baidu.com/s/分享链接)（提取码：abcd）
```

通过 Fork + PR 提交 README 的修改即可。新课程也可以一次 PR 同时创建目录并添加网盘链接。

</details>

<details>
<summary><strong>新建课程时，README 怎么写？</strong></summary>

在课程文件夹中创建 `README.md`，可使用以下模板。课程名称以文件夹名为准，关键词选填。

```markdown
<!-- COURSE_META_START
分类：专业基础课
关键词：算法、数据结构
COURSE_META_END -->

# 课程名称

> **课程分类**：专业基础课  
> **关键词**：算法 · 数据结构

## 课程简介

## 课程资料

## 修读建议
```

分类可选：**公共基础课、专业基础课、专业核心课、通识选修课、实验实践课、其他**。

</details>

如果不会使用 Git，或者想反馈资料问题，也欢迎 [提交 Issue](https://github.com/Jinyong-Li/CSU-Courses/issues/new/choose)。

## 资料规范与版权说明

欢迎分享课件、笔记、试卷和学习经验，请尊重教师和原作者的版权。以下内容请勿上传：

- 盗版电子书、未经授权传播的教材及付费内容。
- 盗版或破解软件及其安装包。
- 教师明确不允许公开的课件、试题等资料。

本仓库资料仅供学习参考。如发现侵权内容，请联系 **iljy@vip.qq.com**，我们将核查处理。

## 致谢

感谢每一位贡献者的分享与维护！

[![Contributors](assets/contributors.svg)](https://github.com/Jinyong-Li/CSU-Courses/graphs/contributors)

本项目参考了 [浙江大学课程攻略共享计划](https://github.com/QSCTech/zju-icicles) 和 [北京航空航天大学课程作业资料共享平台](https://github.com/TheBloodthirster/BUAA_Course_Sharing)，在此致谢。

## 许可

贡献者原创部分采用 [CC BY-NC-SA 4.0](LICENSE) 许可；其他资料版权归各自权利人所有。

<details>
<summary><strong>相关项目：睡眠记录 / 早睡早起打卡</strong></summary>

欢迎参与 [睡眠记录 / 早睡早起打卡](https://github.com/Jinyong-Li/sleep-checkin)：使用 `/sleep` 记录睡觉，`/wake` 记录起床。

</details>
