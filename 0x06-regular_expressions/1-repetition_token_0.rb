#!/usr/bin/env ruby
# A regular expression that is a repetition token
puts ARGV[0].scan(/hbt{2,5}n/).join
