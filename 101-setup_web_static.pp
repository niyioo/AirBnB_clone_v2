# Update the package repository
exec { 'apt_update':
  command => 'apt-get update',
  path    => '/usr/bin',
  onlyif  => 'test -z "$(find /var/lib/apt/lists/ -maxdepth 0 -type f -name lock)"',
}

# Upgrade installed packages
package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt_update'],
}

# Create web_static directories and index.html
file { '/data/web_static/releases/test':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static/shared':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => "This is a test\n",
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
}

# Create a symbolic link
file { '/data/web_static/current':
  ensure  => link,
  target  => '/data/web_static/releases/test',
  owner   => 'root',
  group   => 'root',
  mode    => '0755',
}

# Modify the nginx configuration
file_line { 'hbnb_static_location':
  path   => '/etc/nginx/sites-available/default',
  line   => '        location /hbnb_static/ {',
  after  => '        location / {',
}

file_line { 'alias_setting':
  path   => '/etc/nginx/sites-available/default',
  line   => '                alias /data/web_static/current/;',
  after  => '        location /hbnb_static/ {',
}

# Start the nginx service
service { 'nginx':
  ensure     => 'running',
  enable     => true,
  require    => [File['/etc/nginx/sites-available/default'], File['/etc/nginx/sites-enabled/default']],
}
