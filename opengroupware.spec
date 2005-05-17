# TODO: spec filename vs Name
%define		ogo_makeflags	-s
%define		zid_ver		1.3
%define		xmlrpcd_ver	1.0a
%define		datatrunk	200505120002

Summary:	OpenGroupware
Summary(pl):	OpenGroupware
Name:		opengroupware.org
Version:	r995 
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://download.opengroupware.org/sources/trunk/%{name}-trunk-%{version}-%{datatrunk}.tar.gz
# Source0-md5:	a8b322de9b040ac9c0e671d19b4d3975
URL:		http://www.opengroupware.org/
BuildRequires:	apache-devel >= 2.0.40
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glibc-devel
BuildRequires:	gnustep-make-devel
#BuildRequires:  opengroupware.org-pilot-link-devel
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	pilot-link-devel
BuildRequires:	postgresql-devel
BuildRequires:	openldap-devel
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
webui mailer devel package.

%package webui-news
Summary:	webui news
Group:		Libraries

%description webui-news
webui news package.

%package webui-task
Summary:	webui task
Group:		Libraries

%description webui-task
webui task package.

%package webui-project
Summary:	webui project
Group:		Libraries

%description webui-project
webui project package.

%package webui-resource-dk
Summary:	webui resource dk
Group:		Libraries

%description webui-resource-dk
webui resource dk package.

%package webui-resource-nl
Summary:	webui resource nl
Group:		Libraries

%description webui-resource-nl
webui resource nl package.

%package webui-resource-en
Summary:	webui resource en
Group:		Libraries

%description webui-resource-en
webui resource en package.

%package webui-resource-fr
Summary:	webui resource fr
Group:		Libraries

%description webui-resource-fr
webui resource fr package.

%package webui-resource-de
Summary:	webui resource de
Group:		Libraries

%description webui-resource-de
webui resource de package.

%package webui-resource-hu
Summary:	webui resource hu
Group:		Libraries

%description webui-resource-hu
webui resource hu package.

%package webui-resource-it
Summary:	webui resource it
Group:		Libraries

%description webui-resource-it
webui resource it package.

%package webui-resource-jp
Summary:	webui resource jp
Group:		Libraries

%description webui-resource-jp
webui resource jp package.

%package webui-resource-nb
Summary:	webui resource nb
Group:		Libraries

%description webui-resource-nb
webui resource nb package.

%package webui-resource-pl
Summary:	webui resource pl
Group:		Libraries

%description webui-resource-pl
webui resource pl package.

%package webui-resource-pt
Summary:	webui resource pt
Group:		Libraries

%description webui-resource-pt
webui resource pt package.

%package webui-resource-es
Summary:	webui resource es
Group:		Libraries

%description webui-resource-es
webui resource es package.

%package webui-resource-se
Summary:	webui resource se
Group:		Libraries

%description webui-resource-se
webui resource se package.

%package webui-resource-ptbr
Summary:	webui resource ptbr
Group:		Libraries

%description webui-resource-ptbr
webui resource ptbr package.

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

. %{_libdir}/GNUstep/System/Library/Makefiles/GNUstep.sh
%configure
%{__make} %{ogo_makeflags}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/GNUstep

. %{_libdir}/GNUstep/System/Library/Makefiles/GNUstep.sh

%{__make} %{ogo_makeflags} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_libdir}/GNUstep/System \
	FHS_INSTALL_ROOT=$RPM_BUILD_ROOT%{_prefix} \
	BUNDLE_INSTALL_DIR=$RPM_BUILD_ROOT%{_prefix} \
	WOBUNDLE_INSTALL_DIR=$RPM_BUILD_ROOT%{_prefix}

