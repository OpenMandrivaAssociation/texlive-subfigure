%global tl_name subfigure
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1.5
Release:	%{tl_revision}.1
Summary:	Deprecated: Figures divided into subfigures
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/obsolete/macros/latex/contrib/subfigure
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/subfigure.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/subfigure.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/subfigure.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides support for the manipulation and reference of small or 'sub'
figures and tables within a single figure or table environment. It is
convenient to use this package when your subfigures are to be separately
captioned, referenced, or are to be included in the List-of-Figures. A
new \subfigure command is introduced which can be used inside a figure
environment for each subfigure. An optional first argument is used as
the caption for that subfigure. The package is now considered obsolete:
it was superseded by subfig, but users may find the more recent
subcaption package more satisfactory.

