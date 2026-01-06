# 中南大学课程共享计划 😉
<p align="center">
  <a href="https://github.com/Jinyong-Li/CSU-Courses/stargazers">
    <img src="https://img.shields.io/github/stars/Jinyong-Li/CSU-Courses?style=flat-square" alt="Stars" />
  </a>
  <a href="https://github.com/Jinyong-Li/CSU-Courses/network/members">
    <img src="https://img.shields.io/github/forks/Jinyong-Li/CSU-Courses?style=flat-square" alt="Forks" />
  </a>
  <a href="https://github.com/Jinyong-Li/CSU-Courses/issues">
    <img src="https://img.shields.io/github/issues/Jinyong-Li/CSU-Courses?style=flat-square" alt="Issues" />
  </a>
  <a href="https://github.com/Jinyong-Li/CSU-Courses/pulls">
    <img src="https://img.shields.io/github/issues-pr/Jinyong-Li/CSU-Courses?style=flat-square" alt="Pull Requests" />
  </a>
  <a href="https://github.com/Jinyong-Li/CSU-Courses/commits/main">
    <img src="https://img.shields.io/github/last-commit/Jinyong-Li/CSU-Courses?style=flat-square" alt="Last Commit" />
  </a>
  <a href="https://github.com/Jinyong-Li/CSU-Courses/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/Jinyong-Li/CSU-Courses?style=flat-square" alt="Contributors" />
  </a>
</p>
中南大学课程共享计划——CSU-Courses，欢迎大家贡献！
正是大家的关注、维护和贡献，才使这个项目得以持续完善、不断更新，帮助更多同学更高效地学习与备考~




## 如何为本项目贡献

### 方法一：网页端提交 PR（推荐）

> 适合：补充资料、上传 PDF/Word/图片等。  
> **原则：一个 PR 对应一条分支**。只要该 PR 仍处于 **Open** 状态，后续所有新增/上传都请 **Commit 到该 PR 对应的分支**，这样会自动追加到同一个 PR。


#### 1. Fork 本项目
点击右上角 **Fork**，将仓库 Fork 到你自己的账号下。

#### 2. 为本次贡献创建一个分支（推荐）
进入你自己的 fork 仓库（例如 `yourname/CSU-Courses`）：

1. 点击分支下拉（通常显示 `main`）
2. 输入一个新分支名（例如：`add-xxx-course-materials` 或 `patch-1`）
3. 点击 **Create branch: `<branch>` from `main`**

> 说明：如果你不小心在后续步骤里点了 “Create a new branch …”，也无妨，
> 把它当作你这次贡献的分支即可。关键是：**后续都提交到这一个分支**。

#### 3. 选择/创建课程目录（没有就新建，并添加 README）
- 如果仓库里 **已经有对应课程目录**：直接进入目录，跳到第 4 步。
- 如果 **没有对应课程目录**：建议新建目录并添加 `README.md`（资料简介/注意事项/课程体会等）。

**网页端创建目录的方法：**
1. 确认你当前在**第 2 步创建的分支**（不是 `main`）
2. 点击 **Add file → Create new file**
3. 文件名输入：`课程名/README.md`  
   （输入 `课程名/` 会自动形成目录；以 `README.md` 结尾）
4. 填写 README 内容
5. 提交选项选择：**Commit directly to the `<你的分支名>` branch**（重要）
6. 点击 **Commit changes**

#### 4. 上传资料文件（追加到同一分支）
1. 进入目标课程目录
2. 点击 **Add file → Upload files**
3. 选择文件或拖拽上传
4. 提交选项选择：**Commit directly to the `<你的分支名>` branch**（重要）
5. 点击 **Commit changes**

> 可以重复上传多次；只要 PR 仍是 Open，就一直提交到该 PR 对应分支即可。

#### 5. 创建 Pull Request（PR）
1. 回到你 fork 仓库首页，通过以下任一入口发起 PR：
   - 页面提示横幅里的 **Compare & pull request**
   - **Contribute → Open pull request**
   - **Pull requests → New pull request**
2. 确认参数正确：
   - **base repository（目标仓库）**：`Jinyong-Li/CSU-Courses`
   - **base branch**：`main`
   - **head repository**：你的 fork（例如 `yourname/CSU-Courses`）
   - **compare**：你本次贡献的分支（例如 `add-xxx-course-materials`）
3. 填写标题与说明，点击 **Create pull request**

> [!IMPORTANT]
> 如果 base repository 不是 `Jinyong-Li/CSU-Courses`：  
> 点击页面上方小蓝字 **compare across forks**，手动选择：
> - base repository = `Jinyong-Li/CSU-Courses`
> - base branch = `main`

#### 6. PR 已经开了，但还想继续补充资料（追加到同一个 PR）
前提：该 PR 仍处于 **Open** 状态。

1. 回到你自己的 fork 仓库
2. 切换到该 PR 对应的分支（例如 `add-xxx-course-materials` / `patch-1`）
3. 继续 **Add file → Create new file / Upload files**
4. 提交时始终选择：**Commit directly to该分支**
5. 回到 PR 页面刷新即可，新提交会自动出现在同一个 PR 里

如果该 PR 已经 **Merged/Closed**：请从 fork 的 `main` 创建新分支，再按本文流程开一个新的 PR。


#### 7. （可选）PR 合并后删除分支
当 PR 被 **Merged** 后，你可以删除用于本次贡献的分支，保持仓库整洁：

- 在 PR 页面通常会出现 **Delete branch** 按钮，点击即可删除该分支
- 或在你自己的 fork 仓库的 **Branches** 页面手动删除

> 如果后续还要继续贡献，建议从 fork 的 `main` 再新建一个分支，而不是复用旧分支。


#### 上传限制（GitHub 常见限制）
- 单个文件建议不超过 **25MB**（超过可能无法通过网页上传/或会被限制）
- 一次可上传的文件数量也有限（文件太多建议分批提交）
- 更大的文件建议使用 **Git LFS** 或提供 **网盘/Release 链接**，并在 `README.md` 中说明

### 方法二：写一个Issue，由项目维护人员进行添加。


## 注意事项

下列内容为不适合上传的内容。如果你认为缺少这些资料将会影响资源的完整性，建议你撰写一个 README 文档并放置一些链接或指引文字来帮助找到这些资源。

- 盗版电子书/付费电子书
- 盗版/破解版/绿色版付费软件及其安装包
- 教师不允许上传的内容

如果你认为本仓库的一些文件侵犯了您的权益，请联系我们 iljy@vip.qq.com 。我们将会从仓库中删除这些文件。

## 致谢

感谢以下项目贡献者:

[![Contributors](assets/contributors.svg)](https://github.com/Jinyong-Li/CSU-Courses/graphs/contributors)


本项目参考了[浙江大学课程攻略共享计划](https://github.com/QSCTech/zju-icicles) ，[北京航空航天大学(北航)课程作业资料共享平台](https://github.com/TheBloodthirster/BUAA_Course_Sharing) ，在此表示感谢！

## 许可

由贡献者编写部分的许可如下：

[CC-BY-NC-SA：署名-非商业性使用-相同方式共享](LICENSE)

> 资料仅供参考，请自己判断其适用性。

其他部分的版权归属于其各自的作者。
