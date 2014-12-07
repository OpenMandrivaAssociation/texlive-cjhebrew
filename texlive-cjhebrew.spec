# revision 15878
# category Package
# catalog-ctan /language/hebrew/cjhebrew
# catalog-date 2007-01-01 00:37:00 +0100
# catalog-license lppl
# catalog-version 0.1a
Name:		texlive-cjhebrew
Version:	0.1a
Release:	9
Summary:	Typeset Hebrew with LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/hebrew/cjhebrew
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cjhebrew.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cjhebrew.doc.tar.xz
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
%{_texmfdistdir}/fonts/afm/public/cjhebrew/cjheblsm.afm
%{_texmfdistdir}/fonts/afm/public/cjhebrew/cjhebltx.afm
%{_texmfdistdir}/fonts/enc/dvips/cjhebrew/cjhebltx.enc
%{_texmfdistdir}/fonts/map/dvips/cjhebrew/cjhebrew.map
%{_texmfdistdir}/fonts/tfm/public/cjhebrew/cjhblsm.tfm
%{_texmfdistdir}/fonts/tfm/public/cjhebrew/cjhbltx.tfm
%{_texmfdistdir}/fonts/tfm/public/cjhebrew/cjheblsm.tfm
%{_texmfdistdir}/fonts/tfm/public/cjhebrew/cjhebltx.tfm
%{_texmfdistdir}/fonts/tfm/public/cjhebrew/rcjhblsm.tfm
%{_texmfdistdir}/fonts/tfm/public/cjhebrew/rcjhbltx.tfm
%{_texmfdistdir}/fonts/type1/public/cjhebrew/cjheblsm.pfb
%{_texmfdistdir}/fonts/type1/public/cjhebrew/cjhebltx.pfb
%{_texmfdistdir}/fonts/vf/public/cjhebrew/cjhblsm.vf
%{_texmfdistdir}/fonts/vf/public/cjhebrew/cjhbltx.vf
%{_texmfdistdir}/tex/latex/cjhebrew/cjhebrew.sty
%doc %{_texmfdistdir}/doc/fonts/cjhebrew/cjhebtst.tex
%doc %{_texmfdistdir}/doc/fonts/cjhebrew/manual.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1a-2
+ Revision: 750247
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1a-1
+ Revision: 718063
- texlive-cjhebrew
- texlive-cjhebrew
- texlive-cjhebrew
- texlive-cjhebrew
- texlive-cjhebrew

