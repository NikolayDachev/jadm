# $FreeBSD$

PORTNAME=       jadm
PORTVERSION=    0.7
CATEGORIES=     sysutils

USE_GITHUB=     yes
GH_ACCOUNT=     NikolayDachev
GH_COMMIT=      6999a3c
GH_TAGNAME=     v0.7

MAINTAINER=     jadm@dachev.info
COMMENT=        FreeBSD jail framework with vnet, zfs and jail.conf support

MAN8=           jadm.8                                                                 

USE_PYTHON=yes
USE_PYDISTUTILS=steuptools

DEPENDS= py-pip:${PORTSDIR}/devel/py-pip 

post-install:
	pip install tabulate
	pip install ipaddress
	pip install netifaces

pre-install:
	${INSTALL_MAN} ${WRKSRC}/${MAN8} ${STAGEDIR}${PREFIX}/man/man8/${MAN8}

.include <bsd.port.mk>

