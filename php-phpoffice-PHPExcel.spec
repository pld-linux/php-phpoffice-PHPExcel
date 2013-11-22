# TODO
# - drop PHPExcel/Calculation/Functions.php - php compat functions (find minimum required and use that in .spec)
# - mbstring used unconditionally in some places: ./PHPExcel/Writer/CSV.php, ./PHPExcel/Calculation.php
%define		pkgname	PHPExcel
%define		php_min_version 5.2.1
%include	/usr/lib/rpm/macros.php
Summary:	PHPExcel - OpenXML - Create Excel2007 documents in PHP - Spreadsheet engine
Name:		php-phpoffice-%{pkgname}
Version:	1.7.9
Release:	2
License:	LGPL v2.1
Group:		Development/Languages/PHP
Source0:	https://github.com/PHPOffice/PHPExcel/archive/%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	3a08fd80a8d77c79c72b2ce6f1d4440c
URL:		http://phpexcel.codeplex.com/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php(core) >= %{php_min_version}
Requires:	php(ctype)
Requires:	php(date)
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php(xml)
Suggests:	php(gd)
Suggests:	php(iconv)
Suggests:	php(simplexml)
Suggests:	php(sqlite)
Suggests:	php(xmlreader)
Suggests:	php(zip)
Suggests:	php-jpgraph
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_pear jpgraph_line.php

# exclude optional php dependencies
%define		_noautophp	php-gd php-iconv php-mbstring php-simplexml php-sqlite php-xmlreader

# put it together for rpmbuild
%define		_noautoreq	%{?_noautophp}

%description
PHPExcel - OpenXML - Read, Write and Create Excel documents in PHP -
Spreadsheet engine

Project providing a set of classes for the PHP programming language,
which allow you to write to and read from different spreadsheet file
formats, like Excel (BIFF) .xls, Excel 2007 (OfficeOpenXML) .xlsx,
CSV, Libre/OpenOffice Calc .ods, Gnumeric, PDF, HTML, ... This project
is built around Microsoft's OpenXML standard and PHP. Checkout the
Features this class set provides, such as setting spreadsheet meta
data (author, title, description, ...), multiple worksheets, different
fonts and font styles, cell borders, fills, gradients, adding images
to your spreadsheet, calculating formulas, converting between file
types and much, much more!

%package examples
Summary:	Examples for %{pkgname}
Group:		Documentation

%description examples
Documentation for %{name}.

%description examples -l pl.UTF-8
Dokumentacja do %{name}.

%prep
%setup -q -n %{pkgname}-%{version}
%undos -f php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_data_dir},%{_examplesdir}/%{name}-%{version}}
cp -a Classes/* $RPM_BUILD_ROOT%{php_data_dir}
cp -a Examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.txt changelog.txt
%{php_data_dir}/PHPExcel.php
%dir %{php_data_dir}/PHPExcel
%{php_data_dir}/PHPExcel/*.php
%{php_data_dir}/PHPExcel/CachedObjectStorage
%{php_data_dir}/PHPExcel/CalcEngine
%{php_data_dir}/PHPExcel/Calculation
%{php_data_dir}/PHPExcel/Cell
%{php_data_dir}/PHPExcel/Chart
%{php_data_dir}/PHPExcel/Reader
%{php_data_dir}/PHPExcel/RichText
%{php_data_dir}/PHPExcel/Shared
%{php_data_dir}/PHPExcel/Style
%{php_data_dir}/PHPExcel/Worksheet
%{php_data_dir}/PHPExcel/Writer

%dir %{php_data_dir}/PHPExcel/locale
%lang(cs) %{php_data_dir}/PHPExcel/locale/cs
%lang(da) %{php_data_dir}/PHPExcel/locale/da
%lang(de) %{php_data_dir}/PHPExcel/locale/de
%lang(en_GB) %dir %{php_data_dir}/PHPExcel/locale/en
%lang(en_GB) %{php_data_dir}/PHPExcel/locale/en/uk
%lang(es) %{php_data_dir}/PHPExcel/locale/es
%lang(fi) %{php_data_dir}/PHPExcel/locale/fi
%lang(fr) %{php_data_dir}/PHPExcel/locale/fr
%lang(hu) %{php_data_dir}/PHPExcel/locale/hu
%lang(it) %{php_data_dir}/PHPExcel/locale/it
%lang(nb) %{php_data_dir}/PHPExcel/locale/no
%lang(nl) %{php_data_dir}/PHPExcel/locale/nl
%lang(pl) %{php_data_dir}/PHPExcel/locale/pl
%lang(pt_BR) %dir %{php_data_dir}/PHPExcel/locale/pt
%lang(pt_BR) %{php_data_dir}/PHPExcel/locale/pt/br
%lang(pt) %{php_data_dir}/PHPExcel/locale/pt/config
%lang(pt) %{php_data_dir}/PHPExcel/locale/pt/functions
%lang(ru) %{php_data_dir}/PHPExcel/locale/ru
%lang(sv) %{php_data_dir}/PHPExcel/locale/sv
%lang(tr) %{php_data_dir}/PHPExcel/locale/tr

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
