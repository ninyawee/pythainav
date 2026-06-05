# See: https://github.com/microsoft/vscode-dev-containers/tree/main/containers/python-3
# [Choice] Python version: 3, 3.13, 3.12, 3.11, 3.10, 3.9
ARG VARIANT="3.12"
FROM mcr.microsoft.com/devcontainers/python:1-${VARIANT}

# Install uv (https://docs.astral.sh/uv/)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# Pre-install dependencies for faster first start (the workspace is mounted at runtime).
COPY pyproject.toml uv.lock ./
RUN uv sync --no-install-project
