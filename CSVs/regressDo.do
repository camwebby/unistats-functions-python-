drop if mediantariff == 0
drop if strpos(studymode, "PartTime")
regress salary6monthsafter mediantariff
sum salary6monthsafter

