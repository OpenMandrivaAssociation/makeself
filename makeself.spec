Summary:	Generates a self-extractable archive from a directory


Name:		makeself
Version:	2.1.5
Release:	16
License:	GPLv3
Group: 		Archiving/Compression
Url:		http://www.megastep.org/makeself/
Source0:	http://www.megastep.org/makeself/%{name}-%{version}.tar.bz2
Source1:	http://angst.cynapses.org/stripmakeself
BuildArch:	noarch
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
%setup -q
cp -p %{SOURCE1} .

%build

%install
mkdir -p %{buildroot}%{_bindir} \
	%{buildroot}%{_mandir}/man1 \
	%{buildroot}%{_datadir}/makeself/
install -m 755 makeself.sh %{buildroot}%{_bindir}/makeself
install -m 755 makeself-header.sh %{buildroot}%{_datadir}/makeself/makeself-header
install -m 755 stripmakeself %{buildroot}%{_bindir}/
install -m 644 makeself.1 %{buildroot}%{_mandir}/man1/

%files
%doc COPYING README TODO makeself.lsm
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/makeself/*


