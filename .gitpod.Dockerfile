FROM gitpod/workspace-full

RUN python3 -m pip install --upgrade pip \
    && pip install pipx \
    && pipx install cookiecutter \
    && pipx install poetry \
    && pipx install nox \
    && pipx inject nox nox-poetry \
    && pipx ensurepath \
    && export PATH=$PATH:/home/gitpod/.local/bin \
    && cd /home/gitpod/.pyenv/plugins/python-build/../.. \
    && git pull \
    && cd /home/gitpod \
    && pyenv install 3.7.12 \
    && pyenv install 3.9.9 \
    && pyenv install 3.10.1