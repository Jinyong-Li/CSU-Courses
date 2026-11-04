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

> **第一次来？** 直接点击下方课程名称查找资料。没有想找的课程？[点击新增课程](https://github.com/Jinyong-Li/CSU-Courses/issues/new?template=add-course.yml)，可以同时上传资料，不必先等待目录创建。

## 课程导航

点击课程名称进入文件夹；具体资料以课程目录中的文件为准。

<!-- COURSE_INDEX_START -->

| 方向 | 课程与资源 |
| :--- | :--- |
| **数学与公共基础** | [高等数学](./高等数学/) · [大学物理](./大学物理/) · [英语](./英语/) |
| **计算机与工程基础** | [大计基](./大计基/) · [电工学](./电工学/) |
| **思想政治与国防** | [习概](./习概/) · [毛概](./毛概/) · [马克思主义基本原理](./马克思主义基本原理/) · [军事理论](./军事理论/) |
| **通识与心理健康** | [公选课](./公选课/) · [健康心理学](./健康心理学/) · [大学生心理健康教育](./大学生心理健康教育/) |
| **工程实践** | [制造工程训练](./制造工程训练/) · [金工实习](./金工实习/) |
| **实用模板** | [PPT 模板](./PPT模板/) · [简历模板](./简历模板/) |

<!-- COURSE_INDEX_END -->

> 以上是现有课程快捷导航。[查看仓库所有目录](https://github.com/Jinyong-Li/CSU-Courses/tree/main) 可以找到新合并、但尚未加入导航的课程。

## 参与贡献

**新增课程、小文件上传很简单；较大的文件也可以在同一个 PR 中提交，无需等课程先审核合并。**

### ① 新增课程（推荐，无需 Fork）

**[➕ 点击填写「新增课程」表单](https://github.com/Jinyong-Li/CSU-Courses/issues/new?template=add-course.yml)**

填写课程名称、分类、关键词（选填），然后选择一种提交方式：

| 提交方式 | 适用情况 | 自动处理结果 |
| :--- | :--- | :--- |
| **仅创建课程目录** | 暂时没有资料 | 自动生成课程文件夹和 README，并创建 PR |
| **创建课程并上传资料** | 同时提交常规大小的资料 | 尝试将附件导入课程目录，一起创建 PR |

机器人创建的是 **待审核的 PR**，不会自动合并。你不需要等目录合并后再上传一次资料。

<details>
<summary><strong>查看 Issue 表单的附件规则</strong></summary>

- 支持 PDF、DOCX、PPTX、XLSX、ZIP、PNG、JPG、WEBP、TXT。
- 为保证自动导入稳定，建议单个文件不超过 **20 MiB**（图片不超过 **10 MB**），每次最多 **5 个**，总大小不超过 **50 MiB**；GitHub 表单本身还可能有更严格的格式限制。
- 附件只作为待审核资料。**成功导入的文件**才写入课程 README；导入失败的附件**不会**写成永久链接。
- 有附件导入失败时，机器人会创建**草稿 PR** 并列出问题，维护者处理完成后再进入正常审核。
- ZIP 文件按原样保存，不自动解压。提交前请检查资料内容和版权。

</details>

### ② 为已有课程补充资料（Fork + PR）

课程已存在时，直接 Fork 本仓库，创建分支、添加资料文件（或在课程 README 中补充网盘链接），再提交 PR 即可。

<details>
<summary><strong>展开查看 GitHub 网页端上传流程</strong></summary>

1. 点击仓库右上角 **Fork**，复制仓库到自己的账号。
2. 在自己的 Fork 中从 `main` 新建分支，如 `add-math-notes`。
3. 进入对应课程目录，点击 **Add file → Upload files**，上传资料。
4. 点击 **Commit changes**，提交到刚才的新分支。
5. 点击 **Contribute → Open pull request**，确保目标是 `Jinyong-Li/CSU-Courses` 的 `main`。
6. 填写 PR 说明并提交，等待审核。

**同一个 PR 仍处于 Open 时**，可继续向同一个分支追加文件，无需重复创建 PR。合并后，建议从更新后的 `main` 新建分支。

</details>

### ③ 大文件怎么上传？

| 单个文件大小 | 建议方式 | 说明 |
| :--- | :--- | :--- |
| **≤25 MiB** | 网页上传 / Issue 表单 | Issue 自动导入建议遵守上面的 20 MiB、5 个文件限制 |
| **25–100 MiB** | **Fork + Git 命令行 + PR** | 普通 Git 文件超过 50 MiB 会收到警告，100 MiB 为硬限制 |
| **>100 MiB** | **网盘分享链接 + PR** | 将资料上传至网盘，在课程 README 中添加资料名称、下载链接及提取码（如有） |

**新课程也可以直接走 Fork + PR：** 在同一个分支中新建 `课程名/README.md`、添加资料文件，一次 PR 即可提交完成，**不必先填「新增课程」Issue**。

<details>
<summary><strong>查看 25–100 MiB 文件上传命令</strong></summary>

```bash
# 在自己的 Fork 仓库本地目录中操作
git checkout -b add-large-course-file
# 将文件放入对应课程目录后
git add .
git commit -m "docs: 补充课程资料"
git push origin add-large-course-file
```

然后到 GitHub 对原仓库发起 PR。请不要提交超过 100 MiB 的普通 Git 文件。

</details>

<details>
<summary><strong>查看 100 MiB 以上的网盘资料提交方式</strong></summary>

**无需 Git LFS，也不必将大文件放进 Git 仓库。** 先把文件上传到常用网盘，再通过 Fork + PR，在对应课程文件夹的 `README.md` 中提供下载信息。

建议按下面的格式填写：

```markdown
### 大文件资料（网盘）

- [课程复习资料合集（约 300 MB）](https://pan.baidu.com/s/你的分享链接)（提取码：abcd）
```

- **已有课程**：Fork 后修改课程 `README.md`，添加网盘链接并提交 PR。
- **尚未收录的课程**：也可以通过一次 PR 同时创建课程文件夹、`README.md` 和网盘链接，不必先申请创建空目录。
- 请写明资料名称、内容简介及提取码（如有），尽量选择长期有效的分享链接，并确保资料允许公开分享。
- 链接可能过期或失效，欢迎通过 Issue 反馈，由贡献者或维护者及时修正。

> **只在课程 README 中保留最终网盘资料链接**，不把临时 Issue 附件链接当成课程资料。网盘文件由对应平台托管，不会占用本仓库的 Git LFS 配额。

</details>

<details>
<summary><strong>新建课程文件夹时，README 怎么写？</strong></summary>

在课程文件夹下创建 `README.md`，复制以下最简模板即可。**课程名称就是文件夹名称，关键词选填。**

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

分类请在以下六类中选择：**公共基础课、专业基础课、专业核心课、通识选修课、实验实践课、其他**。

</details>

<details>
<summary><strong>其他问题：不会用 Git、发现错误或资料侵权</strong></summary>

- 不会使用 Fork 或 PR？可通过 [Issues](https://github.com/Jinyong-Li/CSU-Courses/issues) 提出建议并请求协助。
- 发现重复资料、错误或失效链接？欢迎 [提交 Issue](https://github.com/Jinyong-Li/CSU-Courses/issues/new/choose)。
- 请勿上传盗版教材、教师明确禁止公开的资料或个人隐私文件。

</details>

## 资料规范与版权说明

欢迎分享课程笔记、试卷、经验等，但请尊重原作者与授课教师的要求。请不要上传：

- 盗版电子书、未经授权传播的教材及付费内容。
- 盗版或破解软件及其安装包。
- 教师明确不允许公开的课件、试题和其他资料。

资料仅供学习交流，请自行判断准确性和时效性。如认为本仓库内容侵权，请联系 **iljy@vip.qq.com**，我们将核查处理。

## 致谢

感谢每一位贡献者的分享、维护与改进。

[![Contributors](assets/contributors.svg)](https://github.com/Jinyong-Li/CSU-Courses/graphs/contributors)

本项目参考了 [浙江大学课程攻略共享计划](https://github.com/QSCTech/zju-icicles) 和 [北京航空航天大学课程作业资料共享平台](https://github.com/TheBloodthirster/BUAA_Course_Sharing)，在此致谢。

## 许可

贡献者原创部分采用 [CC BY-NC-SA 4.0](LICENSE) 许可；其他资料的版权仍归各自权利人所有。

<details>
<summary><strong>相关项目：睡眠记录 / 早睡早起打卡</strong></summary>

欢迎参与 [睡眠记录 / 早睡早起打卡](https://github.com/Jinyong-Li/sleep-checkin)：通过 `/sleep` 记录睡觉，使用 `/wake` 记录起床。

</details>
