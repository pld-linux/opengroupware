# TODO: spec filename vs Name
# - translate all packages to pl
# - check spellings and typos
# - tweak BR and R to fit PLD
# - check init scripts
# - cleanup and rel 1
# - scavange descriptions of subpackages
# - change %files section to PLD-like
# - make a trigger bout further installing (making database, initializing it etc..)
%define		nightlybuild	r1524
%define		ogo_makeflags	-s
%define		zid_ver		1.3
%define		xmlrpcd_ver	1.1
%define		datatrunk	200601231502
%define		libversion	5.3
%define		zide_v		1.5

Summary:	OpenGroupware
Summary(pl.UTF-8):	OpenGroupware
Name:		opengroupware.org
Version:	1.1
Release:	0.6
License:	GPL
Group:		Libraries
Source0:	http://download.opengroupware.org/nightly/sources/trunk/%{name}-trunk-%{nightlybuild}-%{datatrunk}.tar.gz
# Source0-md5:	f4d97c9fc4f533b936202a3a05e24efa
Source1:	ogo-webui.init
Source2:	ogo-nhsd.init
Source3:	ogo-xmlrpcd.init
Source4:	ogo-zidestore.init
Source5:	ogo-aptnotify.sh
URL:		http://www.opengroupware.org/
BuildRequires:	apache-devel >= 2.0.40
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glibc-devel
BuildRequires:	gnustep-extensions-devel
BuildRequires:	gnustep-make-libFoundation-devel
#BuildRequires:	opengroupware.org-pilot-link-devel
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	openssl-devel >= 0.9.7
#BuildRequires:	pilot-link-devel
BuildRequires:	postgresql-devel
#BuildRequires:	sope-EOF-devel
BuildRequires:	sope-appserver-devel
BuildRequires:	sope-core-devel
BuildRequires:	sope-gdl1-devel
BuildRequires:	sope-ical-devel
BuildRequires:	sope-ldap-devel
BuildRequires:	sope-mime-devel
BuildRequires:	sope-xml-devel
Requires:	apache >= 2.0.40
#Requires:	glibc
Requires:	glibc >= 6:2.3.5-7.6
#Requires:	openldap
Requires:	openssl >= 0.9.7
#Requires:	pilot-link
# local???
Requires:	postgresql
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#echo "LDPATH=/usr/lib/opengroupware.org/Libraries/ix86/linux-gnu/gnu-fd-nil/" >> /etc/env.d/50ogo

%define		GNUSTEP_DIR		%{_libdir}/GNUstep-libFoundation

%define		OGO_USER			ogo
%define		OGO_GROUP		skyrix
%define		OGO_HOME			%{_var}/lib/opengroupware.org
%define		OGO_SHELL		/bin/sh
%define		OGO_SYSCONF		ogo-webui
%define		OGO_PREFIX		%{_prefix}

%define		OGO_INIT_NAME			ogo-webui
%define		OGO_INIT_VERSION		ogo-webui-%{version}
%define		OGO_INIT_PREFIX		%{_prefix}

%define		NHSD_SYSCONF			ogo-nhsd
%define		NHSD_INIT_NAME			ogo-nhsd
%define		NHSD_INIT_VERSION		ogo-nhsd-%{version}
%define		NHSD_INIT_PREFIX		%{_prefix}

%define		XMLRPCD_SYSCONF			ogo-xmlrpcd
%define		XMLRPCD_INIT_NAME			ogo-xmlrpcd
%define		XMLRPCD_INIT_VERSION		ogo-xmlrpcd-%{version}
%define		XMLRPCD_INIT_PREFIX		%{_prefix}

%define		ZIDESTORE_SYSCONF				ogo-zidestore
%define		ZIDESTORE_INIT_NAME			ogo-zidestore
%define		ZIDESTORE_INIT_VERSION		ogo-zidestore-%{zide_v}
%define		ZIDESTORE_INIT_PREFIX		%{_prefix}

%define		WEBUI_OLD_INIT			ogo-webui-1.0a
%define		NHSD_OLD_INIT			ogo-nhsd-1.0a
%define		ZIDESTORE_OLD_INIT	ogo-zidestore-1.3


%description
OGo.

%description -l pl.UTF-8
OGo.

%package docapi
Summary:	docapi
Group:		Libraries

%description docapi
docapi package.

%package docapi-fs-project
Summary:	docapi fs project
Group:		Libraries

%description docapi-fs-project
docapi filesystem project package.

%package docapi-fs-project-devel
Summary:	docapi fs project devel
Group:		Development/Libraries
Requires:	%{name}-docapi-fs-project = %{version}-%{release}

%description docapi-fs-project-devel
docapi filesystem project devel package.

%package docapi-db-project
Summary:	docapi db project
Group:		Libraries

%description docapi-db-project
docapi database project package.

%package docapi-db-project-devel
Summary:	docapi db project devel
Group:		Development/Libraries
Requires:	%{name}-docapi-db-project = %{version}-%{release}

%description docapi-db-project-devel
docapi database project devel package.

%package docapi-devel
Summary:	docapi-devel
Group:		Libraries
Requires:	%{name}-docapi = %{version}-%{release}

%description docapi-devel
docapi devel package.

%package logic
Summary:	logic
Group:		Libraries

%description logic
logic package.

%package logic-tools
Summary:	logic-tools
Group:		Libraries

%description logic-tools
logic tools package.

%package logic-devel
Summary:	logic-devel
Group:		Development/Libraries
Requires:	%{name}-logic = %{version}-%{release}

%description logic-devel
logic devel package.

%package pda
Summary:	pda
Group:		Libraries
#Requires:	opengroupware.org-pilot-link
#Requires:	pilot-link

%description pda
pda package.

%package pda-devel
Summary:	pda devel
Group:		Development/Libraries
Requires:	%{name}-pda = %{version}-%{release}

%description pda-devel
pda devel package.

%package theme-default
Summary:	theme default
Group:		Libraries

%description theme-default
theme default package.

%package theme-ooo
Summary:	theme ooo
Group:		Libraries

%description theme-ooo
theme ooo package.

%package theme-blue
Summary:	theme blue
Group:		Libraries

%description theme-blue
theme blue package.

%package theme-kde
Summary:	theme kde
Group:		Libraries

%description theme-kde
theme kde package.

%package theme-orange
Summary:	theme orange
Group:		Libraries

%description theme-orange
theme orange package.

%package tools
Summary:	tools
Group:		Libraries
Requires:	glibc >= 6:2.3.5-7.6

%description tools
tools package.

%package webui-app
Summary:	webui app
Group:		Libraries

%description webui-app
webui app package.

%package webui-core
Summary:	webui core
Group:		Libraries

%description webui-core
webui core package.

%package webui-core-devel
Summary:	webui core devel
Group:		Development/Libraries
Requires:	%{name}-webui-core = %{version}-%{release}

%description webui-core-devel
webui core devel package.

%package webui-calendar
Summary:	webui calendar
Group:		Libraries

%description webui-calendar
webui calendar package.

%package webui-contact
Summary:	webui contact
Group:		Libraries

%description webui-contact
webui contact package.

%package webui-mailer
Summary:	webui mailer
Group:		Libraries

%description webui-mailer
webui mailer package.

%package webui-mailer-devel
Summary:	webui mailer devel
Group:		Development/Libraries
Requires:	%{name}-webui-mailer = %{version}-%{release}

%description webui-mailer-devel
This package contains the development files for the mailer component
of OpenGroupware.org's Web UI

%package webui-news
Summary:	News component of OpenGroupware.org's Web UI
Group:		Development/Libraries
#Requires:	sope%{smaj}%{smin}-appserver sope%{smaj}%{smin}-core sope%{smaj}%{smin}-gdl1 sope%{smaj}%{smin}-ldap sope%{smaj}%{smin}-mime sope%{smaj}%{smin}-xml ogo-docapi ogo-logic ogo-webui-app ogo-webui-core libfoundation%{lfmaj}%{lfmin} libobjc-lf2
#AutoReqProv:	off

