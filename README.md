# apache-conf

Created Jinja2 template for Apache configuration.

Created _vhosts.j2_ template, which will return a similar Apache config:
```bash
<VirtualHost *:80>
  ServerName www.domain.tld
  DocumentRoot /www/domain
  ServerAdmin www-admin@foo.example.com
  <Directory "/usr/local/httpd/htdocs">
     AllowOverride All
     Options Indexes FollowSymLinks
     Order allow,deny
     Allow from all
  </Directory>
</VirtualHost>
```
Automatization
