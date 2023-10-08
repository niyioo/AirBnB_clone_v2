# Define a class for the web_static setup
class web_static {
  # Ensure that Nginx is installed and started
  package { 'nginx':
    ensure  => 'installed',
  }

  service { 'nginx':
    ensure  => 'running',
    enable  => true,
  }

  # Create directories for web_static
  file { '/data':
    ensure  => 'directory',
  }

  file { '/data/web_static':
    ensure  => 'directory',
  }

  file { '/data/web_static/releases':
    ensure  => 'directory',
  }

  file { '/data/web_static/shared':
    ensure  => 'directory',
  }

  file { '/data/web_static/releases/test':
    ensure  => 'directory',
  }

  # Create an index.html file with content
  file { '/data/web_static/releases/test/index.html':
    ensure  => 'file',
    content => "This is a test\n",
  }

  # Symlink current to test
  file { '/data/web_static/current':
    ensure  => 'link',
    target  => '/data/web_static/releases/test',
  }

  # Set owner and group
  exec { 'change_ownership':
    command => 'chown -R ubuntu:ubuntu /data/',
    path    => '/usr/bin',
    onlyif  => 'test "$(stat -c %U /data/web_static)" != "ubuntu"',
  }

  # Configure Nginx site
  file { '/etc/nginx/sites-available/default':
    ensure  => 'file',
    content => template('web_static/default.erb'),
    require => Service['nginx'],
    notify  => Service['nginx'],
  }
}

# Include the class to set up web_static
include web_static
