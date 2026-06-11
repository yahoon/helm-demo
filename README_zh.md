# helm-demo

[🇺🇸 English](README.md) | [🇨🇳 中文版]

`helm-demo` 是一个打包为 Kubernetes Helm Chart 的简易双端口 Web 应用程序。它主要用于在容器化环境中演示多端口路由和简单的文本响应。

## 🚀 功能特性

- **双端口 Web 服务**：在单个 Release 中同时暴露两个独立的 HTTP 网页端点。
- **8081 端口**：访问时显示文本 `"i am 8081"`。
- **8082 端口**：访问时显示文本 `"i am 8082"`。
- **云原生就绪**：支持通过 Helm OCI 仓库轻松部署到任何 Kubernetes 集群。

## 🛠️ 前置条件

- Kubernetes 1.19+
- Helm 3.8.0+ (需支持 OCI 基础功能)

## 📦 快速开始

### 通过 OCI 仓库安装 Chart (GitHub Packages)

你可以直接从 GitHub Container Registry (GHCR) 使用 OCI 命令安装此 Helm Chart：

```bash
helm install my-helm-demo oci://ghcr.io/yahoon/charts/helm-demo --version 0.1.0
```

你也可以从ArtifactHub.io 找到此chart: https://artifacthub.io/packages/helm/yahoon-helm-demo/helm-demo