cp -Rp WebUI/Templates "$RPM_BUILD_ROOT%{_datadir}/opengroupware.org-%{version}/templates"
cp -Rp WebUI/Resources "$RPM_BUILD_ROOT%{_datadir}/opengroupware.org-%{version}/translations"
cp -Rp Themes/WebServerResources "$RPM_BUILD_ROOT%{_datadir}/opengroupware.org-%{version}/www"
rm -fr "$RPM_BUILD_ROOT%{_datadir}/opengroupware.org-%{version}/templates/HelpUI"
rm -fr "$RPM_BUILD_ROOT%{_datadir}/opengroupware.org-%{version}/translations/COPYRIGHT"
rm -fr "$RPM_BUILD_ROOT%{_datadir}/opengroupware.org-%{version}/translations/ChangeLog"
rm -fr "$RPM_BUILD_ROOT%{_datadir}/opengroupware.org-%{version}/translations/GNUmakefile"
rm -fr "$RPM_BUILD_ROOT%{_datadir}/opengroupware.org-%{version}/www/GNUmakefile"
rm -fr "$RPM_BUILD_ROOT%{_datadir}/opengroupware.org-%{version}/www/tools"

%clean
rm -rf $RPM_BUILD_ROOT

%files docapi
%defattr(644,root,root,755)
%{_libdir}/opengroupware.org-%{version}/datasources/OGoAccounts.ds
%{_libdir}/opengroupware.org-%{version}/datasources/OGoBase.ds
%{_libdir}/opengroupware.org-%{version}/datasources/OGoContacts.ds
%{_libdir}/opengroupware.org-%{version}/datasources/OGoJobs.ds
%{_libdir}/opengroupware.org-%{version}/datasources/OGoProject.ds
%{_libdir}/opengroupware.org-%{version}/datasources/OGoRawDatabase.ds
%{_libdir}/opengroupware.org-%{version}/datasources/OGoScheduler.ds
%{_libdir}/libOGoAccounts*.so.5.1*
%{_libdir}/libOGoBase*.so.5.1*
%{_libdir}/libOGoContacts*.so.5.1*
%{_libdir}/libOGoDocuments*.so.5.1*
%{_libdir}/libOGoJobs*.so.5.1*
%{_libdir}/libOGoProject*.so.5.1*
%{_libdir}/libOGoRawDatabase*.so.5.1*
%{_libdir}/libOGoScheduler*.so.5.1*

%files docapi-fs-project
%defattr(644,root,root,755)
%{_libdir}/opengroupware.org-%{version}/datasources/OGoFileSystemProject.ds
%{_libdir}/libOGoFileSystemProject*.so.5.1*

%files docapi-fs-project-devel
%defattr(644,root,root,755)
%{_includedir}/OGoFileSystemProject
%{_libdir}/libOGoFileSystemProject*.so

%files docapi-db-project
%defattr(644,root,root,755)
%{_libdir}/opengroupware.org-%{version}/datasources/OGoDatabaseProject.ds
%{_libdir}/libOGoDatabaseProject*.so.5.1*

%files docapi-db-project-devel
%defattr(644,root,root,755)
%{_includedir}/OGoDatabaseProject
%{_libdir}/libOGoDatabaseProject*.so

%files docapi-devel
%defattr(644,root,root,755)
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
%defattr(644,root,root,755)
%{_libdir}/opengroupware.org-%{version}/commands/LSAccount.cmd
%{_libdir}/opengroupware.org-%{version}/commands/LSAddress.cmd
%{_libdir}/opengroupware.org-%{version}/commands/LSBase.cmd
%{_libdir}/opengroupware.org-%{version}/commands/LSDocuments.cmd
%{_libdir}/opengroupware.org-%{version}/commands/LSEnterprise.cmd
%{_libdir}/opengroupware.org-%{version}/commands/LSMail.cmd
%{_libdir}/opengroupware.org-%{version}/commands/LSNews.cmd
%{_libdir}/opengroupware.org-%{version}/commands/LSPerson.cmd
%{_libdir}/opengroupware.org-%{version}/commands/LSProject.cmd
%{_libdir}/opengroupware.org-%{version}/commands/LSResource.cmd
%{_libdir}/opengroupware.org-%{version}/commands/LSScheduler.cmd
%{_libdir}/opengroupware.org-%{version}/commands/LSSearch.cmd
%{_libdir}/opengroupware.org-%{version}/commands/LSTasks.cmd
%{_libdir}/opengroupware.org-%{version}/commands/LSTeam.cmd
%{_libdir}/opengroupware.org-%{version}/commands/OGo.model
%{_libdir}/libLSAddress*.so.5.1*
%{_libdir}/libLSFoundation*.so.5.1*
%{_libdir}/libLSSearch*.so.5.1*
%{_libdir}/libOGoSchedulerTools*.so.5.1*

