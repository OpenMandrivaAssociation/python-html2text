Name:           python-html2text
Version:        3.200.3
Release:        1
Summary:        Converts a page of HTML into clean, easy-to-read plain ASCII text
Group:          Development/Python
License:        GPLv3
URL:            http://www.aaronsw.com/2002/html2text/
Source0:        https://github.com/aaronsw/html2text/raw/master/html2text.py
BuildArch:      noarch
BuildRequires:  python
Provides:	pythonegg(html2text)

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
mkdir -p %{buildroot}/%{py_puresitedir}/
install -p -m 0644 html2text.py %{buildroot}/%{py_puresitedir}/

%clean

%files
%{py_puresitedir}/*
