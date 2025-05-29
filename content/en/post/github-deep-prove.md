---
title: deep-prove
date: 2025-05-29T15:30:17+08:00
draft: False
image: https://images.unsplash.com/photo-1663483534256-cca864e104b5?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NDg1MDM3MDJ8&ixlib=rb-4.1.0
tags: ['github',DeepProve,zero-knowledge,machine learning,neural networks,cryptographic techniques,sumchecks,logup GKR,privacy,blockchain,healthcare,finance]
categories: ['github']
---

# [Lagrange-Labs/deep-prove](https://github.com/Lagrange-Labs/deep-prove)

# 🚀 DeepProve: Zero-Knowledge Machine Learning (zkml) Inference

Welcome to **DeepProve**, a cutting-edge framework designed to prove neural network inference using zero-knowledge cryptographic techniques. Whether you're working with Multi-Layer Perceptrons (MLPs) or Convolutional Neural Networks (CNNs), DeepProve offers a fast and efficient way to verify computations without revealing the underlying data.
zkml is the name of the subcrate implementing the proving logic.

## 🤔 What Does DeepProve Do?

DeepProve leverages advanced cryptographic methods like sumchecks and logup GKR to achieve sublinear proving times. This means you can prove the correctness of your model's inference faster than ever before!

### 📊 Benchmark Highlights

CNN 264k: This runs a CNN on the cifar 10 dataset for a total of 264k parameters. DeepProve is proving 158x faster at this size!
Dense 4M: This runs a multiple dense layers for a total of 4 million parameters. DeepProve is proving 54x faster at this size!

| Model Type | ZKML Proving Time (ms) | ZKML Verification Time (ms) | EZKL Proving Time (ms) | EZKL Verification Time (ms) |
|------------|------------------------|-----------------------------|------------------------|-----------------------------|
| CNN 264k   | 1242                   | 599                         | 196567.01              | 312505                      |
| Dense 4M   | 2335                   | 520                         | 126831.3               | 1112                        |



## 📜 Licensing

- **zkml folder**: Licensed under the [Lagrange License](https://github.com/Lagrange-Labs/deep-prove/blob/master/zkml/LICENSE), unless otherwise specified.
- **Rest of the Code**: Licensed under Apache 2.0 + MIT, as per the original repository.

## 🌟 Use Cases

Proving inference of AI models has a wide range of applications, especially in scenarios where privacy and trust are paramount. For instance, in healthcare, sensitive patient data can be used to make predictions without exposing the data itself. In finance, models can be verified for compliance without revealing proprietary algorithms. Additionally, in decentralized applications, zero-knowledge proofs can ensure the integrity of AI computations on the blockchain, fostering trust and transparency. These use cases highlight the transformative potential of ZKML in various industries.

## 🙏 Acknowledgements

This project builds upon the work from scroll-tech/ceno, reusing the sumcheck and GKR implementation from their codebase. Check out their work at [scroll-tech/ceno](https://github.com/scroll-tech/ceno).

For more technical details and usage instructions, dive into the [ZKML README](zkml/README.md).

Happy proving! 🎉
