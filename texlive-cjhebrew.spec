Name:		texlive-cjhebrew
Version:	43444
Release:	1
Summary:	Typeset Hebrew with LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/hebrew/cjhebrew
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cjhebrew.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cjhebrew.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The cjhebrew package provides Adobe Type 1 fonts for Hebrew,
and LaTeX macros to support their use. Hebrew text can be
vocalised, and a few accents are also available. The package
makes it easy to include Hebrew text in other-language
documents. The package makes use of the e-TeX extensions to
TeX, so should be run using an "e-LaTeX".

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/cjhebrew
%{_texmfdistdir}/fonts/enc/dvips/cjhebrew
%{_texmfdistdir}/fonts/map/dvips/cjhebrew
%{_texmfdistdir}/fonts/tfm/public/cjhebrew
%{_texmfdistdir}/fonts/type1/public/cjhebrew
%{_texmfdistdir}/fonts/vf/public/cjhebrew
%{_texmfdistdir}/tex/latex/cjhebrew
%doc %{_texmfdistdir}/doc/latex/cjhebrew

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