%description webui-news
The news component shows recent appointments and tasks for each user.
Additionally it supports the creation and display of simple news items.

%package webui-task
Summary:	Task component of OpenGroupware.org's Web UI
Group:		Development/Libraries
#Requires:	ogo-webui-app ogo-webui-core
#AutoReqProv:	off

%description webui-task
The task component enables users to assign and manage tasks
related to projects or standalone.

%package webui-project
Summary:	Project component of OpenGroupware.org's Web UI
Group:		Development/Libraries
#Requires:	sope%{smaj}%{smin}-appserver sope%{smaj}%{smin}-core sope%{smaj}%{smin}-gdl1 sope%{smaj}%{smin}-ldap sope%{smaj}%{smin}-mime sope%{smaj}%{smin}-xml ogo-docapi ogo-logic ogo-webui-app ogo-webui-core libfoundation%{lfmaj}%{lfmin} libobjc-lf2
#AutoReqProv:	off

%description webui-project
The project component adds project management capabilities to
OpenGroupware.org's web UI. It allows to assign and track a
project's status, add documents and links and interworks nicely
with the task component to assign specific tasks within a project.

%package webui-resource-basque
Summary:	Basque translation for OpenGroupware.org's web UI
Group:		Development/Libraries
#Requires:	ogo-webui-app
#AutoReqProv:	off

%description webui-resource-basque
This package contains the Basque translation for OpenGroupware.org's web UI.
##
%package webui-resource-dk
Summary:	Danish translation for OpenGroupware.org's web UI
Group:		Development/Libraries
#Requires:	ogo-webui-app
#AutoReqProv:	off

%description webui-resource-dk
This package contains the Danish translation for OpenGroupware.org's web UI.
##
%package webui-resource-nl
Summary:	Dutch translation for OpenGroupware.org's web UI
Group:		Development/Libraries
#Requires:	ogo-webui-app
#AutoReqProv:	off

%description webui-resource-nl
This package contains the Dutch translation for OpenGroupware.org's web UI.
##
%package webui-resource-en
Summary:	English translation for OpenGroupware.org's web UI
Group:		Development/Libraries
#Requires:	ogo-webui-app
#AutoReqProv:	off

%description webui-resource-en
This package contains the English translation for OpenGroupware.org's web UI.
##
%package webui-resource-fr
Summary:	French translation for OpenGroupware.org's web UI
Group:		Development/Libraries
#Requires:	ogo-webui-app
#AutoReqProv:	off

%description webui-resource-fr
This package contains the French translation for OpenGroupware.org's web UI.
##
%package webui-resource-de
Summary:	German translation for OpenGroupware.org's web UI
Group:		Development/Libraries
#Requires:	ogo-webui-app
#AutoReqProv:	off

%description webui-resource-de
This package contains the German translation for OpenGroupware.org's web UI.
##
%package webui-resource-hu
Summary:	Hungarian translation for OpenGroupware.org's web UI
Group:		Development/Libraries
#Requires:	ogo-webui-app
#AutoReqProv:	off

%description webui-resource-hu
This package contains the Hungarian translation for OpenGroupware.org's web UI.
##
%package webui-resource-it
Summary:	Italian translation for OpenGroupware.org's web UI
Group:		Development/Libraries
#Requires:	ogo-webui-app
#AutoReqProv:	off

%description webui-resource-it
This package contains the Italian translation for OpenGroupware.org's web UI.
##
%package webui-resource-jp
Summary:	Japanese translation for OpenGroupware.org's web UI
Group:		Development/Libraries
#Requires:	ogo-webui-app
#AutoReqProv:	off

%description webui-resource-jp
This package contains the Japanese translation for OpenGroupware.org's web UI.
##
%package webui-resource-no
Summary:	Norwegian translation for OpenGroupware.org's web UI
Group:		Development/Libraries
#Requires:	ogo-webui-app
#AutoReqProv:	off

%description webui-resource-no
This package contains the Norwegian translation for OpenGroupware.org's web UI.
##
%package webui-resource-pl
Summary:	Polish translation for OpenGroupware.org's web UI
Group:		Development/Libraries
#Requires:	ogo-webui-app
#AutoReqProv:	off

%description webui-resource-pl
This package contains the Polish translation for OpenGroupware.org's web UI.
##
%package webui-resource-pt
Summary:	Portuguese translation for OpenGroupware.org's web UI
Group:		Development/Libraries
#Requires:	ogo-webui-app
#AutoReqProv:	off

%description webui-resource-pt
This package contains the Portuguese translation for OpenGroupware.org's web UI.
##
%package webui-resource-es
Summary:	Spanish translation for OpenGroupware.org's web UI
Group:		Development/Libraries
#Requires:	ogo-webui-app
#AutoReqProv:	off

%description webui-resource-es
This package contains the Spanish translation for OpenGroupware.org's web UI.
##
%package webui-resource-sk
Summary:	Slovak translation for OpenGroupware.org's web UI
Group:		Development/Libraries
#Requires:	ogo-webui-app
#AutoReqProv:	off

%description webui-resource-sk
This package contains the Slovak translation for OpenGroupware.org's web UI.
##
%package webui-resource-ptbr
Summary:	Portuguese (Brazilian) translation for OpenGroupware.org's web UI
Group:		Development/Libraries
#Requires:	ogo-webui-app
#AutoReqProv:	off

%description webui-resource-ptbr
This package contains the Portuguese (Brazilian) translation for OpenGroupware.org's web UI.

%package xmlrpcd
Summary:	xmlrpcd
Group:		Libraries

%description xmlrpcd
xmlrpcd package.

%package zidestore
Summary:	zidestore
Group:		Libraries

%description zidestore
zidestore package.

%package zidestore-devel
Summary:	zidestore devel
Group:		Development/Libraries
Requires:	%{name}-zidestore = %{version}-%{release}

%description zidestore-devel
zidestore devel package.

%prep
%setup -q -n %{name}

%build
. %{_libdir}/GNUstep-libFoundation/System/Library/Makefiles/GNUstep.sh
LIBARY_COMBO=gnu-fd-nil
export LIBRARY_COMBO="gnu-fd-nil"
./configure \
	--prefix=${RPM_BUILD_ROOT}%{_prefix} \
	--enable-debug \
	--gsmake=%{_libdir}/GNUstep-libFoundation/System


%{__make} %{ogo_makeflags}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/GNUstep \
	$RPM_BUILD_ROOT%{_sysconfdir}/sysconfig \
	$RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d \
	$RPM_BUILD_ROOT%{_datadir}/opengroupware.org-%{version}/initscript_templates \
	$RPM_BUILD_ROOT%{_datadir}/opengroupware.org-%{version}/aptnotify_template \
	$RPM_BUILD_ROOT%{_datadir}/zidestore-%{zide_v}/initscript_templates \
	$RPM_BUILD_ROOT%{_var}/lib/opengroupware.org/.libFoundation/Defaults \
	$RPM_BUILD_ROOT%{_var}/lib/opengroupware.org/documents \
	$RPM_BUILD_ROOT%{_var}/lib/opengroupware.org/news \
	$RPM_BUILD_ROOT%{_var}/log/opengroupware



#. %{_libdir}/GNUstep-libFoundation/System/Library/Makefiles/GNUstep.sh

%{__make} %{ogo_makeflags} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_libdir}/GNUstep-libFoundation/System \
	FHS_INSTALL_ROOT=$RPM_BUILD_ROOT%{_prefix} \
	BUNDLE_INSTALL_DIR=$RPM_BUILD_ROOT%{_prefix} \
	WOBUNDLE_INSTALL_DIR=$RPM_BUILD_ROOT%{_prefix}

