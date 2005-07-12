#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Model-CDBI-Plain
Summary:	Catalyst::Model::CDBI::Plain - A Plain base class for Class::DBI models
#Summary(pl):	
Name:		perl-Catalyst-Model-CDBI-Plain
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/J/JE/JESTER/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ec3e400333db09cf7536c40233743783
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Catalyst >= 4.00
BuildRequires:	perl-Class-DBI
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Catalyst::Model::CDBI::Plain is a Model class for Catalyst to be used
with user-specified Class::DBI classes. It does not automatically set
anything up or create relationships; this is left to the user. This
module can be used with existing Class::DBI classes, so that they can
be used with Catalyst, or as a way of writing CDBI-based Model classes
within Catalyst.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Catalyst/Model/*
%{_mandir}/man3/*
