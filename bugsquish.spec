%define	name	bugsquish
%define	version	0.0.6
%define release	%mkrel 15
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
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel

%description
Bugs are trying to suck blood out of your arm! Squish them with with your fly
swatter before you run out of blood.

%prep
%setup -q
%patch0 -p1
chmod a+r -R .
rm -rf `find -name .xvpics`

%build
%make CFLAGS="%{optflags} %ldflags" DATA_PREFIX=%{_gamesdatadir}/%{name}/

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

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

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



%changelog
* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 0.0.6-15mdv2011.0
+ Revision: 635010
- rebuild
- tighten BR

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.6-14mdv2011.0
+ Revision: 616903
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.0.6-13mdv2010.0
+ Revision: 424698
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.0.6-12mdv2009.0
+ Revision: 243372
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 10 2007 Funda Wang <fwang@mandriva.org> 0.0.6-10mdv2008.1
+ Revision: 116846
- drop old menu

  + Thierry Vignaud <tv@mandriva.org>
    - buildrequires X11-devel instead of XFree86-devel
    - import bugsquish


* Fri Jul  7 2006 Pixel <pixel@mandriva.com> 0.0.6-9mdv2007.0
- use mkrel
- switch to XDG menu

* Tue Oct 11 2005 Pixel <pixel@mandriva.com> 0.0.6-8mdk
- rebuild

* Tue Aug 31 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.0.6-7mdk
- rebuild for new menu
- cosmetics

* Fri Jun  4 2004 Pixel <pixel@mandrakesoft.com> 0.0.6-6mdk
- rebuild

* Wed Apr  2 2003 Pixel <pixel@mandrakesoft.com> 0.0.6-5mdk
- remove .xvpics

* Thu Nov 12 2002 Per Øyvind Karlsen <peroyvind@delonic.no> 0.0.6-4mdk
- Removed obsolete Prefix tag
- Removed redundant BuildRequires
- Cleanups
- Added menu item
- Added icons
- Moved stuff to the correct places
- Silent setup

* Thu Sep 05 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.0.6-3mdk
- rebuild

* Sun Jul 21 2002 Pixel <pixel@mandrakesoft.com> 0.0.6-2mdk
- recompile against new vorbis stuff

* Thu Jun 27 2002 Pixel <pixel@mandrakesoft.com> 0.0.6-1mdk
- new release

* Mon Apr 29 2002 Pixel <pixel@mandrakesoft.com> 0.0.4-2mdk
- rebuild for new libasound (alsa)

* Sat Feb  2 2002 Pixel <pixel@mandrakesoft.com> 0.0.4-1mdk
- new release

* Sat Jan 19 2002 Stefan van der Eijk <stefan@eijk.nu> 0.0.2-10mdk
- BuildRequires

* Thu Oct 11 2001 Pixel <pixel@mandrakesoft.com> 0.0.2-9mdk
- rebuilding for libpng3

* Wed Sep 13 2001 Stefan van der Eijk <stefan@eijk.nu> 0.0.2-8mdk
- BuildRequires: libSDL-devel

* Thu Sep  6 2001 Pixel <pixel@mandrakesoft.com> 0.0.2-7mdk
- fix rights

* Thu Sep  6 2001 Pixel <pixel@mandrakesoft.com> 0.0.2-6mdk
- rebuild

* Mon May 14 2001 Pixel <pixel@mandrakesoft.com> 0.0.2-5mdk
- rebuild with new SDL

* Tue Dec 19 2000 Pixel <pixel@mandrakesoft.com> 0.0.2-4mdk
- rebuild with new libSDL_mixer

* Wed Nov 29 2000 Pixel <pixel@mandrakesoft.com> 0.0.2-3mdk
- build req, rebuild

* Thu Nov  2 2000 Pixel <pixel@mandrakesoft.com> 0.0.2-2mdk
- rebuild with uptodate SDL
- fix summary-not-capitalized

* Thu Nov  2 2000 Pixel <pixel@mandrakesoft.com> 0.0.2-1mdk
- initial spec