%files logic-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/load-LSModel

%files logic-devel
%defattr(644,root,root,755)
%{_includedir}/LSFoundation
%{_includedir}/OGoSchedulerTools
%{_libdir}/libLSAddress*.so
%{_libdir}/libLSFoundation*.so
%{_libdir}/libLSSearch*.so
%{_libdir}/libOGoSchedulerTools*.so

%files pda
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/ogo-nhsd-%{version}
%attr(755,root,root) %{_bindir}/ogo-ppls-%{version}
%{_libdir}/libOGoNHS*.so.5.1*
%{_libdir}/%{ogo_libogopalmui}.so.5.1*
%{_libdir}/%{ogo_libogopalm}.so.5.1*
%{_libdir}/libPPSync*.so.5.1*
%{_libdir}/opengroupware.org-%{version}/conduits/OpenGroupwareNHS.conduit/OpenGroupwareNHS
%{_libdir}/opengroupware.org-%{version}/conduits/OpenGroupwareNHS.conduit/Resources/Info-gnustep.plist
%{_libdir}/opengroupware.org-%{version}/conduits/OpenGroupwareNHS.conduit/bundle-info.plist
%{_libdir}/opengroupware.org-%{version}/conduits/OpenGroupwareNHS.conduit/stamp.make
%{_libdir}/opengroupware.org-%{version}/datasources/OGoPalmDS.ds/OGoPalmDS
%{_libdir}/opengroupware.org-%{version}/datasources/OGoPalmDS.ds/Resources/Info-gnustep.plist
%{_libdir}/opengroupware.org-%{version}/datasources/OGoPalmDS.ds/bundle-info.plist
%{_libdir}/opengroupware.org-%{version}/datasources/OGoPalmDS.ds/stamp.make
%{_libdir}/opengroupware.org-%{version}/webui/OGoPalm.lso

%files pda-devel
%defattr(644,root,root,755)
%{_includedir}/OGoNHS
%{_includedir}/OGoPalm
%{_includedir}/OGoPalmUI
%{_includedir}/PPSync
%{_libdir}/libOGoNHS*.so
%{_libdir}/%{ogo_libogopalmui}.so
%{_libdir}/%{ogo_libogopalm}.so
%{_libdir}/libPPSync*.so

%files theme-default
%defattr(644,root,root,755)
%{_datadir}/opengroupware.org-%{version}/www/Danish.lproj
%{_datadir}/opengroupware.org-%{version}/www/English.lproj
%{_datadir}/opengroupware.org-%{version}/www/German.lproj
%{_datadir}/opengroupware.org-%{version}/www/Italian.lproj
%{_datadir}/opengroupware.org-%{version}/www/Polish.lproj
%{_datadir}/opengroupware.org-%{version}/www/Spanish.lproj
%{_datadir}/opengroupware.org-%{version}/www/WOStats.xsl
%{_datadir}/opengroupware.org-%{version}/www/menu.js

%files theme-ooo
%defattr(644,root,root,755)
%{_datadir}/opengroupware.org-%{version}/templates/Themes/OOo
%{_datadir}/opengroupware.org-%{version}/www/English_OOo.lproj
%{_datadir}/opengroupware.org-%{version}/www/German_OOo.lproj

%files theme-blue
%defattr(644,root,root,755)
%{_datadir}/opengroupware.org-%{version}/templates/Themes/blue
%{_datadir}/opengroupware.org-%{version}/www/English_blue.lproj
%{_datadir}/opengroupware.org-%{version}/www/German_blue.lproj

