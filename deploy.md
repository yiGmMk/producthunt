# deploy

github actions 构建,构建后存储到pages分支,再使用netlify部署静态网页

## vercel

no support for go build ,we need to install go manually, 下面的方法试了走不通 [2024/11/18],改用github actions构建

### install go

2024.11.17 install by cmd

```sh
yum install golang
```

we got 

```sh
CtrlF
Running build in Washington, D.C., USA (East) – iad1
Cloning github.com/yiGmMk/producthunt (Branch: master, Commit: 992b208)
Cloning completed: 391.976ms
Previous build cache not available
Running "vercel build"
Vercel CLI 39.0.2
Installing Hugo version 0.58.2
Running "install" command: `yum install golang`...
Failed to set locale, defaulting to C.UTF-8
Amazon Linux 2023 repository                     44 MB/s |  20 MB     00:00    
Last metadata expiration check: 0:00:03 ago on Sun Nov 17 11:30:06 2024.
Dependencies resolved.
================================================================================
 Package         Arch        Version                     Repository        Size
================================================================================
Installing:
 golang          x86_64      1.20.8-1.amzn2023.0.1       amazonlinux      599 k
Installing dependencies:
 golang-bin      x86_64      1.20.8-1.amzn2023.0.1       amazonlinux       58 M
 golang-src      noarch      1.20.8-1.amzn2023.0.1       amazonlinux       11 M
Transaction Summary
================================================================================
Install  3 Packages
Total download size: 69 M
Installed size: 204 M
```

ref https://github.com/orgs/vercel/discussions/38

## netlify

suport hugo but old version 0.85.x,and we need 0.123.x or later,not work
不支持