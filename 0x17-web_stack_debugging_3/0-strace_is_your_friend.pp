# Using strace, find out why Apache is returning a 500 error.
# Your 0-strace_is_your_friend.pp file must contain Puppet code
# You can use whatever Puppet resource type you want for you fix

exec { 'fix the typing error':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => '/usr/local/bin/:/bin/'
}
