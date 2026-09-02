# syntax=docker/dockerfile:1.7@sha256:a57df69d0ea827fb7266491f2813635de6f17269be881f696fbfdf2d83dda33e
FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04@sha256:d94c97dd9cacf183d0a6fd12a8e87b526e9e928307674ae9c94139139c0c6eae

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ARG TARGETARCH
ARG UBUNTU_SNAPSHOT=20260902T000000Z
ARG POWERSHELL_VERSION=7.6.5
ARG POWERSHELL_SHA256=b34ab3b19acac1d3d4d0d3cfdb02acf62f457b0b6a962ff008132033f7566844
ARG AZURE_CLI_VERSION=2.90.0
ARG AZURE_CLI_DEB_VERSION=2.90.0-1~noble
ARG AZURE_CLI_SHA256=ac305806dda839e0857c35f26c05ac7eeecbfdf3ca1c2cc562e1d5124cd044ab
ARG BICEP_VERSION=0.46.1
ARG BICEP_SHA256=3e011d629ea4311b7a7dd8f0040ab2b1a072ea4ff5d02cb75e0e55a9a6703fb9
ARG AZCOPY_VERSION=10.32.8
ARG AZCOPY_SHA256=a95277dbc265912cefdddbaf251aa99ec648cb18ba657e8788066357a9022dc3
ARG PYTHON_VERSION=3.12.14
ARG PYTHON_SHA256=6c6df908d2c3fd24e6d76869e92542abd0f33aec9dfc18df8875f89660286d43
ARG NODE_VERSION=22.23.2
ARG NODE_SHA256=d60acfe00a2932254bb0ad20e01b0d74397a0875595de719654b214f4b03f307
ARG AZ_MODULE_VERSION=16.3.0
ARG GRAPH_MODULE_VERSION=2.39.0
ARG PESTER_VERSION=5.7.1
ARG PSSCRIPTANALYZER_VERSION=1.25.0

ENV AZURE_CORE_COLLECT_TELEMETRY=no \
    AZURE_CORE_ONLY_SHOW_ERRORS=true \
    AZURE_EXTENSION_DIR=/opt/az305/azure-cli-extensions \
    AZURE_EXTENSION_USE_DYNAMIC_INSTALL=no \
    DOTNET_CLI_TELEMETRY_OPTOUT=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    POWERSHELL_TELEMETRY_OPTOUT=1 \
    PATH=/opt/python/3.12.14/bin:/opt/node-v22.23.2-linux-x64/bin:/opt/microsoft/powershell/7:/usr/local/bin:${PATH}

