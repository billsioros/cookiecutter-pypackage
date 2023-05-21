FROM gitpod/workspace-full:2022-06-06-17-32-06

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV PATH="${HOME}/.poetry/bin:${PATH}" \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=0 \
    POETRY_VERSION=1.2.2

RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.2/zsh-in-docker.sh)" -- \
    -p git \
    -p poetry \
    -p pyenv \
    -p docker \
    -p https://github.com/zsh-users/zsh-autosuggestions \
    -p https://github.com/zsh-users/zsh-completions \
    -p https://github.com/zsh-users/zsh-syntax-highlighting \
    -a 'ENABLE_CORRECTION="true"' \
    -a 'COMPLETION_WAITING_DOTS="true"' \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 - \
    && pyenv update \
    && pyenv install -s 3.8.9 \
    && pyenv local 3.8.9 \
    && if ! grep -q "export PIP_USER=no" "$HOME/.bashrc"; then printf '%s\n' "export PIP_USER=no" >> "$HOME/.bashrc"; fi
