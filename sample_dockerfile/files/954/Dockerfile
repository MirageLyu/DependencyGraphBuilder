from ubuntu:15.10
ENV LDAP_USER=dev
ENV LDAP_ID=2051813
ENV LDAP_HOME=/home/$LDAP_USER
ADD bash_scripts  /tmp/bash_scripts
RUN apt-get install -y apt-utils && apt-get update &&   apt-get install -y inetutils-tools aptitude apt-file net-tools g++ xz-utils cmake net-tools inetutils-ping vim aptitude net-tools git golang python python-dev golang-go.tools && \
useradd -u $LDAP_ID -g 0 $LDAP_USER -m && \

cp /tmp/bash_scripts/root_bash_aliases /root/.bash_aliases && cp /tmp/bash_scripts/root_bash_extras /root/.bash_extras && cat /tmp/bash_scripts/root_bashrc > /root/.bashrc && cp /tmp/bash_scripts/bash_powerline02.sh /root/bash_powerline02.sh && \

cp /tmp/bash_scripts/user_bash_aliases ${LDAP_HOME}/.bash_aliases && cp /tmp/bash_scripts/user_bash_extras $LDAP_HOME/.bash_extras && cat /tmp/bash_scripts/user_bashrc > $LDAP_HOME/.bashrc && cp /tmp/bash_scripts/bash_powerline02.sh $LDAP_HOME/bash_powerline02.sh

ADD vim_scripts/vimrc $LDAP_HOME/.vimrc
RUN git clone https://github.com/imkin/bash-powerline.git $LDAP_HOME/bash_powerline && mkdir -p $LDAP_HOME/.vim/bundle && \
git clone git://github.com/altercation/vim-colors-solarized.git $LDAP_HOME/.vim/bundle/vim-colors-solarized && \
git clone https://github.com/VundleVim/Vundle.vim.git $LDAP_HOME/.vim/bundle/Vundle.vim && \
chown -R $LDAP_USER $LDAP_HOME && \
su $LDAP_USER -c 'vim +PluginInstall +qall && ~/.vim/bundle/YouCompleteMe/install.py --clang --clang-completer --gocode-completer' && \
chmod -R go+rw /usr/local
