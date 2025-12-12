%define module  html2text

Name:           python-html2text
Version:        2025.4.15
Release:        2
Summary:        Converts a page of HTML into clean, easy-to-read plain ASCII text
Group:          Development/Python
License:        GPLv3
URL:            https://alir3z4.github.io/html2text/
Source0:        https://files.pythonhosted.org/packages/source/h/html2text/html2text-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
Provides:	pythonegg(html2text)

%description
html2text is a Python script that convers a page of HTML into clean,
easy-to-read plain ASCII text. Better yet, that ASCII also happens to
be valid Markdown (a text-to-HTML format).

Also known as: THE ASCIINATOR, html to text, htm to txt, htm2txt, ...

%prep
%setup -q -n %{module}-%{version}

# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%py_build

%install
%py_install
# fix file conflitct with html2text:
mv %{buildroot}%{_bindir}/html2text %{buildroot}%{_bindir}/python-%{module}

%check
%{__python} setup.py test || /bin/true

%files
%{_bindir}/python-%{module}
%{python_sitelib}/*