RUN if [[ "${TARGETARCH:-amd64}" != "amd64" ]]; then \
      echo "This locked image currently supports linux/amd64 only; received ${TARGETARCH}." >&2; exit 1; \
    fi \
    && export DEBIAN_FRONTEND=noninteractive \
    && sed --in-place \
      "s#http://archive.ubuntu.com/ubuntu/#https://snapshot.ubuntu.com/ubuntu/${UBUNTU_SNAPSHOT}/#g; s#http://security.ubuntu.com/ubuntu/#https://snapshot.ubuntu.com/ubuntu/${UBUNTU_SNAPSHOT}/#g" \
      /etc/apt/sources.list.d/ubuntu.sources \
    && printf '%s\n' 'Acquire::Check-Valid-Until "false";' > /etc/apt/apt.conf.d/99az305-snapshot \
    && apt-get update \
    && apt-get install --yes --no-install-recommends \
      build-essential=12.10ubuntu1 ca-certificates=20260601~24.04.1 \
      curl=8.5.0-2ubuntu10.13 git=1:2.43.0-1ubuntu7.3 jq=1.7.1-3ubuntu0.24.04.2 \
      libbz2-dev=1.0.8-5.1ubuntu0.1 libdb5.3-dev=5.3.28+dfsg2-7 \
      libexpat1-dev=2.6.1-2ubuntu0.4 libffi-dev=3.4.6-1build1 \
      libgdbm-dev=1.23-5.1build1 libgssapi-krb5-2=1.20.1-6ubuntu2.8 \
      libicu74=74.2-1ubuntu3.1 liblzma-dev=5.6.1+really5.4.5-1ubuntu0.3 \
      libncurses-dev=6.4+20240113-1ubuntu2.2 libreadline-dev=8.2-4build1 \
      libsqlite3-dev=3.45.1-1ubuntu2.7 libssl-dev=3.0.13-0ubuntu3.15 \
      libunwind8=1.6.2-3build1.1 libuuid1=2.39.3-9ubuntu6.6 \
      pkg-config=1.8.1-2build1 tk-dev=8.6.14build1 unzip=6.0-28ubuntu4.1 \
      uuid-dev=2.39.3-9ubuntu6.6 xz-utils=5.6.1+really5.4.5-1ubuntu0.3 \
      zlib1g-dev=1:1.3.dfsg-3.1ubuntu2.2 \
    && curl --fail --show-error --location \
      "https://github.com/PowerShell/PowerShell/releases/download/v${POWERSHELL_VERSION}/powershell-${POWERSHELL_VERSION}-linux-x64.tar.gz" \
      --output /tmp/powershell.tar.gz \
    && echo "${POWERSHELL_SHA256}  /tmp/powershell.tar.gz" | sha256sum --check --strict \
    && mkdir --parents "/opt/microsoft/powershell/${POWERSHELL_VERSION}" \
    && tar --extract --gzip --file /tmp/powershell.tar.gz --directory "/opt/microsoft/powershell/${POWERSHELL_VERSION}" \
    && chmod 0755 "/opt/microsoft/powershell/${POWERSHELL_VERSION}/pwsh" \
    && ln --symbolic --force "/opt/microsoft/powershell/${POWERSHELL_VERSION}" /opt/microsoft/powershell/7 \
    && ln --symbolic --force /opt/microsoft/powershell/7/pwsh /usr/local/bin/pwsh \
    && curl --fail --show-error --location \
      "https://packages.microsoft.com/repos/azure-cli/pool/main/a/azure-cli/azure-cli_${AZURE_CLI_DEB_VERSION}_amd64.deb" \
      --output /tmp/azure-cli.deb \
    && echo "${AZURE_CLI_SHA256}  /tmp/azure-cli.deb" | sha256sum --check --strict \
    && apt-get install --yes --no-install-recommends /tmp/azure-cli.deb \
    && curl --fail --show-error --location \
      "https://github.com/Azure/bicep/releases/download/v${BICEP_VERSION}/bicep-linux-x64" \
      --output /usr/local/bin/bicep \
    && echo "${BICEP_SHA256}  /usr/local/bin/bicep" | sha256sum --check --strict \
    && chmod 0755 /usr/local/bin/bicep \
    && curl --fail --show-error --location \
      "https://github.com/Azure/azure-storage-azcopy/releases/download/v${AZCOPY_VERSION}/azcopy_linux_amd64_${AZCOPY_VERSION}.tar.gz" \
      --output /tmp/azcopy.tar.gz \
    && echo "${AZCOPY_SHA256}  /tmp/azcopy.tar.gz" | sha256sum --check --strict \
    && mkdir --parents /tmp/azcopy \
    && tar --extract --gzip --file /tmp/azcopy.tar.gz --directory /tmp/azcopy \
    && install -m 0755 "$(find /tmp/azcopy -type f -name azcopy -print -quit)" /usr/local/bin/azcopy \
    && curl --fail --show-error --location \
      "https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz" \
      --output /tmp/python.tgz \
    && echo "${PYTHON_SHA256}  /tmp/python.tgz" | sha256sum --check --strict \
    && mkdir --parents /tmp/python-source \
    && tar --extract --gzip --strip-components=1 --file /tmp/python.tgz --directory /tmp/python-source \
    && cd /tmp/python-source \
    && ./configure --prefix="/opt/python/${PYTHON_VERSION}" --with-ensurepip=install \
    && make --jobs "$(nproc)" \
    && make install \
    && ln --symbolic --force "/opt/python/${PYTHON_VERSION}/bin/python3.12" /usr/local/bin/python \
    && ln --symbolic --force "/opt/python/${PYTHON_VERSION}/bin/python3.12" /usr/local/bin/python3 \
    && ln --symbolic --force "/opt/python/${PYTHON_VERSION}/bin/pip3.12" /usr/local/bin/pip \
    && ln --symbolic --force "/opt/python/${PYTHON_VERSION}/bin/pip3.12" /usr/local/bin/pip3 \
    && curl --fail --show-error --location \
      "https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.xz" \
      --output /tmp/node.tar.xz \
    && echo "${NODE_SHA256}  /tmp/node.tar.xz" | sha256sum --check --strict \
    && tar --extract --xz --file /tmp/node.tar.xz --directory /opt \
    && for executable in node npm npx corepack; do \
      ln --symbolic --force "/opt/node-v${NODE_VERSION}-linux-x64/bin/${executable}" "/usr/local/bin/${executable}"; \
    done \
    && rm --force /tmp/powershell.tar.gz /tmp/azure-cli.deb /tmp/bicep /tmp/azcopy.tar.gz /tmp/python.tgz /tmp/node.tar.xz \
    && rm --recursive --force /tmp/azcopy /tmp/python-source \
    && apt-get clean \
    && rm --recursive --force /var/lib/apt/lists/*

COPY tools/azure-cli-extensions.lock.json /opt/az305/toolchain/azure-cli-extensions.lock.json

RUN mkdir --parents "${AZURE_EXTENSION_DIR}" /tmp/az305-cli-extensions \
    && while IFS=$'\t' read -r extension version filename uri expected_hash expected_size; do \
      package="/tmp/az305-cli-extensions/${filename}"; \
      curl --fail --show-error --location "${uri}" --output "${package}"; \
      echo "${expected_hash}  ${package}" | sha256sum --check --strict; \
      test "$(stat --format='%s' "${package}")" = "${expected_size}"; \
      PIP_NO_INDEX=1 az extension add --source "${package}" --yes --only-show-errors; \
      test "$(az extension show --name "${extension}" --query version --output tsv)" = "${version}"; \
      az extension show --name "${extension}" --output json \
        | jq --exit-status '(.metadata["azext.isPreview"] // false) == false' > /dev/null; \
    done < <(jq --raw-output '.extensions[] | [.name, .version, .filename, .uri, .sha256, .size] | @tsv' /opt/az305/toolchain/azure-cli-extensions.lock.json) \
    && chmod --recursive a+rX "${AZURE_EXTENSION_DIR}" \
    && rm --recursive --force /tmp/az305-cli-extensions

ENV AZ_MODULE_VERSION=16.3.0 \
    GRAPH_MODULE_VERSION=2.39.0 \
    PESTER_VERSION=5.7.1 \
    PSSCRIPTANALYZER_VERSION=1.25.0

COPY tools/powershell-packages.lock.json /opt/az305/toolchain/powershell-packages.lock.json

RUN mkdir --parents /tmp/az305-psgallery /usr/local/share/powershell/Modules \
    && while IFS=$'\t' read -r module version uri expected_hash; do \
      package="/tmp/az305-psgallery/${module}.${version}.nupkg"; \
      target="/usr/local/share/powershell/Modules/${module}/${version}"; \
      curl --fail --show-error --location "${uri}" --output "${package}"; \
      echo "${expected_hash}  ${package}" | sha256sum --check --strict; \
      mkdir --parents "${target}"; \
      unzip -q "${package}" -d "${target}"; \
      test -f "${target}/${module}.psd1"; \
      rm --recursive --force "${target}/_rels" "${target}/package"; \
      rm --force "${target}/[Content_Types].xml" "${target}/${module}.nuspec" "${target}/.signature.p7s"; \
    done < <(jq --raw-output '.packages[] | [.name, .version, .uri, .sha256] | @tsv' /opt/az305/toolchain/powershell-packages.lock.json) \
    && rm --recursive --force /tmp/az305-psgallery

ARG ACTIONLINT_VERSION=1.7.12
ARG ACTIONLINT_SHA256=8aca8db96f1b94770f1b0d72b6dddcb1ebb8123cb3712530b08cc387b349a3d8
ARG GITLEAKS_VERSION=8.30.1
ARG GITLEAKS_SHA256=551f6fc83ea457d62a0d98237cbad105af8d557003051f41f3e7ca7b3f2470eb

RUN curl --fail --show-error --location \
      "https://github.com/rhysd/actionlint/releases/download/v${ACTIONLINT_VERSION}/actionlint_${ACTIONLINT_VERSION}_linux_amd64.tar.gz" \
      --output /tmp/actionlint.tar.gz \
    && echo "${ACTIONLINT_SHA256}  /tmp/actionlint.tar.gz" | sha256sum --check --strict \
    && mkdir --parents /tmp/actionlint \
    && tar --extract --gzip --file /tmp/actionlint.tar.gz --directory /tmp/actionlint \
    && install -m 0755 /tmp/actionlint/actionlint /usr/local/bin/actionlint \
    && curl --fail --show-error --location \
      "https://github.com/gitleaks/gitleaks/releases/download/v${GITLEAKS_VERSION}/gitleaks_${GITLEAKS_VERSION}_linux_x64.tar.gz" \
      --output /tmp/gitleaks.tar.gz \
    && echo "${GITLEAKS_SHA256}  /tmp/gitleaks.tar.gz" | sha256sum --check --strict \
    && mkdir --parents /tmp/gitleaks \
    && tar --extract --gzip --file /tmp/gitleaks.tar.gz --directory /tmp/gitleaks \
    && install -m 0755 /tmp/gitleaks/gitleaks /usr/local/bin/gitleaks \
    && rm --recursive --force /tmp/actionlint /tmp/gitleaks \
    && rm --force /tmp/actionlint.tar.gz /tmp/gitleaks.tar.gz

COPY package.json package-lock.json /opt/az305/node-quality/

RUN cd /opt/az305/node-quality \
    && npm ci --ignore-scripts --no-audit --no-fund

ENV PATH=/opt/az305/node-quality/node_modules/.bin:${PATH}

COPY requirements-container.lock.txt /tmp/az305-requirements/

RUN python -m pip install --no-cache-dir \
      --require-hashes \
      --requirement /tmp/az305-requirements/requirements-container.lock.txt \
    && python -m pip check \
    && rm --recursive --force /tmp/az305-requirements

COPY tools/container-lock.json tools/quality-tools-lock.json tools/azure-cli-extensions.lock.json tools/Test-ContainerToolchain.ps1 /opt/az305/toolchain/

RUN pwsh -NoLogo -NoProfile -File /opt/az305/toolchain/Test-ContainerToolchain.ps1 \
      -LockFile /opt/az305/toolchain/container-lock.json -Strict

WORKDIR /workspaces/az-305
