Name:           python-html2text
Version:        2.39
Release:        %mkrel 2
Summary:        Converts a page of HTML into clean, easy-to-read plain ASCII text
Group:          Development/Python
License:        GPLv3
URL:            http://www.aaronsw.com/2002/html2text/
Source0:        http://www.aaronsw.com/2002/html2text/html2text-%{version}.py
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:      noarch
BuildRequires:  python

%description
html2text is a Python script that convers a page of HTML into clean,
easy-to-read plain ASCII text. Better yet, that ASCII also happens to
be valid Markdown (a text-to-HTML format).

Also known as: THE ASCIINATOR, html to text, htm to txt, htm2txt, ...

%prep
%setup -q -c -T
install -p %{SOURCE0} ./html2text.py

%build
echo Nothing to build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{python_sitelib}/
install -p -m 0644 html2text.py %{buildroot}/%{python_sitelib}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python_sitelib}/*


%changelog
* Mon Nov 15 2010 Ahmad Samir <ahmadsamir@mandriva.org> 2.39-2mdv2011.0
+ Revision: 597746
- Resubmit, the last package has a wrong file list

* Sat Oct 30 2010 Ahmad Samir <ahmadsamir@mandriva.org> 2.39-1mdv2011.0
+ Revision: 590521
- update to 2.39

* Sun Feb 07 2010 Ahmad Samir <ahmadsamir@mandriva.org> 2.38-1mdv2010.1
+ Revision: 501852
- Fix spec
- Import python-html2text (based on Fedora .spec)


