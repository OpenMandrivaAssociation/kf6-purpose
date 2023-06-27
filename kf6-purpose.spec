%define libname %mklibname KF6Purpose
%define devname %mklibname KF6Purpose -d
%define git 20230627

Name: kf6-purpose
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/purpose/-/archive/master/purpose-master.tar.bz2#/purpose-%{git}.tar.bz2
Summary: Framework for providing abstractions to get the developer's purposes fulfilled
URL: https://invent.kde.org/frameworks/purpose
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6KIO)
Requires: %{libname} = %{EVRD}

%description
Framework for providing abstractions to get the developer's purposes fulfilled

%package -n %{libname}
Summary: Framework for providing abstractions to get the developer's purposes fulfilled
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Framework for providing abstractions to get the developer's purposes fulfilled

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Framework for providing abstractions to get the developer's purposes fulfilled

%prep
%autosetup -p1 -n purpose-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/purpose.*
%{_datadir}/icons/hicolor/*/apps/phabricator-purpose.*
%{_datadir}/icons/hicolor/*/apps/reviewboard-purpose.*
%{_datadir}/kf6/purpose

%files -n %{devname}
%{_includedir}/KF6/Purpose
%{_libdir}/cmake/KF6Purpose
%{_includedir}/KF6/PurposeWidgets

%files -n %{libname}
%{_libdir}/libKF6Purpose.so*
%{_libdir}/libKF6PurposeWidgets.so*
%{_libdir}/libPhabricatorHelpers.so*
%{_libdir}/libReviewboardHelpers.so*
%{_libdir}/libexec/kf6/purposeprocess
%{_qtdir}/plugins/kf6/kfileitemaction/*
%{_qtdir}/plugins/kf6/purpose
%{_qtdir}/qml/org/kde/purpose