SHAREDIR="${RPM_BUILD_ROOT}%{_datadir}/opengroupware.org-%{version}"
rm -f "${SHAREDIR}/templates"
rm -f "${SHAREDIR}/translations"
rm -f "${SHAREDIR}/www"
cp -Rp WebUI/Templates "${SHAREDIR}/templates"
cp -Rp WebUI/Resources "${SHAREDIR}/translations"
cp -Rp Themes/WebServerResources "${SHAREDIR}/www"
rm -fr "${SHAREDIR}/templates/ChangeLog"
rm -fr "${SHAREDIR}/templates/GNUmakefile"
rm -fr "${SHAREDIR}/templates/HelpUI"
rm -fr "${SHAREDIR}/translations/COPYRIGHT"
rm -fr "${SHAREDIR}/translations/ChangeLog"
rm -fr "${SHAREDIR}/translations/GNUmakefile"
rm -fr "${SHAREDIR}/www/GNUmakefile"
rm -fr "${SHAREDIR}/www/tools"

#prepare initscript templates
INITSCRIPTS_TMP_DIR_OGO="${SHAREDIR}/initscript_templates"
INITSCRIPTS_TMP_DIR_ZIDE="${RPM_BUILD_ROOT}%{_datadir}/zidestore-%{zide_v}/initscript_templates"

install %{SOURCE1} $INITSCRIPTS_TMP_DIR_OGO/
install %{SOURCE2} $INITSCRIPTS_TMP_DIR_OGO/
install %{SOURCE3} $INITSCRIPTS_TMP_DIR_OGO/
install %{SOURCE4} $INITSCRIPTS_TMP_DIR_ZIDE/

#ghost initscripts
INITSCRIPT_DST="${RPM_BUILD_ROOT}%{_sysconfdir}/rc.d/init.d"
touch ${INITSCRIPT_DST}/%{NHSD_INIT_NAME}
touch ${INITSCRIPT_DST}/%{OGO_INIT_NAME}
touch ${INITSCRIPT_DST}/%{XMLRPCD_INIT_NAME}
touch ${INITSCRIPT_DST}/%{ZIDESTORE_INIT_NAME}

#template for ogo-aptnotify
APTNOTIFY_TMP_DIR="${SHAREDIR}/aptnotify_template"
install %{SOURCE5} ${APTNOTIFY_TMP_DIR}/

#create sysconfig
echo "RUN_DBSCRIPT=\"YES\"		# will run the whole script - or not, as thou wish
PATCH_POSTGRESQL_CONF=\"YES\"		# will backup and patch postgresql.conf - if needed
PATCH_PGHBA_CONF=\"YES\"		# will backup and patch pg_hba.conf - if needed
CREATE_DB_USER=\"YES\"			# will create a DB user for OpenGroupware.org
CREATE_DB_ITSELF=\"YES\"		# will create the DB itself for OpenGroupware.org
ROLLIN_SCHEME=\"YES\"			# will roll'in the current base DB scheme of OGo
FORCE_OVERRIDE_PRESENT_SCHEME=\"YES\"	# might harm thy current scheme (or not?)
UPDATE_SCHEMA=\"YES\"			# will attempt to update the database scheme - if needed
OGO_USER=\"ogo\"			# default username (unix) of your OGo install - might vary
PGCLIENTENCODING=\"LATIN1\"		# client encoding to use
USE_SKYAPTNOTIFY=\"YES\"		# periodically runs aptnotify - or not
" >$RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{OGO_SYSCONF}

echo "PGCLIENTENCODING=\"LATIN1\"	# client encoding to use
" >$RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{NHSD_SYSCONF}

echo "PGCLIENTENCODING=\"LATIN1\"	# client encoding to use
" >$RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{XMLRPCD_SYSCONF}

echo "PGCLIENTENCODING=\"LATIN1\"	# client encoding to use
" >$RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{ZIDESTORE_SYSCONF}

install -d $RPM_BUILD_ROOT/etc/ld.so.conf.d
echo '%{_libdir}' > $RPM_BUILD_ROOT/etc/ld.so.conf.d/opengroupware.conf
echo '%{_libdir}' > $RPM_BUILD_ROOT/etc/ld.so.conf.d/ogo.conf

%pre
if [ "$1" = "1" ]; then
	%groupadd -g 157 "%{OGO_GROUP}"
	%useradd -u 157 -d "%{OGO_HOME}" -s "%{OGO_SHELL}" -c "OpenGroupware.org User" -g "%{OGO_GROUP}" "%{OGO_USER}"
fi

%post
if [ "$1" = "1" ]; then
	cd %{_sysconfdir}
	ln -s %{_var}/lib/opengroupware.org/.libFoundation opengroupware.org
	## some defaults
	export PATH=$PATH:%{_bindir}
	##
	chmod 755 %{OGO_HOME}
	chown -R %{OGO_USER}:%{OGO_GROUP} %{OGO_HOME}
	##
	su - %{OGO_USER} -c "
	Defaults write NSGlobalDomain LSConnectionDictionary '{hostName=\"127.0.0.1\"; userName=OGo; password=\"\"; port=5432; databaseName=OGo}'
	Defaults write NSGlobalDomain LSNewsImagesPath '%{OGO_HOME}/news'
	Defaults write NSGlobalDomain LSNewsImagesUrl '/ArticleImages'
	Defaults write NSGlobalDomain skyrix_id `hostname`
	Defaults write NSGlobalDomain TimeZoneName GMT
	Defaults write NSGlobalDomain WOHttpAllowHost '( localhost, 127.0.0.1, localhost.localdomain)'
	Defaults write ogo-nhsd-%{version} NGBundlePath '%{_libdir}/opengroupware.org-%{version}/conduits'
	Defaults write skyaptnotify AptNotifyVerbose NO
	Defaults write skyaptnotify AptNotifyFromAdress '%{OGO_USER}@`hostname`'
	Defaults write skyaptnotify AptNotifySentResourcesFile '%{_var}/log/opengroupware/sent-resources'
	Defaults write skyaptnotify AptNotifySkyrixPassword '\"\"'
	Defaults write skyaptnotify AptNotifySkyrixUser root
	"
fi
/sbin/ldconfig

if [ "$1" = "2" ]; then
	if [ -e %{_var}/log/opengroupware ]; then
		chown -R %{OGO_USER}:%{OGO_GROUP} %{_var}/log/opengroupware
	fi
fi

%postun
if [ "$1" = "0" ]; then
	if [ "`getent passwd %{OGO_USER}`" ]; then
		echo -en "removing user %{OGO_USER}.\n"
		%userremove "%{OGO_USER}"
	fi
	if [ "`getent group %{OGO_GROUP}`" ]; then
		echo -en "removing group %{OGO_GROUP}.\n"
		%groupremove "%{OGO_GROUP}"
	fi
	if [ -h "%{_sysconfdir}/opengroupware.org" ]; then
		rm %{_sysconfdir}/opengroupware.org
	fi
fi
/sbin/ldconfig

%post docapi -p /sbin/ldconfig

%post docapi-fs-project -p /sbin/ldconfig

%post docapi-db-project -p /sbin/ldconfig

%post logic -p /sbin/ldconfig

%post webui-core -p /sbin/ldconfig

%post webui-mailer -p /sbin/ldconfig

%post tools
if [ "$1" = "1" ]; then
	CRON_D="%{_sysconfdir}/cron.d"
	if [ -d "$CRON_D" ]; then
		echo "*/5 * * * root %{_bindir}/ogo-aptnotify.sh >/dev/null" >%{_sysconfdir}/cron.d/ogo-aptnotify
	fi
	%{__sed} "s^OGO_SYSCONF^%{OGO_SYSCONF}^g; \
		s^OGO_PREFIX^%{OGO_PREFIX}^g" \
		"%{_datadir}/opengroupware.org-%{version}/aptnotify_template/ogo-aptnotify.sh" \
		>"%{_bindir}/ogo-aptnotify.sh"
	chmod 750 "%{_bindir}/ogo-aptnotify.sh"
