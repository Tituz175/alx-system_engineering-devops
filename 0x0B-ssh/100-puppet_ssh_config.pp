# Puppet for configuration
file_line {'Name':
    path => '/etc/ssh/ssh_config',
    line => 'Host localhost
        HostName localhost
        PasswordAuthentication no
        IdentityFile ~/.ssh/school
        User ubuntu',
}
