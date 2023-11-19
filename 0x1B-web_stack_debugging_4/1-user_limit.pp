# Solving the limit file at holberton user.

# Increasing the hard limit for 'holberton' users from 5 to 10000 
exec { 'fix_limit_hbton_user':
  command => 'sed -i "/holberton hard/s/5/10000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increasing the soft limit for 'holberton' users from 4 to 20000 
exec { 'increase_soft_file':
  command => 'sed -i "/holberton soft/s/4/20000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