fi

if [ "$1" = "2" ]; then
	CRON_D="%{_sysconfdir}/cron.d"
	if [ -d "$CRON_D" ]; then
		echo "*/5 * * * root %{_bindir}/ogo-aptnotify.sh >/dev/null" >%{_sysconfdir}/cron.d/ogo-aptnotify
	fi
	%{__sed} "s^OGO_SYSCONF^%{OGO_SYSCONF}^g; \
		s^OGO_PREFIX^%{OGO_PREFIX}^g" \
		"%{_datadir}/opengroupware.org-%{version}/aptnotify_template/ogo-aptnotify.sh" \
		>"%{_bindir}/ogo-aptnotify.sh"
	chmod 750 "%{_bindir}/ogo-aptnotify.sh"
fi

%post pda
if [ "$1" = "1" ]; then
	%{__sed} -e "s^NHSD_INIT_VERSION^%{NHSD_INIT_VERSION}^g; \
		s^NHSD_INIT_PREFIX^%{NHSD_INIT_PREFIX}^g; \
		s^NHSD_SYSCONF^%{NHSD_SYSCONF}^g; \
		s^GNUSTEP_DIR^%{GNUSTEP_DIR}^g" \
		"%{_datadir}/opengroupware.org-%{version}/initscript_templates/ogo-nhsd.init" \
		>%{_sysconfdir}/rc.d/init.d/"%{NHSD_INIT_NAME}"
	chown root:root %{_sysconfdir}/rc.d/init.d/"%{NHSD_INIT_NAME}"
	chmod 754 %{_sysconfdir}/rc.d/init.d/"%{NHSD_INIT_NAME}"
	chkconfig --add "%{NHSD_INIT_NAME}"
	/sbin/ldconfig
fi

if [ "$1" = "2" ]; then
	if [ ! -f "/etc/rc.d/init.d/%{NHSD_INIT_NAME}" ]; then
		%{__sed} "s^NHSD_INIT_VERSION^%{NHSD_INIT_VERSION}^g; \
			s^NHSD_INIT_PREFIX^%{NHSD_INIT_PREFIX}^g; \
			s^NHSD_SYSCONF^%{NHSD_SYSCONF}^g; \
			s^GNUSTEP_DIR^%{GNUSTEP_DIR}^g" \
			"%{_datadir}/opengroupware.org-%{version}/initscript_templates/ogo-nhsd.init" \
			>%{_sysconfdir}/rc.d/init.d/"%{NHSD_INIT_NAME}"
		chown root:root %{_sysconfdir}/rc.d/init.d/"%{NHSD_INIT_NAME}"
		chmod 754 %{_sysconfdir}/rc.d/init.d/"%{NHSD_INIT_NAME}"
		chkconfig --add "%{NHSD_INIT_NAME}"
		/sbin/ldconfig
	else
		%{__sed} "s^NHSD_INIT_VERSION^%{NHSD_INIT_VERSION}^g; \
			s^NHSD_INIT_PREFIX^%{NHSD_INIT_PREFIX}^g; \
			s^NHSD_SYSCONF^%{NHSD_SYSCONF}^g; \
			s^GNUSTEP_DIR^%{GNUSTEP_DIR}^g" \
			"%{_datadir}/opengroupware.org-%{version}/initscript_templates/ogo-nhsd.init" \
			>%{_sysconfdir}/rc.d/init.d/"%{NHSD_INIT_NAME}"
		chown root:root %{_sysconfdir}/rc.d/init.d/"%{NHSD_INIT_NAME}"
		chmod 754 %{_sysconfdir}/rc.d/init.d/"%{NHSD_INIT_NAME}"
	fi
	/sbin/ldconfig
	if [ -f "%{_sysconfdir}/rc.d/init.d/%{NHSD_INIT_NAME}" ]; then
		"%{_sysconfdir}/rc.d/init.d/%{NHSD_INIT_NAME}" restart >/dev/null 2>&1
	fi
fi

%post webui-app
if [ "$1" = "1" ]; then
	%{__sed} "s^OGO_INIT_VERSION^%{OGO_INIT_VERSION}^g; \
		s^OGO_INIT_PREFIX^%{OGO_INIT_PREFIX}^g; \
		s^OGO_SYSCONF^%{OGO_SYSCONF}^g; \
		s^GNUSTEP_DIR^%{GNUSTEP_DIR}^g" \
		"%{_datadir}/opengroupware.org-%{version}/initscript_templates/ogo-webui.init" \
		>%{_sysconfdir}/rc.d/init.d/"%{OGO_INIT_NAME}"
	chown root:root %{_sysconfdir}/rc.d/init.d/"%{OGO_INIT_NAME}"
	chmod 754 %{_sysconfdir}/rc.d/init.d/"%{OGO_INIT_NAME}"
	chkconfig --add "%{OGO_INIT_NAME}"
	chkconfig "%{OGO_INIT_NAME}" on
fi
/sbin/ldconfig

if [ "$1" = "2" ]; then
	if [ ! -f "/etc/rc.d/init.d/%{OGO_INIT_NAME}" ]; then
		%{__sed} "s^OGO_INIT_VERSION^%{OGO_INIT_VERSION}^g; \
			s^OGO_INIT_PREFIX^%{OGO_INIT_PREFIX}^g; \
			s^OGO_SYSCONF^%{OGO_SYSCONF}^g; \
			s^GNUSTEP_DIR^%{GNUSTEP_DIR}^g" \
			"%{_datadir}/opengroupware.org-%{version}/initscript_templates/ogo-webui.init" \
			>%{_sysconfdir}/rc.d/init.d/"%{OGO_INIT_NAME}"
		chown root:root %{_sysconfdir}/rc.d/init.d/"%{OGO_INIT_NAME}"
		chmod 754 %{_sysconfdir}/rc.d/init.d/"%{OGO_INIT_NAME}"
		chkconfig --add "%{OGO_INIT_NAME}"
		chkconfig "%{OGO_INIT_NAME}" on
	else
		%{__sed} "s^OGO_INIT_VERSION^%{OGO_INIT_VERSION}^g; \
			s^OGO_INIT_PREFIX^%{OGO_INIT_PREFIX}^g; \
			s^OGO_SYSCONF^%{OGO_SYSCONF}^g; \
			s^GNUSTEP_DIR^%{GNUSTEP_DIR}^g" \
			"%{_datadir}/opengroupware.org-%{version}/initscript_templates/ogo-webui.init" \
			>%{_sysconfdir}/rc.d/init.d/"%{OGO_INIT_NAME}"
		chown root:root %{_sysconfdir}/rc.d/init.d/"%{OGO_INIT_NAME}"
		chmod 754 %{_sysconfdir}/rc.d/init.d/"%{OGO_INIT_NAME}"
	fi
	/sbin/ldconfig
	if [ -f "%{_sysconfdir}/rc.d/init.d/%{OGO_INIT_NAME}" ]; then
		"%{_sysconfdir}/rc.d/init.d/%{OGO_INIT_NAME}" restart >/dev/null 2>&1
	fi
fi

%post xmlrpcd
if [ "$1" = "1" ]; then
	%{__sed} "s^XMLRPCD_INIT_VERSION^%{XMLRPCD_INIT_VERSION}^g; \
		s^XMLRPCD_INIT_PREFIX^%{XMLRPCD_INIT_PREFIX}^g; \
		s^XMLRPCD_SYSCONF^%{XMLRPCD_SYSCONF}^g; \
		s^GNUSTEP_DIR^%{GNUSTEP_DIR}^g" \
		"%{_datadir}/opengroupware.org-%{version}/initscript_templates/ogo-xmlrpcd.init" \
		>%{_sysconfdir}/rc.d/init.d/"%{XMLRPCD_INIT_NAME}"
	chown root:root %{_sysconfdir}/rc.d/init.d/"%{XMLRPCD_INIT_NAME}"
	chmod 754 %{_sysconfdir}/rc.d/init.d/"%{XMLRPCD_INIT_NAME}"
	chkconfig --add "%{XMLRPCD_INIT_NAME}"
	/sbin/ldconfig
