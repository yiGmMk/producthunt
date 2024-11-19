
---
title: Hugo|构建网站-minify带来的问题
description: 使用Hugo构建静态网站,为什么hugo从meta标签中删除引号,why hugo remove quotes from meta
date: 2024-11-19
image: cover.jpg
categories:
    - hugo
---

不管是官方推荐还是各种文档里,hugo构建大多使用下面的命令完成,有很多好处如缩小体积,优化加载速度等,但也有一些问题

```sh
hugo  --gc --minify
```

## build

### --minify

hugo --minify 命令用于对生成的站点内容进行压缩，从而减小文件大小，提高网页加载速度。具体来说，这个选项会对 HTML、CSS 和 JavaScript 等资源文件进行压缩或最小化处理，删除多余的空格、换行和注释，同时可能会进行某些简单的代码优化。使用 --minify 选项有助于优化网页性能，尤其是在网络带宽有限或需要提高访问速度的情况下。

#### 问题

[--minify会删除meta标签中的引号](https://discourse.gohugo.io/t/hugo-minify-and-quotes-in-meta-tags/21603/1)

删除后,bing和baidu都不能通过站点认证,因为标签被修改了,而他们要求完全一致才通过,这是百度的说明
```sh
HTML标签验证

将以下代码添加到您的网站首页HTML代码的<head>标签与</head>标签之间，完成操作后请点击“验证”按钮。

<meta name="baidu-site-verification" content="codeva-xxx" />

为保持验证通过的状态,成功验证后请不要删除该标签
```

为了通过验证,在构建时不使用--minify,或使用其他方式通过验证

### --gc

在 Hugo 中，hugo --gc 命令用于进行“垃圾收集”（Garbage Collection），这可以帮助清理未使用的资源文件或生成的文件。具体来说，当你在项目中频繁地添加、删除或移动内容时，Hugo 可能会留下不再需要的文件或数据。使用 --gc 选项会对这些过时的文件进行清理，以确保最终生成的站点只包含当前版本需要的文件，这样可以减少占用的磁盘空间，并保持项目的整洁。
hugo --gc 通常与其他构建选项结合使用，尤其是在你对网站进行了许多变更之后，这是一个确保项目干净有效的好习惯。

## 配置

### 网站head

在 layout/partials/head下新建custom.html文件,添加自定义标签
