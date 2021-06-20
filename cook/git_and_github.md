# Git与Github

## Git

- Git 是一个开源的分布式版本控制系统，用于敏捷高效地处理任何或小或大的项目。
- Git 是 Linus Torvalds 为了帮助管理 Linux 内核开发而开发的一个开放源码的版本控制软件。

我们的目标是Git与Github联合使用，所以本教程的Git部分只讲解与Github联合使用的必要部分。若想要单独使用Git，或与其他网络托管平台或软件进行联动，请自行搜索教程。

### Git安装
[官网下载](https://git-scm.com/downloads)

- 添加邮箱密码

### Git工作流程
Git的一般工作流程如下
- 克隆 Git 资源作为工作目录。
- 在克隆的资源上添加或修改文件。
- 如果其他人修改了，你可以更新资源。
- 在提交前查看修改。
- 提交修改。
- 在修改完成后，如果发现错误，可以撤回提交并再次修改并提交。

![Git工作流程图](../images/git/git-process.png)   
（图片来自：[Git 教程 | 菜鸟教程](https://www.runoob.com/git/git-workflow.html)） 

理解工作区、暂存区和版本库

![关系图](../images/git/relationship.jpg)   
（图片来自：[Git 教程 | 菜鸟教程](https://www.runoob.com/git/git-workspace-index-repo.html)） 



### Git工作命令

以上相对常用的工作命令如下

    // 克隆Git资源
    git clone xxx.git

    // 查看目前工作目录的git状态
    git status

    // 将已经修改的文件添加到暂存区
    git add xxx

    // 将所有已经修改的文件添加到暂存区
    git add .

    //比较文件的不同，即暂存区和工作区的差异。
    git diff

    // 将暂存区的内容添加到本地仓库中
    git commit
    git commit -m 'comment here'


以下两个命令同样非常常用，但我们会在下面介绍 Github 时介绍

    // 将远程仓库同步至本地仓库
    git pull

    // 将本地仓库推送至远程仓库
    git push


## Github

gitHub是一个面向开源及私有软件项目的托管平台，因为只支持git 作为唯一的版本库格式进行托管，故名gitHub。

- github上添加密钥

### Github准备

### Github工作流程

### 多人协作

## 应用

### 准备工作
做好

### 场景一：查找开源库并下载
有时候我们需要在Github中查找别人的代码，并希望能够下载下来并运行，或者修改后运行，我们有以下两种方式。

1. 直接在Github中查找，并下载压缩包。

2. 通过Git进行下载


### 场景二：单人多计算机同步代码


