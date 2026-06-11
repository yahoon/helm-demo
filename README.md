# helm-demo

[🇨🇳 中文版](README_zh.md) | [🇺🇸 English]

`helm-demo` is a simple, multi-port web application packaged as a Helm Chart for Kubernetes. It is designed to demonstrate multi-port routing and simple text responses within a containerized environment.

## 🚀 Features

- **Multi-port Web Server**: Exposes two independent HTTP web endpoints within a single release.
- **Port 8081**: Responds with the text `"i am 8081"`.
- **Port 8082**: Responds with the text `"i am 8082"`.
- **Cloud-Native Ready**: Easily deploys to any Kubernetes cluster via Helm (OCI registry support).

## 🛠️ Prerequisites

- Kubernetes 1.19+
- Helm 3.8.0+ (with OCI support enabled)

## 📦 Quick Start

### Installing the Chart via OCI (GitHub Packages)

You can install this helm chart directly from GitHub Container Registry (GHCR) using OCI:

```bash
helm install my-helm-demo oci://ghcr.io/yahoon/charts/helm-demo --version 1.0.0
```

You can also find the chart at ArtifactHub.io: https://artifacthub.io/packages/helm/yahoon-helm-demo/helm-demo

