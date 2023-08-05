#!/usr/bin/env ruby

log_message = ARGV[0]

sender = log_message[/from:(.*?)\]/, 1]
receiver = log_message[/to:(.*?)\]/, 1]
flags = log_message[/flags:(.*?)\]/, 1]

puts "#{sender},#{receiver},#{flags}"