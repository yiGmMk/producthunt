---
title: PakePlus
date: 2025-07-24T15:37:37+08:00
draft: False
image: https://images.unsplash.com/photo-1591708370135-f2fac858e97b?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTMzNDI1NDV8&ixlib=rb-4.1.0
tags: ['github',]
categories: ['github']
---

# [Sjj1024/PakePlus](https://github.com/Sjj1024/PakePlus)

<h4 align="right"> 
<span href=".README.md">English</span> 
<a href="https://github.com/Sjj1024/PakePlus/discussions/2" 
style="margin: 0 10px;" >简体中文</a> 
<a href="https://github.com/Sjj1024/PakePlus/discussions/108">日本语</a>
</h4>  
<p align="center">
    <img src="./docs/pakeplus.png" width=138/>
</p>  
<h1 align="center">PakePlus</h1>  
<p align="center"><strong>Turn any webpage into a desktop or mobile app in just 9 minutes. Simple and easy to use.</strong></p>

<div align="left">PakePlus supports Mac, Windows, and Linux, and will soon support Android and iOS. There’s no need to install complex dependencies locally— all you need is a Github Token. Plus, PakePlus is only about 5MB in size. For the latest version, please see the <a href="[#popular-packages](https://github.com/Sjj1024/PakePlus/releases)">release page</a>. Check the README for information on <a href="#popular-packages">popular packages</a> and <a href="#development">custom development</a>. Feel free to share your suggestions in the <a href="https://github.com/Sjj1024/PakePlus/discussions">discussion area</a>.</div>

https://github.com/user-attachments/assets/b88bf541-0b26-4020-9eec-da79e1734fc9

## Features

-   🎐 About 20 times smaller than Electron packages (approximately 5MB!)
-   🚀 Powered by Rust and Tauri, PakePlus is lighter and faster than JS-based frameworks.
-   📦 Rich built-in feature packs—supporting shortcuts, immersive windows, and minimal customization.
-   👻 PakePlus is just a simple tool—using Tauri to replace older packaging methods (even though PWA is often sufficient).
-   🤗 PakePlus is easy to use; all you need is a GitHub Token to get a desktop app.
-   🌹 No need to install complex dependencies locally; use Github Action for cloud-based auto-packaging.
-   🧑‍🤝‍🧑 Supports internationalization, user-friendly for a global audience, and it follows your system language automatically.
-   💡 Supports custom js injection. you can write your own js code to inject into the page.
-   🎨 ui is more beautiful, more comfortable to use.

## Popular Packages

<img src=https://sjj1024.github.io/PakePlus/preview.webp  width=1920/>

PakePlus supports installation packages for both ARM and Intel architectures. Most popular program installation packages only include the ARM architecture for macOS and the Intel architecture for Windows. If you need installation packages for additional architectures, please use PakePlus to compile the required package separately.

<table>
    <tr>
        <td>DeepSeek
            <a href="https://github.com/Sjj1024/PakePlus/releases/download/OtherFiles/DeepSeek_0.0.1_aarch64.dmg">Mac</a>
            <a href="https://github.com/Sjj1024/PakePlus/releases/download/OtherFiles/DeepSeek_0.0.1_x64-setup.exe">Windows</a>
            <a href="https://github.com/Sjj1024/PakePlus/releases/download/OtherFiles/DeepSeek_0.0.1_amd64.deb">Linux</a>
        </td>
        <td>X (Twitter)
            <a href="https://github.com/codegirle/PakePlus/releases/download/Twitter/Twitter_0.0.1_aarch64.dmg">Mac</a>
            <a href="https://github.com/codegirle/PakePlus/releases/download/Twitter/Twitter_0.0.1_x64-setup.exe">Windows</a>
            <a href="https://github.com/codegirle/PakePlus/releases/download/Twitter/twitter_0.0.1_amd64.deb">Linux</a>
        </td>
    </tr>
    <tr>
        <td><img src=https://sjj1024.github.io/PakePlus/deepseek.png width=600/></td>
        <td><img src=https://sjj1024.github.io/PakePlus/xtwitter.png width=600/></td>
    </tr>
    <tr>
        <td>YouTube
            <a href="https://github.com/codegirle/PakePlus/releases/download/YouTube/YouTube_0.0.2_aarch64.dmg">Mac</a>
            <a href="https://github.com/codegirle/PakePlus/releases/download/YouTube/YouTube_0.0.2_x64-setup.exe">Windows</a>
            <a href="https://github.com/codegirle/PakePlus/releases/download/YouTube/you-tube_0.0.2_amd64.deb">Linux</a>
        </td>
        <td>小红书(Red Book)
            <a href="https://github.com/Sjj1024/PakePlus/releases/download/OtherFiles/_0.0.1_aarch64.dmg">Mac</a>
            <a href="https://github.com/Sjj1024/PakePlus/releases/download/OtherFiles/_0.0.1_x64-setup.exe">Windows</a>
            <a href="https://github.com/Sjj1024/PakePlus/releases/download/OtherFiles/_0.0.1_amd64.deb">Linux</a>
        </td>
    </tr>
    <tr>
        <td><img src=https://sjj1024.github.io/PakePlus/youtube.png width=600/></td>
        <td><img src=https://sjj1024.github.io/PakePlus/hongshu.png width=600/></td>
    </tr>
        <tr>
        <td>Tiktok
            <a href="https://github.com/codegirle/PakePlus/releases/download/Tiktok/Tiktok_0.0.2_aarch64.dmg">Mac</a>
            <a href="https://github.com/codegirle/PakePlus/releases/download/Tiktok/Tiktok_0.0.2_x64-setup.exe">Windows</a>
            <a href="https://github.com/codegirle/PakePlus/releases/download/Tiktok/tiktok_0.0.2_amd64.deb">Linux</a>
        </td>
        <td>抖音
            <a href="https://github.com/codegirle/PakePlus/releases/download/Douyin/Douyin_0.0.2_aarch64.dmg">Mac</a>
            <a href="https://github.com/codegirle/PakePlus/releases/download/Douyin/Douyin_0.0.2_x64-setup.exe">Windows</a>
            <a href="https://github.com/codegirle/PakePlus/releases/download/Douyin/douyin_0.0.2_amd64.deb">Linux</a>
        </td>
    </tr>
    <tr>
        <td><img src=https://sjj1024.github.io/PakePlus/tiktok.png width=600/></td>
        <td><img src=https://sjj1024.github.io/PakePlus/douyin.png width=600/></td>
    </tr>
