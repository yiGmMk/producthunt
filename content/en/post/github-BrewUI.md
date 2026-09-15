---
title: BrewUI
date: 2026-09-15T20:47:54+08:00
draft: False
image: https://images.unsplash.com/photo-1663860194262-8ba762768500?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3ODk0NzYyMzh8&ixlib=rb-4.1.0
tags: ['github',Homebrew, GUI, macOS]
categories: ['github']
---

# [Homebrew/BrewUI](https://github.com/Homebrew/BrewUI)

# 🧑‍💻 BrewUI

<img width="1336" height="844" alt="BrewUI user interface" src="https://github.com/user-attachments/assets/3969e6b2-3054-4127-be5c-847aa1d98c01" />

Homebrew's official macOS GUI: making package management approachable for users who prefer graphical interfaces over Terminal, while maintaining complete transparency about underlying Homebrew operations.

## 💡 Motivation

Enable CLI-averse users to safely discover, install, update, and manage Homebrew packages through a native SwiftUI interface that never hides what Homebrew is doing.

## 📲 Tech

- **Swift 6.0** with strict concurrency · **SwiftUI** · **Swift Package Manager**
- **macOS Tahoe 26+**
- Data from the `brew` CLI and the [Homebrew JSON API](https://formulae.brew.sh/docs/api/)

## 📦 Installation

```bash
brew install --cask homebrew-app
```

## 🛠️ Development

After cloning:

```bash
./scripts/bootstrap
```

This installs Mint from `Brewfile`, runs `mint bootstrap` to build the SwiftFormat and SwiftLint versions pinned in `Mintfile`, enables repository git hooks, and resolves Swift package dependencies for `Homebrew.xcodeproj`.

After bootstrap, commits automatically run checks on staged Swift files:

1. `mint run swiftformat`
2. `mint run swiftlint` (with `--fix`, then strict validation)

If unresolved lint violations remain, the commit is blocked and the hook prints specific SwiftLint failures so you can fix and re-commit.

## 🚧 Status

Stable and under active development.

## 📄 Licence

[AGPL-3.0](LICENSE). If you reuse or adapt the source the AGPL terms apply, including the network-use clause.
