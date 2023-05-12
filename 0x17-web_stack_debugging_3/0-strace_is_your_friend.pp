# Manage the file '/var/www/html/wp-settings.php'
file { '/var/www/html/wp-settings.php':
  ensure  => present,  # Ensure that the file exists
  content => inline_template('<%= File.read("/var/www/html/wp-settings.php").gsub(/\.phpp/, ".php") %>'),
  # The content of the file is dynamically generated using an inline Ruby template.
  # It reads the content of the existing file and replaces any occurrence of '.phpp' with '.php'.
}