</table>

## Getting Started

1. Download the app from the release page：https://github.com/Sjj1024/PakePlus/releases, double-click to install, and run the app.
2. Configure a Github Token, create a new project, and set up the configurations. get token guide: <a href="https://sjj1024.github.io/PakePlus/">English</a> <a href="https://sjj1024.github.io/PakePlus/index_zh.html" style="margin: 0 10px;">简体中文</a><a href="https://sjj1024.github.io/PakePlus/index_zh.html">日本语</a>

```
Explanation of Github Token permissions:
1. For the beta version, token permissions required:
All repositories: Fork an original template repository
Actions: Manage GitHub actions
Administration: Fork and manage files in the repository
Contents: Add, delete, modify, and find repository contents
Issues: Submit issues to PakePlus

1. For the classic version, token permissions required:
repo: Fork and manage template code
workflow: Compile and release your software
```

1. You can preview the app in a new window and click the publish button to package the app.
2. You can download the app from the release page.

## FAQ

1. Mac users may see an “App is damaged” warning on installation. click cancel and Run the following command, then reopen the app:

```sh
sudo xattr -r -d com.apple.quarantine /Applications/PakePlus.app
```

2. When you package the app, Mac users may see an “App is damaged” warning on installation. click cancel and Run the following command, then reopen the app:

```sh
sudo xattr -r -d com.apple.quarantine /Applications/YourAppName.app
```

3. If you encounter any issues while using the program, please download the latest version, as versions developed before 2025 were based on Tauri v1.0. In 2025, Tauri was upgraded to v2.0. If the latest version still has issues, please submit an issue with detailed information so that we can update and resolve it more quickly.

4. After you add the GitHub Token, PakePlus will fork a PakePlus repository into your own repository. All your future projects will rely on this repository for creation and compilation, so please do not delete your PakePlus repository.

## Developing PakePlus

If you want to develop PakePlus locally, ensure your environment is prepared beforehand. Make sure Rust `>=1.63` and Node `>=16` (e.g., `16.18.1`) are installed on your computer. For installation guidance, please refer to the [Tauri Documentation](https://tauri.app/v1/guides/getting-started/prerequisites).

If you’re unfamiliar with these, it’s best to try the one-click packaging tool above.

```sh
# Install dependencies
pnpm i

# Local development [Right-click to open debug mode.]
pnpm run dev

# Package the app
pnpm run build

# github action
releaseDraft: false：means this version is not a draft version, it will be considered as a stable release.
prerelease: false：means this version is not a pre-release version, which means it is a stable version.
publish: false：means this version will not be published immediately, although it will be created, it will not be publicly displayed.
```

## Support

1. wechat and group
 <p align="center" style="display:flex; justify-content: flex-start;" >
    <img src="./docs/mywx.png" width=300/>
    <img src="./docs/wxcode.png" width=300/>
 </p>

1. If PakePlus has brought joy to your life, feel free to support it.
 <p align="center" style="display:flex; justify-content: flex-start;">
    <img src="./docs/pay.png" width=620/>
 </p>

## TODO

1. add auto update feature
2. support build android apk and build ios ipa
3. add upload front build dist to build
