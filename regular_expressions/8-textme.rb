#!/usr/bin/env ruby

log = ARGV[0]

# Use capture groups that stop at the closing bracket
matches = log.scan(/\[from:([^\]]+)\] \[to:([^\]]+)\] \[flags:([^\]]+)\]/)

# Output if matches were found
matches.each do |from, to, flags|
  puts "#{from},#{to},#{flags}"
end
