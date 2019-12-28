FROM pritunl/archlinux

# RUN echo [archlinuxfr] >> /etc/pacman.conf
# RUN echo SigLevel = Never  >> /etc/pacman.conf
# RUN echo Server = 'http://repo.archlinux.fr/$arch' >> /etc/pacman.conf
# RUN pacman -Sy --noconfirm --needed yaourt

RUN pacman -Syy --noconfirm --needed wget git mercurial unzip base-devel

RUN git clone https://github.com/gmkurtzer/singularity.git /tmp/singularity
WORKDIR /tmp/singularity
RUN ./autogen.sh
RUN ./configure --prefix=/usr/local --sysconfdir=/etc
RUN make
RUN sudo make install

RUN hg clone http://hg.code.sf.net/p/octave/mpi /tmp/mpi
WORKDIR /tmp/mpi
RUN hg archive ../mpi.zip
RUN octave-cli --eval 'pkg install ../mpi.zip'

RUN pacman -Syy --noconfirm --needed octave

RUN git clone https://github.com/open-mpi/ompi.git /tmp/ompi
WORKDIR /tmp/ompi
RUN ./autogen.pl
RUN ./configure --prefix=/usr/local
RUN make
RUN make install

ENTRYPOINT singularity

