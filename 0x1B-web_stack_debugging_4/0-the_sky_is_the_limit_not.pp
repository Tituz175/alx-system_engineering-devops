# Using puppet to fix error 500 in apache server 

exec { 'webstack_debug':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restarting the Nginx
exec { 'nginx-restart':
  require => Exec['webstack_debug'],
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
