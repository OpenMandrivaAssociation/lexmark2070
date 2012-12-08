Summary:	Lexmark 2070 Printer B/W driver
Name:		lexmark2070
Version:	0.6
Release:	%mkrel 13
License:	GPL
Group:		System/Printing
URL:		http://www.kornblum.i-p.com/2070/Lexmark2070.old.html
Source0:	http://www.kornblum.i-p.com/2070/Lexmark2070.latest.tar.bz2
Patch0:		Lexmark2070-LDFLAGS.diff
Requires:	c2070
BuildRequires:	netpbm-devel
Conflicts:	printer-utils = 2007
Conflicts:	printer-filters = 2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This filter allows to print in B/W a Lexmark 2070 (windows GDI) printer.

%prep

%setup -q -c
%patch0 -p0

%build
make -f makefile CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 Lexmark2070 %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc README LICENSE
%attr(0755,root,root) %{_bindir}/*


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6-12mdv2011.0
+ Revision: 666073
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6-11mdv2011.0
+ Revision: 606402
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6-10mdv2010.1
+ Revision: 519017
- rebuild

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.6-9mdv2010.0
+ Revision: 425507
- rebuild

* Thu Dec 25 2008 Oden Eriksson <oeriksson@mandriva.com> 0.6-8mdv2009.1
+ Revision: 318498
- use %%optflags and %%ldflags

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.6-7mdv2009.0
+ Revision: 222423
- rebuild

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 0.6-6mdv2008.1
+ Revision: 150443
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 0.6-5mdv2008.0
+ Revision: 75340
- fix deps (pixel)

* Tue Aug 28 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.6-4mdv2008.0
+ Revision: 72853
- Bumped.

  + Oden Eriksson <oeriksson@mandriva.com>
    - use the new System/Printing RPM GROUP

* Fri Aug 10 2007 Oden Eriksson <oeriksson@mandriva.com> 0.6-2mdv2008.0
+ Revision: 61084
- rebuild
- Import lexmark2070



* Thu Aug 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.6-1mdv2008.0
- initial Mandriva package

* Mon Mar 01 2004 Marcelo Ricardo Leitner <mrl@conectiva.com.br>
+ 2004-03-01 10:54:58 (50594)
- Adopted the real version as the real upstream version, 0.6.

* Thu Aug 29 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-08-29 18:08:36 (8365)
- Imported package from 8.0.
