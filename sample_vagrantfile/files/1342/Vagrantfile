# -*- mode: ruby -*-
# vi: set ft=ruby :
VAGRANTFILE_API_VERSION = "2"



# Load settings and config from local yaml file.
if File.exists?("local.config.yaml")
  settings = YAML.load_file 'local.config.yaml'
else
  settings = Hash.new
end
target = settings['target'] || 'virtualbox'
aws_access_key = settings['aws_access_key'] || 'CHANGEME'
aws_secret_key = settings['aws_secret_key'] || 'CHANGEME'

puts "Target:              " + target
puts "AWS access key:              " + aws_access_key
puts "AWS secret key:              " + aws_secret_key



# Use config-#{target}.yml for basic VM configuration.
require 'yaml'
dir = File.dirname(File.expand_path(__FILE__))
if !File.exist?("#{dir}/config-#{target}.yml")
  raise 'Configuration file not found! Please copy example.config.yml to config.yml and try again.'
end
vconfig = YAML::load_file("#{dir}/config-#{target}.yml")



# Load specific vagrant.
Vagrant.require_version '>= 1.6.0'
dir = File.dirname(File.expand_path(__FILE__))
eval File.read("#{dir}/vagrant/Vagrantfile-#{target}")