fi

if [ "$1" = "2" ]; then
	if [ ! -f "/etc/init.d/%{XMLRPCD_INIT_NAME}" ]; then
		%{__sed} "s^XMLRPCD_INIT_VERSION^%{XMLRPCD_INIT_VERSION}^g; \
			s^XMLRPCD_INIT_PREFIX^%{XMLRPCD_INIT_PREFIX}^g; \
			s^XMLRPCD_SYSCONF^%{XMLRPCD_SYSCONF}^g; \
			s^GNUSTEP_DIR^%{GNUSTEP_DIR}^g" \
			"%{_datadir}/opengroupware.org-%{version}/initscript_templates/ogo-xmlrpcd.init" \
			>%{_sysconfdir}/rc.d/init.d/"%{XMLRPCD_INIT_NAME}"
		chown root:root %{_sysconfdir}/rc.d/init.d/"%{XMLRPCD_INIT_NAME}"
		chmod 754 %{_sysconfdir}/rc.d/init.d/"%{XMLRPCD_INIT_NAME}"
		chkconfig --add "%{XMLRPCD_INIT_NAME}"
		/sbin/ldconfig
	else
		%{__sed} "s^XMLRPCD_INIT_VERSION^%{XMLRPCD_INIT_VERSION}^g; \
			s^XMLRPCD_INIT_PREFIX^%{XMLRPCD_INIT_PREFIX}^g; \
			s^XMLRPCD_SYSCONF^%{XMLRPCD_SYSCONF}^g; \
			s^GNUSTEP_DIR^%{GNUSTEP_DIR}^g" \
			"%{_datadir}/opengroupware.org-%{version}/initscript_templates/ogo-xmlrpcd.init" \
			>%{_sysconfdir}/rc.d/init.d/"%{XMLRPCD_INIT_NAME}"
		chown root:root %{_sysconfdir}/rc.d/init.d/"%{XMLRPCD_INIT_NAME}"
		chmod 754 %{_sysconfdir}/rc.d/init.d/"%{XMLRPCD_INIT_NAME}"
	fi
	/sbin/ldconfig
	if [ -f "%{_sysconfdir}/rc.d/init.d/%{XMLRPCD_INIT_NAME}" ]; then
		"%{_sysconfdir}/rc.d/init.d/%{XMLRPCD_INIT_NAME}" restart >/dev/null 2>&1
	fi
fi

%post zidestore
if [ "$1" = "1" ]; then
	%{__sed} "s^ZIDESTORE_INIT_VERSION^%{ZIDESTORE_INIT_VERSION}^g; \
		s^ZIDESTORE_INIT_PREFIX^%{ZIDESTORE_INIT_PREFIX}^g; \
		s^ZIDESTORE_SYSCONF^%{ZIDESTORE_SYSCONF}^g; \
		s^GNUSTEP_DIR^%{GNUSTEP_DIR}^g" \
		"%{_datadir}/zidestore-%{zide_v}/initscript_templates/ogo-zidestore.init" \
		>%{_sysconfdir}/rc.d/init.d/"%{ZIDESTORE_INIT_NAME}"
	chown root:root %{_sysconfdir}/rc.d/init.d/"%{ZIDESTORE_INIT_NAME}"
	chmod 754 %{_sysconfdir}/rc.d/init.d/"%{ZIDESTORE_INIT_NAME}"
	chkconfig --add "%{ZIDESTORE_INIT_NAME}"
	/sbin/ldconfig
fi

if [ "$1" = "2" ]; then
	if [ ! -f "/etc/init.d/%{ZIDESTORE_INIT_NAME}" ]; then
		%{__sed} "s^ZIDESTORE_INIT_VERSION^%{ZIDESTORE_INIT_VERSION}^g; \
			s^ZIDESTORE_INIT_PREFIX^%{ZIDESTORE_INIT_PREFIX}^g; \
			s^ZIDESTORE_SYSCONF^%{ZIDESTORE_SYSCONF}^g; \
			s^GNUSTEP_DIR^%{GNUSTEP_DIR}^g" \
			"%{_datadir}/zidestore-%{zide_v}/initscript_templates/ogo-zidestore.init" \
			>%{_sysconfdir}/rc.d/init.d/"%{ZIDESTORE_INIT_NAME}"
		chown root:root %{_sysconfdir}/rc.d/init.d/"%{ZIDESTORE_INIT_NAME}"
		chmod 754 %{_sysconfdir}/rc.d/init.d/"%{ZIDESTORE_INIT_NAME}"
		chkconfig --add "%{ZIDESTORE_INIT_NAME}"
		/sbin/ldconfig
	else
		%{__sed} "s^ZIDESTORE_INIT_VERSION^%{ZIDESTORE_INIT_VERSION}^g; \
		s^ZIDESTORE_INIT_PREFIX^%{ZIDESTORE_INIT_PREFIX}^g; \
		s^ZIDESTORE_SYSCONF^%{ZIDESTORE_SYSCONF}^g; \
		s^GNUSTEP_DIR^%{GNUSTEP_DIR}^g" \
		"%{_datadir}/zidestore-%{zide_v}/initscript_templates/ogo-zidestore.init" \
		>%{_sysconfdir}/init.d/"%{ZIDESTORE_INIT_NAME}"
		chown root:root %{_sysconfdir}/rc.d/init.d/"%{ZIDESTORE_INIT_NAME}"
		chmod 754 %{_sysconfdir}/rc.d/init.d/"%{ZIDESTORE_INIT_NAME}"
	fi
	/sbin/ldconfig
	if [ -f "%{_sysconfdir}/rc.d/init.d/%{ZIDESTORE_INIT_NAME}" ]; then
		"%{_sysconfdir}/rc.d/init.d/%{ZIDESTORE_INIT_NAME}" restart >/dev/null 2>&1
	fi
fi

# ****************************** preun *********************************
%preun tools
if [ "$1" = "0" ]; then
	if [ -f "%{_sysconfdir}/cron.d/ogo-aptnotify" ]; then
		rm -f "%{_sysconfdir}/cron.d/ogo-aptnotify"
	fi
	if [ -f "%{_bindir}/ogo-aptnotify.sh" ]; then
		rm -f "%{_bindir}/ogo-aptnotify.sh"
	fi
fi

%preun pda
if [ "$1" = "0" ]; then
	if [ -f "%{_sysconfdir}/rc.d/init.d/%{NHSD_INIT_NAME}" ]; then
		service "%{NHSD_INIT_NAME}" stop
		chkconfig "%{NHSD_INIT_NAME}" off
		chkconfig --del "%{NHSD_INIT_NAME}"
		rm -f "%{_sysconfdir}/rc.d/init.d/%{NHSD_INIT_NAME}"
	fi
	/sbin/ldconfig
fi

%pre pda
if [ "$1" = "2" ]; then
	if [ -f "%{_sysconfdir}/rc.d/init.d/%{NHSD_OLD_INIT}" ]; then
		service "%{NHSD_OLD_INIT}" stop
		chkconfig "%{NHSD_OLD_INIT}" off
		chkconfig --del "%{NHSD_OLD_INIT}"
		rm -f "%{_sysconfdir}/rc.d/init.d/%{NHSD_OLD_INIT}"
	fi
fi

%preun webui-app
if [ "$1" = "0" ]; then
	if [ -f "%{_sysconfdir}/rc.d/init.d/%{OGO_INIT_NAME}" ]; then
		service "%{OGO_INIT_NAME}" stop
		chkconfig "%{OGO_INIT_NAME}" off
		chkconfig --del "%{OGO_INIT_NAME}"
		rm -f "%{_sysconfdir}/rc.d/init.d/%{OGO_INIT_NAME}"
	fi
