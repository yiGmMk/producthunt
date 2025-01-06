# Product Hunt 热榜

使用Product Hunt API 获取每日产品热榜,bing使用LLM翻译成多语言版本

## LLM

- [自部署gpt-4o接口](https://gpt4o.programnotes.cn/docs),使用https://github.com/yiGmMk/free-unoficial-gpt4o-mini-api 部署
- google gemini 转换成openai格式的接口: [gemini-1.5-flash](https://gemini2gpt.programnotes.cn/v1),使用https://github.com/yiGmMk/openai-gemini部署
- [硅基流动提供的免费额度](https://cloud.siliconflow.cn/i/eluTiiYw)
- [openrouter.ai提供的免费额度](https://openrouter.ai/)

<img align="right" width="150" alt="logo" src="https://user-images.githubusercontent.com/5889006/190859553-5b229b4f-c476-4cbd-928f-890f5265ca4c.png">

## Hugo Theme Stack Starter Template

This is a quick start template for [Hugo theme Stack](https://github.com/CaiJimmy/hugo-theme-stack). It uses [Hugo modules](https://gohugo.io/hugo-modules/) feature to load the theme.

It comes with a basic theme structure and configuration. GitHub action has been set up to deploy the theme to a public GitHub page automatically. Also, there's a cron job to update the theme automatically everyday.

### Get started

1. Click *Use this template*, and create your repository as `<username>.github.io` on GitHub.
![Step 1](https://user-images.githubusercontent.com/5889006/156916624-20b2a784-f3a9-4718-aa5f-ce2a436b241f.png)

2. Once the repository is created, create a GitHub codespace associated with it.
![Create codespace](https://user-images.githubusercontent.com/5889006/156916672-43b7b6e9-4ffb-4704-b4ba-d5ca40ffcae7.png)

3. And voila! You're ready to go. The codespace has been configured with the latest version of Hugo extended, just run `hugo server` in the terminal and see your new site in action.

4. Check `config` folder for the configuration files. You can edit them to suit your needs. Make sure to update the `baseurl` property in `config/_default/config.toml` to your site's URL.

5. Open Settings -> Pages. Change the build branch from `master` to `gh-pages`.
![Build](https://github.com/namanh11611/hugo-theme-stack-starter/assets/16586200/12c763cd-bead-4923-b610-8788f388fcb5)

6. Once you're done editing the site, just commit it and push it. GitHub action will deploy the site automatically to GitHub page asociated with the repository.
![GitHub action](https://user-images.githubusercontent.com/5889006/156916881-90b8bb9b-1925-4e60-9d7a-8026cda729bf.png)

---

In case you don't want to use GitHub codespace, you can also run this template in your local machine. **You need to install Git, Go and Hugo extended locally.**

### Update theme manually

Run:

```bash
hugo mod get -u github.com/CaiJimmy/hugo-theme-stack/v3
hugo mod tidy
```

> This starter template has been configured with `v3` version of theme. Due to the limitation of Go module, once the `v4` or up version of theme is released, you need to update the theme manually. (Modifying `config/module.toml` file)

## Deploy to another static page hostings

### Vercel

not work for hugo 0.138.0 2024/11/18 [说明](./deploy.md)

### Netlify

现部署到github的指定分支 gh-pages(使用github actions),再将静态文件部署到netlify

[![Netlify Status](https://api.netlify.com/api/v1/badges/3b25f6c5-ce4c-4825-9c3b-943592e42e88/deploy-status)](https://app.netlify.com/sites/producthunt-daily/deploys)