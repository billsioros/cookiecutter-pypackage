FROM mcr.microsoft.com/devcontainers/python:1-3.9-bullseye

# Set up zsh
RUN apt-get update && \
    apt-get install -y zsh curl fonts-powerline fonts-firacode \
    && chsh -s /usr/bin/zsh

# Install Meslo Nerd Font
RUN mkdir -p /usr/share/fonts/truetype/meslo \
    && curl -sSL -o /usr/share/fonts/truetype/meslo/MesloLGS_NF-Regular.ttf https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Regular.ttf \
    && curl -sSL -o /usr/share/fonts/truetype/meslo/MesloLGS_NF-Bold.ttf https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold.ttf \
    && curl -sSL -o /usr/share/fonts/truetype/meslo/MesloLGS_NF-Italic.ttf https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Italic.ttf \
    && curl -sSL -o /usr/share/fonts/truetype/meslo/MesloLGS_NF-BoldItalic.ttf https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold%20Italic.ttf \
    && fc-cache -f -v

# Set up Oh-my-Zsh
ENV ZSH="${HOME}/.oh-my-zsh"
RUN rm -rf ${ZSH}
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
RUN sed -i 's/ZSH_THEME=.*/ZSH_THEME="powerlevel10k\/powerlevel10k"/' ${HOME}/.zshrc

# Install Powerlevel10k theme
RUN git clone --depth=1 https://github.com/romkatv/powerlevel10k.git $ZSH/themes/powerlevel10k

# Install zsh-autosuggestions
RUN git clone --depth=1 https://github.com/zsh-users/zsh-autosuggestions.git $ZSH/plugins/zsh-autosuggestions

# Install zsh-completions
RUN git clone --depth=1 https://github.com/zsh-users/zsh-completions.git $ZSH/plugins/zsh-completions

# Install zsh-syntax-highlighting
RUN git clone --depth=1 https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH/plugins/zsh-syntax-highlighting

# Install additional plugins
RUN sed -i 's/^plugins=(\(.*\))/plugins=(git poetry docker zsh-autosuggestions zsh-completions zsh-syntax-highlighting)/' ${HOME}/.zshrc

# Set up Poetry
ENV PATH="${HOME}/.poetry/bin:${PATH}"
ENV POETRY_HOME=${HOME}/.poetry
ENV POETRY_NO_INTERACTION=1
ENV POETRY_VIRTUALENVS_CREATE=0
ENV POETRY_VERSION=1.2.2
RUN curl -sSL https://install.python-poetry.org | python -
RUN mkdir -p ${HOME}/.cache/pypoetry/virtualenvs
RUN touch ${HOME}/.cache/pypoetry/virtualenvs/envs.toml

RUN mkdir /workspaces