fi
/sbin/ldconfig

%pre webui-app
if [ "$1" = "2" ]; then
	if [ -f "%{_sysconfdir}/rc.d/init.d/%{WEBUI_OLD_INIT}" ]; then
		service "%{WEBUI_OLD_INIT}" stop
		chkconfig "%{WEBUI_OLD_INIT}" off
		chkconfig --del "%{WEBUI_OLD_INIT}"
		rm -f "%{_sysconfdir}/rc.d/init.d/%{WEBUI_OLD_INIT}"
	fi
fi

%preun xmlrpcd
if [ "$1" = "0" ]; then
	if [ -f "%{_sysconfdir}/rc.d/init.d/%{XMLRPCD_INIT_NAME}" ]; then
		service "%{XMLRPCD_INIT_NAME}" stop
		chkconfig "%{XMLRPCD_INIT_NAME}" off
		chkconfig --del "%{XMLRPCD_INIT_NAME}"
		rm -f "%{_sysconfdir}/rc.d/init.d/%{XMLRPCD_INIT_NAME}"
	fi
	/sbin/ldconfig
fi

%pre xmlrpcd
if [ "$1" = "2" ]; then
	if [ -f "%{_sysconfdir}/rc.d/init.d/%{XMLRPCD_OLD_INIT}" ]; then
		service "%{XMLRPCD_OLD_INIT}" stop
		chkconfig "%{XMLRPCD_OLD_INIT}" off
		chkconfig --del "%{XMLRPCD_OLD_INIT}"
		rm -f "%{_sysconfdir}/rc.d/init.d/%{XMLRPCD_OLD_INIT}"
	fi
fi

%preun zidestore
if [ "$1" = "0" ]; then
	if [ -f "%{_sysconfdir}/rc.d/init.d/%{ZIDESTORE_INIT_NAME}" ]; then
		service "%{ZIDESTORE_INIT_NAME}" stop
		chkconfig "%{ZIDESTORE_INIT_NAME}" off
		chkconfig --del "%{ZIDESTORE_INIT_NAME}"
		rm -f "%{_sysconfdir}/rc.d/init.d/%{ZIDESTORE_INIT_NAME}"
	fi
	/sbin/ldconfig
fi

%pre zidestore
if [ "$1" = "2" ]; then
	if [ -f "%{_sysconfdir}/rc.d/init.d/%{ZIDESTORE_OLD_INIT}" ]; then
		service "%{ZIDESTORE_OLD_INIT}" stop
		chkconfig "%{ZIDESTORE_OLD_INIT}" off
		chkconfig --del "%{ZIDESTORE_OLD_INIT}"
		rm -f "%{_sysconfdir}/rc.d/init.d/%{ZIDESTORE_OLD_INIT}"
	fi 
fi


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,ogo,skyrix,-)
/etc/ld.so.conf.d/opengroupware.conf
%dir %attr(700,ogo,skyrix) %{_var}/lib/opengroupware.org/.libFoundation
%dir %attr(700,ogo,skyrix) %{_var}/lib/opengroupware.org/.libFoundation/Defaults
%dir %attr(700,ogo,skyrix) %{_var}/lib/opengroupware.org/documents
%dir %attr(755,ogo,skyrix) %{_var}/lib/opengroupware.org/news
%dir %attr(700,ogo,skyrix) %{_var}/log/opengroupware

%files docapi
%defattr(-,root,root,-)
%{_libdir}/opengroupware.org-%{version}/datasources/OGoAccounts.ds
%{_libdir}/opengroupware.org-%{version}/datasources/OGoBase.ds
%{_libdir}/opengroupware.org-%{version}/datasources/OGoContacts.ds
%{_libdir}/opengroupware.org-%{version}/datasources/OGoJobs.ds
%{_libdir}/opengroupware.org-%{version}/datasources/OGoProject.ds
%{_libdir}/opengroupware.org-%{version}/datasources/OGoRawDatabase.ds
%{_libdir}/opengroupware.org-%{version}/datasources/OGoScheduler.ds
%{_libdir}/libOGoAccounts*.so.%{libversion}*
%{_libdir}/libOGoBase*.so.%{libversion}*
%{_libdir}/libOGoContacts*.so.%{libversion}*
%{_libdir}/libOGoDocuments*.so.%{libversion}*
%{_libdir}/libOGoJobs*.so.%{libversion}*
%{_libdir}/libOGoProject*.so.%{libversion}*
%{_libdir}/libOGoRawDatabase*.so.%{libversion}*
%{_libdir}/libOGoScheduler*.so.%{libversion}*

%files docapi-fs-project
%defattr(-,root,root,-)
%{_libdir}/opengroupware.org-%{version}/datasources/OGoFileSystemProject.ds
%{_libdir}/libOGoFileSystemProject*.so.%{libversion}*

%files docapi-fs-project-devel
%defattr(-,root,root,-)
%{_includedir}/OGoFileSystemProject
%{_libdir}/libOGoFileSystemProject*.so

%files docapi-db-project
%defattr(-,root,root,-)
%{_libdir}/opengroupware.org-%{version}/datasources/OGoDatabaseProject.ds
%{_libdir}/libOGoDatabaseProject*.so.%{libversion}*

%files docapi-db-project-devel
%defattr(-,root,root,-)
%{_includedir}/OGoDatabaseProject
%{_libdir}/libOGoDatabaseProject*.so

%files docapi-devel
%defattr(-,root,root,-)
%{_includedir}/OGoAccounts
%{_includedir}/OGoBase
%{_includedir}/OGoContacts
%{_includedir}/OGoDocuments
%{_includedir}/OGoJobs
%{_includedir}/OGoProject
%{_includedir}/OGoRawDatabase
%{_includedir}/OGoScheduler
%{_libdir}/libOGoAccounts*.so
%{_libdir}/libOGoBase*.so
%{_libdir}/libOGoContacts*.so
%{_libdir}/libOGoDocuments*.so
%{_libdir}/libOGoJobs*.so
%{_libdir}/libOGoProject*.so
%{_libdir}/libOGoRawDatabase*.so
%{_libdir}/libOGoScheduler*.so

%files logic
%defattr(-,root,root,-)
%{_libdir}/opengroupware.org-%{version}/commands/LSAccount.cmd
%{_libdir}/opengroupware.org-%{version}/commands/LSAddress.cmd
%{_libdir}/opengroupware.org-%{version}/commands/LSBase.cmd
%{_libdir}/opengroupware.org-%{version}/commands/LSDocuments.cmd
%{_libdir}/opengroupware.org-%{version}/commands/LSEnterprise.cmd
%{_libdir}/opengroupware.org-%{version}/commands/LSMail.cmd
%{_libdir}/opengroupware.org-%{version}/commands/LSNews.cmd
%{_libdir}/opengroupware.org-%{version}/commands/LSPerson.cmd
%{_libdir}/opengroupware.org-%{version}/commands/LSProject.cmd
%{_libdir}/opengroupware.org-%{version}/commands/LSScheduler.cmd
%{_libdir}/opengroupware.org-%{version}/commands/LSSearch.cmd
%{_libdir}/opengroupware.org-%{version}/commands/LSTasks.cmd
%{_libdir}/opengroupware.org-%{version}/commands/LSTeam.cmd
%{_libdir}/opengroupware.org-%{version}/commands/OGo.model
%{_libdir}/libLSAddress*.so.%{libversion}*
%{_libdir}/libLSFoundation*.so.%{libversion}*
%{_libdir}/libLSSearch*.so.%{libversion}*
%{_libdir}/libOGoSchedulerTools*.so.%{libversion}*

