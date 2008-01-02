Summary:	Generates a self-extractable archive from a directory
Name:		makeself
Version:	2.1.4
Release:	%mkrel 2
Source0:	http://www.megastep.org/makeself/%{name}-%{version}.tar.bz2
Source1:	http://angst.cynapses.org/stripmakeself
Patch0:		makeself-2.1.4-deb.patch
Patch1:		stripmakeself-bin_sh.patch
License:	GPL
Group: 		Archiving/Compression
Url:		http://www.megastep.org/makeself/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	bzip2
Requires:	coreutils
Requires:	gnupg

%description
Makeself is a small shell script that generates a self-extractable
tar.gz archive from a directory. The resulting file appears as a shell
script (many of those have a .run suffix), and can be launched as
is. The archive will then uncompress itself to a temporary directory
and an optional arbitrary command will be executed (for example an
installation script). This is pretty similar to archives generated
with WinZip Self-Extractor in the Windows world. Makeself archives
also include checksums for integrity self-validation (CRC and/or MD5
checksums).

The makeself.sh script itself is used only to create the archives from
a directory of files. The resultant archive is actually a compressed
(using gzip, bzip2, or compress) TAR archive, with a small shell
script stub at the beginning. This small stub performs all the steps
of extracting the files, running the embedded command, and removing
the temporary files when it's all over. All what the user has to do to
install the software contained in such an archive is to "run" the
archive, i.e sh nice-software.run. I recommend using the "run" (which
was introduced by some Makeself archives released by Loki Software) or
"sh" suffix for such archives not to confuse the users, since they
know it's actually shell scripts (with quite a lot of binary data
attached to it though!).


%prep
%setup
cp -p %{SOURCE1} .
%patch0 -p1 -b .deb
%patch1 -p1 -b .binsh

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT%{_mandir}/man1 \
	$RPM_BUILD_ROOT%{_datadir}/makeself/
install -m 755 makeself.sh $RPM_BUILD_ROOT%{_bindir}/makeself
install -m 755 makeself-header.sh $RPM_BUILD_ROOT%{_datadir}/makeself/makeself-header
install -m 755 stripmakeself $RPM_BUILD_ROOT%{_bindir}/
install -m 644 makeself.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING README TODO update-readme makeself.lsm
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/makeself/*

