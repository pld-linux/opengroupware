# TODO: spec filename vs Name
# - make it build oustide GNUstep directory : /usr/lib/
# - make proper ./configure build
# - check %files section
# - translate all packages to pl
# - scavange as much as possible from the included spec in maitance
# - make proper rc-init scripts
# - scavange and adjust configure files check scripts
# - check spellings and typos
# - tweak BR and R to fit PLD
%define		nightlybuild	r1259
%define		ogo_makeflags	-s
%define		zid_ver		1.3
%define		xmlrpcd_ver	1.0a
%define		datatrunk	200509011104
%define		libogo_v	5.3
%define zide_v 1.5

Summary:	OpenGroupware
Summary(pl):	OpenGroupware
Name:		opengroupware.org
Version:	1.1
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	http://download.opengroupware.org/nightly/sources/trunk/%{name}-trunk-%{nightlybuild}-%{datatrunk}.tar.gz
# Source0-md5:	c141909fa83d0779f8e7931fbcb6bd3b
URL:		http://www.opengroupware.org/
BuildRequires:	apache-devel >= 2.0.40
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glibc-devel
BuildRequires:	gnustep-make-libFoundation-devel
#BuildRequires:  opengroupware.org-pilot-link-devel
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel >= 0.9.7
#BuildRequires:	pilot-link-devel
BuildRequires:	postgresql-devel
BuildRequires:	openldap-devel
BuildRequires:	sope-appserver-devel
BuildRequires:	sope-core-devel
BuildRequires:	sope-EOF-devel
BuildRequires:	sope-gdl1-devel
BuildRequires:	sope-ical-devel
BuildRequires:	sope-ldap-devel
BuildRequires:	sope-mime-devel
BuildRequires:	sope-xml-devel
BuildRequires:	gnustep-extensions-devel
#Requires:	pilot-link
Requires:	apache
#Requires:	glibc
Requires:	openssl >= 0.9.7
#Requires:	openldap
# local???
Requires:	postgresql
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#echo "LDPATH=/usr/lib/opengroupware.org/Libraries/ix86/linux-gnu/gnu-fd-nil/" >> /etc/env.d/50ogo

%description
OGo.

%description -l pl
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
Requires:	opengroupware.org-pilot-link
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
Summary:      News component of OpenGroupware.org's Web UI
Group:        Development/Libraries
#Requires:     sope%{smaj}%{smin}-appserver sope%{smaj}%{smin}-core sope%{smaj}%{smin}-gdl1 sope%{smaj}%{smin}-ldap sope%{smaj}%{smin}-mime sope%{smaj}%{smin}-xml ogo-docapi ogo-logic ogo-webui-app ogo-webui-core libfoundation%{lfmaj}%{lfmin} libobjc-lf2
AutoReqProv:  off

%description webui-news
The news component shows recent appointments and tasks for each user.
Additionally it supports the creation and display of simple news items.

%package webui-task
Summary:      Task component of OpenGroupware.org's Web UI
Group:        Development/Libraries
Requires:     ogo-webui-app ogo-webui-core
AutoReqProv:  off

%description webui-task
The task component enables users to assign and manage tasks
related to projects or standalone.

%package webui-project
Summary:      Project component of OpenGroupware.org's Web UI
Group:        Development/Libraries
Requires:     sope%{smaj}%{smin}-appserver sope%{smaj}%{smin}-core sope%{smaj}%{smin}-gdl1 sope%{smaj}%{smin}-ldap sope%{smaj}%{smin}-mime sope%{smaj}%{smin}-xml ogo-docapi ogo-logic ogo-webui-app ogo-webui-core libfoundation%{lfmaj}%{lfmin} libobjc-lf2
AutoReqProv:  off

%description webui-project
The project component adds project management capabilities to
OpenGroupware.org's web UI. It allows to assign and track a
project's status, add documents and links and interworks nicely
with the task component to assign specific tasks within a project.

%package webui-resource-basque
Summary:      Basque translation for OpenGroupware.org's web UI
Group:        Development/Libraries
Requires:     ogo-webui-app
AutoReqProv:  off