%files logic-tools
%defattr(-,root,root,-)
%{_bindir}/load-LSModel

%files logic-devel
%defattr(-,root,root,-)
%{_includedir}/LSFoundation
%{_includedir}/OGoSchedulerTools
%{_libdir}/libLSAddress*.so
%{_libdir}/libLSFoundation*.so
%{_libdir}/libLSSearch*.so
%{_libdir}/libOGoSchedulerTools*.so

#%files pda
#%defattr(-,root,root,-)
#%{_sbindir}/ogo-nhsd-%{version}
#%{_bindir}/ogo-ppls-%{version}
#%{_libdir}/libOGoNHS*.so.%{libversion}*
#%{_libdir}/libOGoPalmUI_d.so.%{libversion}*
#%{_libdir}/libOGoPalm_d.so.%{libversion}*
#%{_libdir}/libPPSync*.so.%{libversion}*
#%{_libdir}/opengroupware.org-%{version}/conduits/OpenGroupwareNHS.conduit/ix86/linux-gnu/gnu-fd-nil/OpenGroupwareNHS
#%{_libdir}/opengroupware.org-%{version}/conduits/OpenGroupwareNHS.conduit/Resources/Info-gnustep.plist
#%{_libdir}/opengroupware.org-%{version}/conduits/OpenGroupwareNHS.conduit/bundle-info.plist
#%{_libdir}/opengroupware.org-%{version}/conduits/OpenGroupwareNHS.conduit/stamp.make
#%{_libdir}/opengroupware.org-%{version}/datasources/OGoPalmDS.ds/ix86/linux-gnu/gnu-fd-nil/OGoPalmDS
#%{_libdir}/opengroupware.org-%{version}/datasources/OGoPalmDS.ds/Resources/Info-gnustep.plist
#%{_libdir}/opengroupware.org-%{version}/datasources/OGoPalmDS.ds/bundle-info.plist
#%{_libdir}/opengroupware.org-%{version}/datasources/OGoPalmDS.ds/stamp.make
#%{_libdir}/opengroupware.org-%{version}/webui/OGoPalm.lso
#%{_datadir}/opengroupware.org-%{version}/initscript_templates/ogo-nhsd.init
#%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/%{NHSD_SYSCONF}
#%ghost %attr(0755,root,root) %config %{_sysconfdir}/rc.d/init.d/%{NHSD_INIT_NAME}

#%files pda-devel
#%defattr(-,root,root,-)
#%{_includedir}/OGoNHS
#%{_includedir}/OGoPalm
#%{_includedir}/OGoPalmUI
#%{_includedir}/PPSync
#%{_libdir}/libOGoNHS*.so
#%{_libdir}/libOGoPalmUI_d.so
#%{_libdir}/libOGoPalm_d.so
#%{_libdir}/libPPSync*.so

%files theme-default
%defattr(-,root,root,-)
%{_datadir}/opengroupware.org-%{version}/www/Danish.lproj
%{_datadir}/opengroupware.org-%{version}/www/English.lproj
%{_datadir}/opengroupware.org-%{version}/www/German.lproj
%{_datadir}/opengroupware.org-%{version}/www/Italian.lproj
%{_datadir}/opengroupware.org-%{version}/www/Polish.lproj
%{_datadir}/opengroupware.org-%{version}/www/Spanish.lproj
%{_datadir}/opengroupware.org-%{version}/www/WOStats.xsl
%{_datadir}/opengroupware.org-%{version}/www/menu.js

%files theme-ooo
%defattr(-,root,root,-)
%{_datadir}/opengroupware.org-%{version}/templates/Themes/OOo
%{_datadir}/opengroupware.org-%{version}/www/English_OOo.lproj
%{_datadir}/opengroupware.org-%{version}/www/German_OOo.lproj

%files theme-blue
%defattr(-,root,root,-)
%{_datadir}/opengroupware.org-%{version}/templates/Themes/blue
%{_datadir}/opengroupware.org-%{version}/www/English_blue.lproj
%{_datadir}/opengroupware.org-%{version}/www/German_blue.lproj

%files theme-kde
%defattr(-,root,root,-)
%{_datadir}/opengroupware.org-%{version}/templates/Themes/kde
%{_datadir}/opengroupware.org-%{version}/www/English_kde.lproj

%files theme-orange
%defattr(-,root,root,-)
%{_datadir}/opengroupware.org-%{version}/templates/Themes/orange
%{_datadir}/opengroupware.org-%{version}/www/English_orange.lproj
%{_datadir}/opengroupware.org-%{version}/www/German_orange.lproj

%files tools
%defattr(-,root,root,-)
/etc/ld.so.conf.d/ogo.conf
%{_bindir}/ogo-account-add
%{_bindir}/ogo-account-del
%{_bindir}/ogo-account-list
%{_bindir}/ogo-acl-list
%{_bindir}/ogo-check-aptconflicts
%{_bindir}/ogo-check-permission
%{_bindir}/ogo-defaults
%{_bindir}/ogo-instfilter-procmail
%{_bindir}/ogo-jobs-export
%{_bindir}/ogo-project-export
%{_bindir}/ogo-project-import
%{_bindir}/ogo-project-list
%{_bindir}/ogo-runcmd
%{_bindir}/ogo-vcard-get
%{_bindir}/ogo-vcard-put
%{_bindir}/sky_install_sieve
%{_bindir}/sky_send_bulk_messages
%{_bindir}/skyaptnotify
%{_datadir}/opengroupware.org-%{version}/aptnotify_template/ogo-aptnotify.sh

%files webui-app
%defattr(-,root,root,-)
%{_sbindir}/ogo-webui-%{version}
%{_datadir}/opengroupware.org-%{version}/templates/ogo-webui-%{version}
%{_datadir}/opengroupware.org-%{version}/initscript_templates/ogo-webui.init
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/%{OGO_SYSCONF}
%ghost %attr(0755,root,root) %config %{_sysconfdir}/rc.d/init.d/%{OGO_INIT_NAME}

%files webui-core
%defattr(-,root,root,-)
%{_libdir}/libOGoFoundation*.so.%{libversion}*
%{_libdir}/opengroupware.org-%{version}/webui/AdminUI.lso
%{_libdir}/opengroupware.org-%{version}/webui/BaseUI.lso
%{_libdir}/opengroupware.org-%{version}/webui/OGoUIElements.lso
%{_libdir}/opengroupware.org-%{version}/webui/PreferencesUI.lso
%{_libdir}/opengroupware.org-%{version}/webui/PropertiesUI.lso
%{_libdir}/opengroupware.org-%{version}/webui/RelatedLinksUI.lso
%{_libdir}/opengroupware.org-%{version}/webui/SoOGo.lso
%{_datadir}/opengroupware.org-%{version}/templates/AdminUI
%{_datadir}/opengroupware.org-%{version}/templates/BaseUI
%{_datadir}/opengroupware.org-%{version}/templates/OGoUIElements
%{_datadir}/opengroupware.org-%{version}/templates/PreferencesUI
%{_datadir}/opengroupware.org-%{version}/templates/PropertiesUI
%{_datadir}/opengroupware.org-%{version}/templates/RelatedLinksUI

%files webui-core-devel
%defattr(-,root,root,-)
%{_includedir}/OGoFoundation
%{_libdir}/libOGoFoundation*.so

%files webui-calendar
%defattr(-,root,root,-)
%{_libdir}/opengroupware.org-%{version}/webui/LSWScheduler.lso
%{_libdir}/opengroupware.org-%{version}/webui/OGoResourceScheduler.lso
%{_libdir}/opengroupware.org-%{version}/webui/OGoScheduler.lso
%{_libdir}/opengroupware.org-%{version}/webui/OGoSchedulerDock.lso
%{_libdir}/opengroupware.org-%{version}/webui/OGoSchedulerViews.lso
%{_datadir}/opengroupware.org-%{version}/templates/LSWScheduler
%{_datadir}/opengroupware.org-%{version}/templates/OGoResourceScheduler
%{_datadir}/opengroupware.org-%{version}/templates/OGoScheduler
%{_datadir}/opengroupware.org-%{version}/templates/OGoSchedulerDock
%{_datadir}/opengroupware.org-%{version}/templates/OGoSchedulerViews

