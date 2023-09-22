# This Puppet manifest ensures create a file in /tmp 

file { '/tmp/school':
    ensure  => 'file',
    mode    => 'o744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet'
}