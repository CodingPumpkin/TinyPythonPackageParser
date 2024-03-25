#!/bin/tclsh

proc parse_M_message {raw} {
	set message [lindex $raw end]
	#puts "$packege_type: Packege type is M"
	#puts "The message is: $message"
	return $message
}

proc is_valid_date {raw_date} {
	if {![regexp -expanded {^\d{8}$} $raw_date]} {
		return 0
	} else {
		return [string equal [clock format [clock scan $raw_date  -format "%d%m%Y"] -format "%d%m%Y"] $raw_date]
	}
}

proc is_valid_time {raw_time} {
	if { ![regexp -expanded {^\d{6}$} $raw_time] } {
		return 0
	} else {
		return [string equal [clock format [clock scan $raw_time -format "%S%M%H"] -format "%S%M%H"] $raw_time]
	}
}

proc get_date {raw_date} {
	if { [is_valid_date $raw_date] } {
		return $raw_date
	} else {
		puts "Invalid date. 01.01.2001 is set instead"
		return "01012001"
	}
}

proc get_time {raw_time} {
	if { [is_valid_time $raw_time] } {
		return $raw_time
	} else {
		puts "Invalid time. 00:00:00 is set instead"
		return "000000"
	}
}

proc get_course {raw_degrees} {
	if { [is_valid_time $raw_time] } {
		return $raw_time
	} else {
		puts "Invalid time. 00:00:00 is set instead"
		return "000000"
	}
}

proc is_int {num} {
	if {[string is integer $num]} {
		return $num
	} else {
		puts "Warning! $num is not a whole number. Setting value to zero"
		return 0
	}
}

proc is_float {num} {
	if {[string is double $num]} {
		return $num
	} else {
		puts "Warning! $num is not a number. Setting value to zero"
		return 0.0
	}
}

proc check_lat {c} {
	if {$c == "N" || $c == "S"} {
		return $c
	} else {
		puts "Warning! $c is not a valid parameter. Setting N instead"
		return "N"
	}
}

proc check_lon {c} {
	if {$c == "E" || $c == "W"} {
		return $c
	} else {
		puts "Warning! $c is not a valid parameter. Setting W instead"
		return "W"
	}
}


proc parse_SD_message {raw_data} {
	puts "packege_type: Packege type is SD"
	set tokens [split [lindex $raw_data end] ";"]
	puts [llength $tokens]
	if {[llength $tokens] != 10} {
		puts "Invalid message size for SD type. Setting default values"
		set SD(date) "01012001"
		set SD(time) "000000"
		set SD(lat_1) 0.0
		set SD(lat_2) "N"
		set SD(lon_1) 0.0
		set SD(lon_2) "W"
		set SD(speed) 0
		set SD(course) 0
		set SD(height) 1
		set SD(sats) 0
	} else {
		set SD(date) [get_date [lindex $tokens {0}]]
		set SD(time) [get_time [lindex $tokens {1}]]
		set SD(lat_1) [is_float [lindex $tokens {2}]]
		set SD(lat_2) [check_lat [lindex $tokens {3}]]
		set SD(lon_1) [is_float [lindex $tokens {4}]]
		set SD(lon_2) [check_lon [lindex $tokens {5}]]
		set SD(speed) [is_int [lindex $tokens {6}]]
		set SD(course) [expr [is_int [lindex $tokens {7}]] % 360]
		set SD(height) [is_int [lindex $tokens {8}]]
		set SD(sats) [is_int [lindex $tokens {9}]]
	}
	return [array get SD]
}

puts "Enter data packege:"
gets stdin sample_pkg
regexp {[A-Z]+} $sample_pkg packege_type
set raw_data [split [string trim $sample_pkg] "#"]
if {$packege_type == "M"} {
	puts [parse_M_message $raw_data]
} elseif {$packege_type == "SD"} {
	puts [parse_SD_message $raw_data]
} else {
	puts "Error. Unknown packege type"
}
