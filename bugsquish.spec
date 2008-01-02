%define	name	bugsquish
%define	version	0.0.6
%define release	%mkrel 10
%define	Summary	Kill bugs with mouse

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	ftp://ftp.sonic.net/pub/users/nbs/unix/x/bugsquish/%{name}-%{version}.tar.bz2
Source5:	%{name}-16.png
Source6:	%{name}-32.png
Source7:	%{name}-48.png
Patch0:		bugsquish-0.0.2-fix-CFLAGS.patch.bz2
License:	GPL
Url:		http://newbreedsoftware.com/bugsquish/
Group:		Games/Arcade
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	X11-devel SDL_image-devel SDL_mixer-devel alsa-lib-devel esound-devel

%description
Bugs are trying to suck blood out of your arm! Squish them with with your fly
swatter before you run out of blood.

%prep
%setup -q
%patch0 -p1
chmod a+r -R .
rm -rf `find -name .xvpics`

%build
%make CFLAGS="%{optflags}" DATA_PREFIX=%{_gamesdatadir}/%{name}/

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name} $RPM_BUILD_ROOT%{_gamesbindir}/%{name}
install -d $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}
cp -a data/* $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Bugsquish
Comment=%{summary}
Exec=%_gamesbindir/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

install -D -m644 %SOURCE6 $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -D -m644 %SOURCE5 $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -D -m644 %SOURCE7 $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS.txt CHANGES.txt README.txt
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_datadir}/applications/*
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

