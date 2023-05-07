#!/usr/bin/env ruby
#This is a Ruby script that accepts one argument pass it to a regular expression matching method
puts ARGV[0].scan(/hbt+n/).join
