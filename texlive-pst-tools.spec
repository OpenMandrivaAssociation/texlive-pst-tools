Name:		texlive-pst-tools
Epoch:		1
Version:	0.09b
Release:	2
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
%{_texmfdistdir}/dvips/pst-tools
%{_texmfdistdir}/tex/generic/pst-tools
%{_texmfdistdir}/tex/latex/pst-tools
%doc %{_texmfdistdir}/doc/generic/pst-tools

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
