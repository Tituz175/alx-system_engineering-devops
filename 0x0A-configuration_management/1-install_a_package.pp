# Using Puppet, install flask from pip3.
# Requirements:
#    Install flask
#    Version must be 2.1.0

package { 'python3-pip':
    ensure => 'installed',
}

package { 'Flask':
    ensure   => '2.1.0',
    provider => 'pip',
    require  => Package['python3-pip']
}
