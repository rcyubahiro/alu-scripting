#!/usr/bin/env ruby
# Capture and output the sender, receiver, and flags
puts ARGV[0].scan(/from:([^\s]+)/).join + ',' + 
     ARGV[0].scan(/to:([^\s]+)/).join + ',' + 
     ARGV[0].scan(/flags:([^\]]+)/).join