%description webui-resource-basque
This package contains the Basque translation for OpenGroupware.org's web UI.
##
%package webui-resource-dk
Summary:      Danish translation for OpenGroupware.org's web UI
Group:        Development/Libraries
Requires:     ogo-webui-app
AutoReqProv:  off

%description webui-resource-dk
This package contains the Danish translation for OpenGroupware.org's web UI.
##
%package webui-resource-nl
Summary:      Dutch translation for OpenGroupware.org's web UI
Group:        Development/Libraries
Requires:     ogo-webui-app
AutoReqProv:  off

%description webui-resource-nl
This package contains the Dutch translation for OpenGroupware.org's web UI.
##
%package webui-resource-en
Summary:      English translation for OpenGroupware.org's web UI
Group:        Development/Libraries
Requires:     ogo-webui-app
AutoReqProv:  off

%description webui-resource-en
This package contains the English translation for OpenGroupware.org's web UI.
##
%package webui-resource-fr
Summary:      French translation for OpenGroupware.org's web UI
Group:        Development/Libraries
Requires:     ogo-webui-app
AutoReqProv:  off

%description webui-resource-fr
This package contains the French translation for OpenGroupware.org's web UI.
##
%package webui-resource-de
Summary:      German translation for OpenGroupware.org's web UI
Group:        Development/Libraries
Requires:     ogo-webui-app
AutoReqProv:  off

%description webui-resource-de
This package contains the German translation for OpenGroupware.org's web UI.
##
%package webui-resource-hu
Summary:      Hungarian translation for OpenGroupware.org's web UI
Group:        Development/Libraries
Requires:     ogo-webui-app
AutoReqProv:  off

%description webui-resource-hu
This package contains the Hungarian translation for OpenGroupware.org's web UI.
##
%package webui-resource-it
Summary:      Italian translation for OpenGroupware.org's web UI
Group:        Development/Libraries
Requires:     ogo-webui-app
AutoReqProv:  off

%description webui-resource-it
This package contains the Italian translation for OpenGroupware.org's web UI.
##
%package webui-resource-jp
Summary:      Japanese translation for OpenGroupware.org's web UI
Group:        Development/Libraries
Requires:     ogo-webui-app
AutoReqProv:  off

%description webui-resource-jp
This package contains the Japanese translation for OpenGroupware.org's web UI.
##
%package webui-resource-no
Summary:      Norwegian translation for OpenGroupware.org's web UI
Group:        Development/Libraries
Requires:     ogo-webui-app
AutoReqProv:  off

%description webui-resource-no
This package contains the Norwegian translation for OpenGroupware.org's web UI.
##
%package webui-resource-pl
Summary:      Polish translation for OpenGroupware.org's web UI
Group:        Development/Libraries
Requires:     ogo-webui-app
AutoReqProv:  off

%description webui-resource-pl
This package contains the Polish translation for OpenGroupware.org's web UI.
##
%package webui-resource-pt
Summary:      Portuguese translation for OpenGroupware.org's web UI
Group:        Development/Libraries
Requires:     ogo-webui-app
AutoReqProv:  off

%description webui-resource-pt
This package contains the Portuguese translation for OpenGroupware.org's web UI.
##
%package webui-resource-es
Summary:      Spanish translation for OpenGroupware.org's web UI
Group:        Development/Libraries
Requires:     ogo-webui-app
AutoReqProv:  off

%description webui-resource-es
This package contains the Spanish translation for OpenGroupware.org's web UI.
##
%package webui-resource-sk
Summary:      Slovak translation for OpenGroupware.org's web UI
Group:        Development/Libraries
Requires:     ogo-webui-app
AutoReqProv:  off

%description webui-resource-sk
This package contains the Slovak translation for OpenGroupware.org's web UI.
##
%package webui-resource-ptbr
Summary:      Portuguese (Brazilian) translation for OpenGroupware.org's web UI
Group:        Development/Libraries
Requires:     ogo-webui-app
AutoReqProv:  off

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
%setup -q -n opengroupware.org

%build
set -x
. %{_libdir}/GNUstep-libFoundation/System/Library/Makefiles/GNUstep.sh
./configure
%{__make} %{ogo_makeflags}

%install
set -x
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/GNUstep

