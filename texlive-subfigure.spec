Name:		texlive-subfigure
Version:	15878
Release:	2
Summary:	Deprecated: Figures divided into subfigures
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/obsolete/macros/latex/contrib/subfigure
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subfigure.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subfigure.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subfigure.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides support for the manipulation and reference of small or
'sub' figures and tables within a single figure or table
environment. It is convenient to use this package when your
subfigures are to be separately captioned, referenced, or are
to be included in the List-of-Figures. A new \subfigure command
is introduced which can be used inside a figure environment for
each subfigure. An optional first argument is used as the
caption for that subfigure. This package is now obsolescent:
new users should use subfig instead.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/subfigure/subfigure.cfg
%{_texmfdistdir}/tex/latex/subfigure/subfigure.sty
%doc %{_texmfdistdir}/doc/latex/subfigure/README
%doc %{_texmfdistdir}/doc/latex/subfigure/ltxdoc.cfg
%doc %{_texmfdistdir}/doc/latex/subfigure/subfigure.pdf
%doc %{_texmfdistdir}/doc/latex/subfigure/test.tex
%doc %{_texmfdistdir}/doc/latex/subfigure/test2.tex
%doc %{_texmfdistdir}/doc/latex/subfigure/test3.tex
%doc %{_texmfdistdir}/doc/latex/subfigure/test4.tex
%doc %{_texmfdistdir}/doc/latex/subfigure/test5.tex
#- source
%doc %{_texmfdistdir}/source/latex/subfigure/Makefile
%doc %{_texmfdistdir}/source/latex/subfigure/subfigure.dtx
%doc %{_texmfdistdir}/source/latex/subfigure/subfigure.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