%files theme-kde
%defattr(644,root,root,755)
%{_datadir}/opengroupware.org-%{version}/templates/Themes/kde
%{_datadir}/opengroupware.org-%{version}/www/English_kde.lproj

%files theme-orange
%defattr(644,root,root,755)
%{_datadir}/opengroupware.org-%{version}/templates/Themes/orange
%{_datadir}/opengroupware.org-%{version}/www/English_orange.lproj
%{_datadir}/opengroupware.org-%{version}/www/German_orange.lproj

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sky_add_account
%attr(755,root,root) %{_bindir}/sky_del_account
%attr(755,root,root) %{_bindir}/sky_get_login_names
%attr(755,root,root) %{_bindir}/sky_install_procmail
%attr(755,root,root) %{_bindir}/sky_install_sieve
%attr(755,root,root) %{_bindir}/sky_send_bulk_messages
%attr(755,root,root) %{_bindir}/skyaptnotify
%attr(755,root,root) %{_bindir}/skycheckperm
%attr(755,root,root) %{_bindir}/skydefaults
%attr(755,root,root) %{_bindir}/skyjobs2ical
%attr(755,root,root) %{_bindir}/skylistacls
%attr(755,root,root) %{_bindir}/skylistprojects
%attr(755,root,root) %{_bindir}/skyprojectexporter
%attr(755,root,root) %{_bindir}/skyprojectimporter
%attr(755,root,root) %{_bindir}/skyruncmd

%files webui-app
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/ogo-webui-%{version}
%{_libdir}/opengroupware.org-%{version}/webui
%{_datadir}/opengroupware.org-%{version}/templates

%files webui-core
%defattr(644,root,root,755)
%{_libdir}/libOGoFoundation*.so.5.1*
%{_libdir}/opengroupware.org-%{version}/webui/AdminUI.lso
%{_libdir}/opengroupware.org-%{version}/webui/BaseUI.lso
%{_libdir}/opengroupware.org-%{version}/webui/OGoUIElements.lso
%{_libdir}/opengroupware.org-%{version}/webui/PreferencesUI.lso
%{_libdir}/opengroupware.org-%{version}/webui/PropertiesUI.lso
%{_libdir}/opengroupware.org-%{version}/webui/RelatedLinksUI.lso
%{_datadir}/opengroupware.org-%{version}/templates/AdminUI
%{_datadir}/opengroupware.org-%{version}/templates/BaseUI
%{_datadir}/opengroupware.org-%{version}/templates/OGoUIElements
%{_datadir}/opengroupware.org-%{version}/templates/PreferencesUI
%{_datadir}/opengroupware.org-%{version}/templates/PropertiesUI
%{_datadir}/opengroupware.org-%{version}/templates/RelatedLinksUI

%files webui-core-devel
%defattr(644,root,root,755)
%{_includedir}/OGoFoundation
%{_libdir}/libOGoFoundation*.so

%files webui-calendar
%defattr(644,root,root,755)
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
%defattr(644,root,root,755)
%{_libdir}/opengroupware.org-%{version}/webui/AddressUI.lso
%{_libdir}/opengroupware.org-%{version}/webui/EnterprisesUI.lso
%{_libdir}/opengroupware.org-%{version}/webui/LDAPAccounts.lso
%{_libdir}/opengroupware.org-%{version}/webui/PersonsUI.lso
%{_datadir}/opengroupware.org-%{version}/templates/AddressUI
%{_datadir}/opengroupware.org-%{version}/templates/EnterprisesUI
%{_datadir}/opengroupware.org-%{version}/templates/LDAPAccounts
%{_datadir}/opengroupware.org-%{version}/templates/PersonsUI

%files webui-mailer
%defattr(644,root,root,755)
%{_libdir}/libOGoWebMail*.so.5.1*
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
%defattr(644,root,root,755)
%{_includedir}/OGoWebMail
%{_libdir}/libOGoWebMail*.so

%files webui-news
%defattr(644,root,root,755)
%{_libdir}/opengroupware.org-%{version}/webui/NewsUI.lso
%{_datadir}/opengroupware.org-%{version}/templates/NewsUI