%{_datadir}/opengroupware.org-%{version}/Holidays.plist

%files webui-contact
%defattr(-,root,root,-)
%{_libdir}/opengroupware.org-%{version}/webui/AddressUI.lso
%{_libdir}/opengroupware.org-%{version}/webui/EnterprisesUI.lso
%{_libdir}/opengroupware.org-%{version}/webui/LDAPAccounts.lso
%{_libdir}/opengroupware.org-%{version}/webui/PersonsUI.lso
%{_datadir}/opengroupware.org-%{version}/templates/AddressUI
%{_datadir}/opengroupware.org-%{version}/templates/EnterprisesUI
%{_datadir}/opengroupware.org-%{version}/templates/LDAPAccounts
%{_datadir}/opengroupware.org-%{version}/templates/PersonsUI

%files webui-mailer
%defattr(-,root,root,-)
%{_libdir}/libOGoWebMail*.so.%{libversion}*
%{_libdir}/opengroupware.org-%{version}/webui/LSWMail.lso
%{_libdir}/opengroupware.org-%{version}/webui/OGoMailEditor.lso
%{_libdir}/opengroupware.org-%{version}/webui/OGoMailFilter.lso
%{_libdir}/opengroupware.org-%{version}/webui/OGoMailInfo.lso
%{_libdir}/opengroupware.org-%{version}/webui/OGoMailViewers.lso
%{_libdir}/opengroupware.org-%{version}/webui/OGoRecipientLists.lso
%{_libdir}/opengroupware.org-%{version}/webui/OGoWebMail.lso
%{_datadir}/opengroupware.org-%{version}/templates/LSWMail
%{_datadir}/opengroupware.org-%{version}/templates/OGoMailEditor
%{_datadir}/opengroupware.org-%{version}/templates/OGoMailFilter
%{_datadir}/opengroupware.org-%{version}/templates/OGoMailInfo
%{_datadir}/opengroupware.org-%{version}/templates/OGoMailViewers
%{_datadir}/opengroupware.org-%{version}/templates/OGoRecipientLists
%{_datadir}/opengroupware.org-%{version}/templates/OGoWebMail

%files webui-mailer-devel
%defattr(-,root,root,-)
%{_includedir}/OGoWebMail
%{_libdir}/libOGoWebMail*.so

%files webui-news
%defattr(-,root,root,-)
%{_libdir}/opengroupware.org-%{version}/webui/NewsUI.lso
%{_datadir}/opengroupware.org-%{version}/templates/NewsUI

%files webui-task
%defattr(-,root,root,-)
%{_libdir}/opengroupware.org-%{version}/webui/JobUI.lso
%{_datadir}/opengroupware.org-%{version}/templates/JobUI

%files webui-project
%defattr(-,root,root,-)
%{_libdir}/opengroupware.org-%{version}/webui/LSWProject.lso
%{_libdir}/opengroupware.org-%{version}/webui/OGoDocInlineViewers.lso
%{_libdir}/opengroupware.org-%{version}/webui/OGoNote.lso
%{_libdir}/opengroupware.org-%{version}/webui/OGoProject.lso
%{_libdir}/opengroupware.org-%{version}/webui/OGoProjectInfo.lso
%{_libdir}/opengroupware.org-%{version}/webui/OGoProjectZip.lso
%{_datadir}/opengroupware.org-%{version}/templates/LSWProject
%{_datadir}/opengroupware.org-%{version}/templates/OGoDocInlineViewers
%{_datadir}/opengroupware.org-%{version}/templates/OGoNote
%{_datadir}/opengroupware.org-%{version}/templates/OGoProject
%{_datadir}/opengroupware.org-%{version}/templates/OGoProjectInfo
%{_datadir}/opengroupware.org-%{version}/templates/OGoProjectZip

%files webui-resource-basque
%defattr(-,root,root,-)
%{_datadir}/opengroupware.org-%{version}/translations/Basque.lproj

%files webui-resource-dk
%defattr(-,root,root,-)
%{_datadir}/opengroupware.org-%{version}/translations/Danish.lproj

%files webui-resource-nl
%defattr(-,root,root,-)
%{_datadir}/opengroupware.org-%{version}/translations/Dutch.lproj

%files webui-resource-en
%defattr(-,root,root,-)
%{_datadir}/opengroupware.org-%{version}/translations/English.lproj

%files webui-resource-fr
%defattr(-,root,root,-)
%{_datadir}/opengroupware.org-%{version}/translations/French.lproj

%files webui-resource-de
%defattr(-,root,root,-)
%{_datadir}/opengroupware.org-%{version}/translations/German.lproj

%files webui-resource-hu
%defattr(-,root,root,-)
%{_datadir}/opengroupware.org-%{version}/translations/Hungarian.lproj

%files webui-resource-it
%defattr(-,root,root,-)
%{_datadir}/opengroupware.org-%{version}/translations/Italian.lproj

%files webui-resource-jp
%defattr(-,root,root,-)
%{_datadir}/opengroupware.org-%{version}/translations/Japanese.lproj

%files webui-resource-no
%defattr(-,root,root,-)
%{_datadir}/opengroupware.org-%{version}/translations/Norwegian.lproj

%files webui-resource-pl
%defattr(-,root,root,-)
%{_datadir}/opengroupware.org-%{version}/translations/Polish.lproj

%files webui-resource-pt
%defattr(-,root,root,-)
%{_datadir}/opengroupware.org-%{version}/translations/Portuguese.lproj

%files webui-resource-sk
%defattr(-,root,root,-)
%{_datadir}/opengroupware.org-%{version}/translations/Slovak.lproj

%files webui-resource-es
%defattr(-,root,root,-)
%{_datadir}/opengroupware.org-%{version}/translations/Spanish.lproj

%files webui-resource-ptbr
%defattr(-,root,root,-)
%{_datadir}/opengroupware.org-%{version}/translations/ptBR.lproj

%files xmlrpcd
%defattr(-,root,root,-)
%{_sbindir}/ogo-xmlrpcd-%{version}
%{_datadir}/opengroupware.org-%{version}/initscript_templates/ogo-xmlrpcd.init
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/%{XMLRPCD_SYSCONF}
%ghost %attr(0755,root,root) %{_sysconfdir}/rc.d/init.d/%{XMLRPCD_INIT_NAME}

%files zidestore
%defattr(-,root,root,-)
%{_sbindir}/ogo-zidestore-%{zide_v}
%{_libdir}/libZSAppointments*.so.%{zide_v}*
%{_libdir}/libZSBackend*.so.%{zide_v}*
%{_libdir}/libZSContacts*.so.%{zide_v}*
%{_libdir}/libZSFrontend*.so.%{zide_v}*
%{_libdir}/libZSProjects*.so.%{zide_v}*
%{_libdir}/libZSTasks*.so.%{zide_v}*
%{_libdir}/zidestore-%{zide_v}
%{_datadir}/zidestore-%{zide_v}
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/%{ZIDESTORE_SYSCONF}
%ghost %attr(0755,root,root) %{_sysconfdir}/rc.d/init.d/%{ZIDESTORE_INIT_NAME}

%files zidestore-devel
%defattr(-,root,root,-)
%{_includedir}/ZSBackend
%{_includedir}/ZSFrontend
%{_libdir}/libZSAppointments*.so
%{_libdir}/libZSBackend*.so
%{_libdir}/libZSContacts*.so
%{_libdir}/libZSFrontend*.so
%{_libdir}/libZSProjects*.so
%{_libdir}/libZSTasks*.so
