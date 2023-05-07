#!/usr/bin/env ruby
#This is a Ruby script that accepts one argument and passes it to a regular expression
puts ARGV[0].scan(/hb?tn/).join
