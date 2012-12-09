# revision 25024
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-tools
# catalog-date 2012-01-04 09:11:42 +0100
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-pst-tools
Version:	0.1
Release:	1
Summary:	PStricks support functions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-tools
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-tools.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-tools.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-tools.source.tar.xz
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
%{_texmfdistdir}/tex/generic/pst-tools/pst-tools.tex
%{_texmfdistdir}/tex/latex/pst-tools/pst-tools.sty
%doc %{_texmfdistdir}/doc/generic/pst-tools/Changes
%doc %{_texmfdistdir}/doc/generic/pst-tools/README
%doc %{_texmfdistdir}/doc/generic/pst-tools/pst-tools-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-tools/pst-tools-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-tools/pst-tools-doc.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-tools/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 759031
- texlive-pst-tools
- texlive-pst-tools

