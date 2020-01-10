%define tarball xf86-video-geode
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir	%{moduledir}/drivers

Summary:   Xorg X11 AMD Geode video driver
Name:      xorg-x11-drv-geode
Version:   2.11.15
Release:   1%{?dist}
URL:       http://www.x.org/wiki/AMDGeodeDriver
Source0:   http://xorg.freedesktop.org/releases/individual/driver/xf86-video-geode-%{version}.tar.bz2
License:   MIT
Group:     User Interface/X Hardware Support

Patch1:    geode-2.11.14-ftbfs.patch

ExclusiveArch: %{ix86}

BuildRequires: pkgconfig
BuildRequires: xorg-x11-server-devel
BuildRequires: xorg-x11-proto-devel

Requires:  xorg-x11-server-Xorg >= 1.1.0

%description 
X.Org X11 AMD Geode video driver.

%prep
%setup -q -n %{tarball}-%{version}
%patch1 -p1

%build
%configure --disable-static --libdir=%{_libdir} --mandir=%{_mandir} \
	     --enable-visibility
make

%install
%makeinstall DESTDIR=$RPM_BUILD_ROOT

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

# Compat symlink for legacy driver name so existing xorg.conf's do not break
ln -s geode_drv.so $RPM_BUILD_ROOT%{_libdir}/xorg/modules/drivers/amd_drv.so

%files
%defattr(-,root,root,-)
%{driverdir}/amd_drv.so
%{driverdir}/geode_drv.so
%{driverdir}/ztv_drv.so

%changelog
* Sun Nov 24 2013 Peter Robinson <pbrobinson@fedoraproject.org> 2.11.15-1
- New upstream release

* Wed Nov 20 2013 Adam Jackson <ajax@redhat.com> - 2.11.14-11
- 1.15RC2 ABI rebuild

* Wed Nov 06 2013 Adam Jackson <ajax@redhat.com> - 2.11.14-10
- 1.15RC1 ABI rebuild

* Fri Oct 25 2013 Adam Jackson <ajax@redhat.com> 2.11.14-9
- Fix FTBFS against 1.15

* Fri Oct 25 2013 Adam Jackson <ajax@redhat.com> - 2.11.14-8
- ABI rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> - 2.11.14-6
- require xorg-x11-server-devel, not -sdk

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> - 2.11.14-5
- ABI rebuild

* Fri Feb 15 2013 Peter Hutterer <peter.hutterer@redhat.com> - 2.11.14-4
- ABI rebuild

* Fri Feb 15 2013 Peter Hutterer <peter.hutterer@redhat.com> - 2.11.14-3
- ABI rebuild

* Thu Jan 10 2013 Adam Jackson <ajax@redhat.com> - 2.11.14-2
- ABI rebuild

* Mon Nov 26 2012 Daniel Drake <dsd@laptop.org> 2.11.14-1
- New upstream release

* Tue Nov 20 2012 Daniel Drake <dsd@laptop.org> 2.11.13-5
- Fix GNOME notification area rendering bug

* Tue Oct 30 2012 Daniel Drake <dsd@laptop.org> 2.11.13-4
- Add solid picture acceleration to maintain glyph rendering performance
  and work around an X glyph rendering bug (freedesktop#55723).

* Mon Aug 06 2012 Dave Airlie <airlied@redhat.com> 2.11.13-3
- update from git to make build

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul  6 2012 Daniel Drake <dsd@laptop.org> - 2.11.13-1
- New version

* Wed Feb  8 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 2.11.12-4
- Rebuild for Xorg ABI version bump

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 17 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 2.11.12-3
- Rebuild for Xorg ABI version bump
- Drop ancient obsoletes and clean up spec

* Tue Sep 13 2011 Daniel Drake <dsd@laptop.org> - 2.11.12-2
- rebuild for Xorg ABI version 11

* Thu Mar 17 2011 Daniel Drake <dsd@laptop.org> - 2.11.12-1
- update to v2.11.12 (no changes over 2.11.11-4, but rebuild for new X ABI)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb  7 2011 Daniel Drake <dsd@laptop.org> - 2.11.11-4
- add upstream patch to compile with new kernel headers without v4l1

* Mon Feb  7 2011 Daniel Drake <dsd@laptop.org> - 2.11.11-3
- add upstream patch to fix Xv video corruption (fd.o #33004)

* Thu Jan 13 2011 Daniel Drake <dsd@laptop.org> - 2.11.11-2
- update to 2.11.11

* Sun Dec 12 2010 Daniel Drake <dsd@laptop.org> - 2.11.10-2
- fix compile on xorg-1.9.99

* Wed Dec  1 2010 Daniel Drake <dsd@laptop.org> - 2.11.10-1
- update to 2.11.10

* Wed Sep 01 2010 Bernie Innocenti <bernie@codewiz.org> 2.11.9-1
- update to 2.11.9

* Mon Jul 05 2010 Dave Airlie <airlied@redhat.com> 2.11.4.1-4
- update to geode git for latest server API

* Mon Jul 05 2010 Peter Hutterer <peter.hutterer@redhat.com> - 2.11.4.1-3
- rebuild for X Server 1.9

* Thu Jan 21 2010 Peter Hutterer <peter.hutterer@redhat.com> - 2.11.4.1-2
- Rebuild for server 1.8

* Thu Sep 10 2009 Dave Airlie <airlied@redhat.com> 2.11.4.1-1
- geode 2.11.4.1

* Wed Aug 05 2009 Dave Airlie <airlied@redhat.com> 2.11.3-1
- geode 2.11.3 
- add abi/api patches + autoreconf

* Tue Aug 04 2009 Adam Jackson <ajax@redhat.com> 2.11.2-4
- Fix for new DPMS headers

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.2-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 2.11.2-2.1
- ABI bump

* Tue Jun 23 2009 Dave Airlie <airlied@redhat.com> 2.11.2-2
- update for new server ABI

* Tue May 12 2009 Chris Ball <cjb@laptop.org> 2.11.2-1
- fix crasher bug due to EXA ABI change: RHBZ #500086

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Chris Ball <cjb@laptop.org> 2.11.1-1
- update to 2.11.1
- this build works on the OLPC XO with upstream/Rawhide kernels

* Mon Dec 22 2008 Dave Airlie <airlied@redhat.com> 2.11.0-2
- update for new server API

* Wed Dec 10 2008 Warren Togami <wtogami@redhat.com> - 2.11.0-1
- update to 2.11.0 adds xrandr-1.2 and fixes cursor issues

* Wed Aug 20 2008 Warren Togami <wtogami@redhat.com> - 2.10.1-1
- update to 2.10.1

* Fri Jun 13 2008 Dennis Gilmore <dennis@ausil.us> 2.10.0-1
- update to 2.10.0  drop upstreamed patches

* Tue May 20 2008 Dennis Gilmore <dennis@ausil.us> 2.9.0-2
- apply patches for olpc

* Thu May 08 2008 Dennis Gilmore <dennis@ausil.us> 2.9.0-1
- update to 2.9.0
- adds olpc support for everything but DPMS

* Thu Apr 17 2008 Warren Togami <wtogami@redhat.com> 2.8.0-3
- Use libddc instead of unreliable BIOS DDC queries.

* Wed Apr 02 2008 Warren Togami <wtogami@redhat.com> 2.8.0-2
- License: MIT

* Wed Apr 02 2008 Warren Togami <wtogami@redhat.com> 2.8.0-1
- 2.8.0 rename from amd to geode
  compat symlink to old name retains old xorg.conf compat
