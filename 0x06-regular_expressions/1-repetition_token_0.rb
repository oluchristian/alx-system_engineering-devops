#!/usr/bin/env ruby
# A regular expression that is a repetition token
puts ARGV[0].scan(/hb(t{2,5})n/).join
