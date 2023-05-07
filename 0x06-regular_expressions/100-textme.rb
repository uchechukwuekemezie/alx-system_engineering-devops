#!/usr/bin/env ruby
# A regex that matches a given pattern
# A script that outputs: [SENDER],[RECEIVER],[FLAGS]
# The sender's phone number or name (including country code if present)
# The receiver's phone number or name (including country code if present)
# The flags that were used
puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
