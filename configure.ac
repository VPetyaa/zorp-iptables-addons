
AC_INIT([iptables-addons], [1.0.0])

AC_CONFIG_HEADERS([config.h])
AC_CONFIG_MACRO_DIR([m4])
AC_PROG_INSTALL
AM_INIT_AUTOMAKE([-Wall])
AC_PROG_CC
AM_PROG_CC_C_O
AC_DISABLE_STATIC
AM_PROG_LIBTOOL

AC_PREFIX_DEFAULT(/usr/local)

if test "x$prefix" = "xNONE"; then
        prefix=$ac_default_prefix
fi

AC_CHECK_HEADERS([linux/netfilter/x_tables.h], [],
	[AC_MSG_ERROR([You need to have linux/netfilter/x_tables.h])])
PKG_CHECK_MODULES([libxtables], [xtables >= 1.4.5])

ADDONS_DIR="${prefix}/lib/xtables"

AC_SUBST(ADDONS_DIR)

AC_CONFIG_FILES([Makefile extensions/GNUmakefile	])
AC_OUTPUT