. %{_libdir}/GNUstep-libFoundation/System/Library/Makefiles/GNUstep.sh

%{__make} %{ogo_makeflags} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_libdir}/GNUstep-libFoundation/System \
	FHS_INSTALL_ROOT=$RPM_BUILD_ROOT%{_prefix} \
	BUNDLE_INSTALL_DIR=$RPM_BUILD_ROOT%{_prefix} \
	WOBUNDLE_INSTALL_DIR=$RPM_BUILD_ROOT%{_prefix}

SHAREDIR="${RPM_BUILD_ROOT}%{_prefix}/share/opengroupware.org-%{version}"
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

##prepare initscript templates
#INITSCRIPTS_TMP_DIR_OGO="${SHAREDIR}/initscript_templates"
#INITSCRIPTS_TMP_DIR_ZIDE="${RPM_BUILD_ROOT}%{_prefix}/share/zidestore-%{zide_v}/initscript_templates"
#mkdir -p ${INITSCRIPTS_TMP_DIR_OGO}
#mkdir -p ${INITSCRIPTS_TMP_DIR_ZIDE}
#cp %{_specdir}/initscript_templates/redhat_nhsd ${INITSCRIPTS_TMP_DIR_OGO}/
#cp %{_specdir}/initscript_templates/redhat_xmlrpcd ${INITSCRIPTS_TMP_DIR_OGO}/
#cp %{_specdir}/initscript_templates/redhat_opengroupware ${INITSCRIPTS_TMP_DIR_OGO}/
#cp %{_specdir}/initscript_templates/redhat_zidestore ${INITSCRIPTS_TMP_DIR_ZIDE}/
#cp %{_specdir}/initscript_templates/suse_nhsd ${INITSCRIPTS_TMP_DIR_OGO}/
#cp %{_specdir}/initscript_templates/suse_xmlrpcd ${INITSCRIPTS_TMP_DIR_OGO}/
#cp %{_specdir}/initscript_templates/suse_opengroupware ${INITSCRIPTS_TMP_DIR_OGO}/
#cp %{_specdir}/initscript_templates/suse_zidestore ${INITSCRIPTS_TMP_DIR_ZIDE}/

#ghost initscripts
#INITSCRIPT_DST="${RPM_BUILD_ROOT}%{_sysconfdir}/init.d"
#mkdir -p ${INITSCRIPT_DST}
#touch ${INITSCRIPT_DST}/ogo-nhsd
#touch ${INITSCRIPT_DST}/ogo-webui
#touch ${INITSCRIPT_DST}/ogo-xmlrpcd
#touch ${INITSCRIPT_DST}/ogo-zidestore

##template for ogo-aptnotify
#APTNOTIFY_TMP_DIR="${SHAREDIR}/aptnotify_template"
#mkdir -p ${APTNOTIFY_TMP_DIR}
#cp %{_specdir}/aptnotify_template/ogo-aptnotify.sh ${APTNOTIFY_TMP_DIR}/

%clean
rm -rf $RPM_BUILD_ROOT

%files docapi
%defattr(-,root,root,-)
%{_libdir}/opengroupware.org-%{version}/datasources/OGoAccounts.ds
%{_libdir}/opengroupware.org-%{version}/datasources/OGoBase.ds
%{_libdir}/opengroupware.org-%{version}/datasources/OGoContacts.ds
%{_libdir}/opengroupware.org-%{version}/datasources/OGoJobs.ds
%{_libdir}/opengroupware.org-%{version}/datasources/OGoProject.ds
%{_libdir}/opengroupware.org-%{version}/datasources/OGoRawDatabase.ds
%{_libdir}/opengroupware.org-%{version}/datasources/OGoScheduler.ds
%{_libdir}/libOGoAccounts*.so.%{libogo_v}*
%{_libdir}/libOGoBase*.so.%{libogo_v}*
%{_libdir}/libOGoContacts*.so.%{libogo_v}*
%{_libdir}/libOGoDocuments*.so.%{libogo_v}*
%{_libdir}/libOGoJobs*.so.%{libogo_v}*
%{_libdir}/libOGoProject*.so.%{libogo_v}*
%{_libdir}/libOGoRawDatabase*.so.%{libogo_v}*
%{_libdir}/libOGoScheduler*.so.%{libogo_v}*

