# revision 32002
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-tools
# catalog-date 2013-10-26 16:53:57 +0200
# catalog-license lppl
# catalog-version 0.04
Name:		texlive-pst-tools
Epoch:		1
Version:	0.04
Release:	5
Summary:	PStricks support functions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-tools
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-tools.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-tools.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides helper functions for other PSTricks
related packages.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-tools/pst-tools.pro
%{_texmfdistdir}/tex/generic/pst-tools/pst-tools.tex
%{_texmfdistdir}/tex/latex/pst-tools/pst-tools.sty
%doc %{_texmfdistdir}/doc/generic/pst-tools/Changes
%doc %{_texmfdistdir}/doc/generic/pst-tools/README
%doc %{_texmfdistdir}/doc/generic/pst-tools/pst-tools-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-tools/pst-tools-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-tools/pst-tools-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