%files webui-task
%defattr(644,root,root,755)
%{_libdir}/opengroupware.org-%{version}/webui/JobUI.lso
%{_datadir}/opengroupware.org-%{version}/templates/JobUI

%files webui-project
%defattr(644,root,root,755)
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

%files webui-resource-dk
%defattr(644,root,root,755)
%{_datadir}/opengroupware.org-%{version}/translations/Danish.lproj

%files webui-resource-nl
%defattr(644,root,root,755)
%{_datadir}/opengroupware.org-%{version}/translations/Dutch.lproj

%files webui-resource-en
%defattr(644,root,root,755)
%{_datadir}/opengroupware.org-%{version}/translations/English.lproj

%files webui-resource-fr
%defattr(644,root,root,755)
%{_datadir}/opengroupware.org-%{version}/translations/French.lproj

%files webui-resource-de
%defattr(644,root,root,755)
%{_datadir}/opengroupware.org-%{version}/translations/German.lproj

%files webui-resource-hu
%defattr(644,root,root,755)
%{_datadir}/opengroupware.org-%{version}/translations/Hungarian.lproj

%files webui-resource-it
%defattr(644,root,root,755)
%{_datadir}/opengroupware.org-%{version}/translations/Italian.lproj

%files webui-resource-jp
%defattr(644,root,root,755)
%{_datadir}/opengroupware.org-%{version}/translations/Japanese.lproj

#%files webui-resource-no
#%defattr(644,root,root,755)
#%{_datadir}/opengroupware.org-%{version}/translations/Norwegian.lproj

%files webui-resource-pl
%defattr(644,root,root,755)
%{_datadir}/opengroupware.org-%{version}/translations/Polish.lproj

%files webui-resource-pt
%defattr(644,root,root,755)
%{_datadir}/opengroupware.org-%{version}/translations/Portuguese.lproj

%files webui-resource-es
%defattr(644,root,root,755)
%{_datadir}/opengroupware.org-%{version}/translations/Spanish.lproj

%files webui-resource-se
%defattr(644,root,root,755)
%{_datadir}/opengroupware.org-%{version}/translations/Swedish.lproj

%files webui-resource-ptbr
%defattr(644,root,root,755)
%{_datadir}/opengroupware.org-%{version}/translations/ptBR.lproj

%files xmlrpcd
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/ogo-xmlrpcd-%{xmlrpcd_ver}

%files zidestore
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/ogo-zidestore-%{zid_ver}
%{_libdir}/libZSAppointments*.so.%{zid_ver}*
%{_libdir}/libZSBackend*.so.%{zid_ver}*
%{_libdir}/libZSContacts*.so.%{zid_ver}*
%{_libdir}/libZSFrontend*.so.%{zid_ver}*
%{_libdir}/libZSProjects*.so.%{zid_ver}*
%{_libdir}/libZSTasks*.so.%{zid_ver}*
%{_libdir}/zidestore-%{zid_ver}/Appointments.zsp
%{_libdir}/zidestore-%{zid_ver}/Contacts.zsp
%{_libdir}/zidestore-%{zid_ver}/EvoConnect.zsp
%{_libdir}/zidestore-%{zid_ver}/PrefsUI.zsp
%{_libdir}/zidestore-%{zid_ver}/Projects.zsp
%{_libdir}/zidestore-%{zid_ver}/RSS.zsp
%{_libdir}/zidestore-%{zid_ver}/Tasks.zsp
%{_libdir}/zidestore-%{zid_ver}/WCAP.zsp
%{_libdir}/zidestore-%{zid_ver}/ZSCommon.zsp
%{_datadir}/zidestore-%{zid_ver}

%files zidestore-devel
%defattr(644,root,root,755)
%{_includedir}/ZSBackend
%{_includedir}/ZSFrontend
%{_libdir}/libZSAppointments*.so
%{_libdir}/libZSBackend*.so
%{_libdir}/libZSContacts*.so
%{_libdir}/libZSFrontend*.so
%{_libdir}/libZSProjects*.so
%{_libdir}/libZSTasks*.so