%files docapi-fs-project
%defattr(-,root,root,-)
%{_libdir}/opengroupware.org-%{version}/datasources/OGoFileSystemProject.ds
%{_libdir}/libOGoFileSystemProject*.so.%{libogo_v}*

%files docapi-fs-project-devel
%defattr(-,root,root,-)
%{_includedir}/OGoFileSystemProject
%{_libdir}/libOGoFileSystemProject*.so

%files docapi-db-project
%defattr(-,root,root,-)
%{_libdir}/opengroupware.org-%{version}/datasources/OGoDatabaseProject.ds
%{_libdir}/libOGoDatabaseProject*.so.%{libogo_v}*

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
%{_libdir}/libLSAddress*.so.%{libogo_v}*
%{_libdir}/libLSFoundation*.so.%{libogo_v}*
%{_libdir}/libLSSearch*.so.%{libogo_v}*
%{_libdir}/libOGoSchedulerTools*.so.%{libogo_v}*

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
#%{_libdir}/libOGoNHS*.so.%{libogo_v}*
#%{_libdir}/%{ogo_libogopalmui}.so.%{libogo_v}*
#%{_libdir}/%{ogo_libogopalm}.so.%{libogo_v}*
#%{_libdir}/libPPSync*.so.%{libogo_v}*
#%{_libdir}/opengroupware.org-%{version}/conduits/OpenGroupwareNHS.conduit/OpenGroupwareNHS
#%{_libdir}/opengroupware.org-%{version}/conduits/OpenGroupwareNHS.conduit/Resources/Info-gnustep.plist
#%{_libdir}/opengroupware.org-%{version}/conduits/OpenGroupwareNHS.conduit/bundle-info.plist
#%{_libdir}/opengroupware.org-%{version}/conduits/OpenGroupwareNHS.conduit/stamp.make
#%{_libdir}/opengroupware.org-%{version}/datasources/OGoPalmDS.ds/OGoPalmDS
#%{_libdir}/opengroupware.org-%{version}/datasources/OGoPalmDS.ds/Resources/Info-gnustep.plist
#%{_libdir}/opengroupware.org-%{version}/datasources/OGoPalmDS.ds/bundle-info.plist
#%{_libdir}/opengroupware.org-%{version}/datasources/OGoPalmDS.ds/stamp.make
#%{_libdir}/opengroupware.org-%{version}/webui/OGoPalm.lso
#%{_datadir}/opengroupware.org-%{version}//*nhsd
#%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/ogo-nhsd
#%ghost %attr(0755,root,root) %config %{_sysconfdir}/init.d/ogo-nhsd

#%files pda-devel
#%defattr(-,root,root,-)
#%{_includedir}/OGoNHS
#%{_includedir}/OGoPalm
#%{_includedir}/OGoPalmUI
#%{_includedir}/PPSync
#%{_libdir}/libOGoNHS*.so
#%{_libdir}/%{ogo_libogopalmui}.so
#%{_libdir}/%{ogo_libogopalm}.so
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
#%{_datadir}/opengroupware.org-%{version}/aptnotify_template/ogo-aptnotify.sh

%files webui-app
%defattr(-,root,root,-)
%{_sbindir}/ogo-webui-%{version}
%{_datadir}/opengroupware.org-%{version}/templates/ogo-webui-%{version}
#%{_datadir}/opengroupware.org-%{version}/initscript_templates/*opengroupware
#%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/ogo-webui
#%ghost %attr(0755,root,root) %config %{_sysconfdir}/init.d/ogo-webui

%files webui-core
%defattr(-,root,root,-)
%{_libdir}/libOGoFoundation*.so.%{libogo_v}*
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
%{_libdir}/libOGoWebMail*.so.%{libogo_v}*
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
#%{_datadir}/opengroupware.org-%{version}/initscript_templates/*xmlrpcd
#%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/ogo-xmlrpcd
#%ghost %attr(0755,root,root) %{_sysconfdir}/init.d/ogo-xmlrpcd

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
#%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/ogo-zidestore
#%ghost %attr(0755,root,root) %{_sysconfdir}/init.d/ogo-zidestore

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
