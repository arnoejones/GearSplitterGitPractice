# Purpose: Store gear ratios in one location for a lookup
#
# Author:      Arno E Jones
#
# Created:     7/13/2018
# Copyright:   (c) jonesar 2018, 2019
# Licence:     This code can be freely shared and modified as long as the author is credited with the original (this) version.
#-------------------------------------------------------------------------------
# this is mod 1 from Alpha branch

# This is mod 1
# This is mod 2
# This is mod 3
# this is the push/pull github
def tj_auto_trans_ratios():
    tj_automatic_transmission_ratio = [
        2.21,  #reverse
        2.84  #1st

    ]
def jk_auto_trans_ratios():
    jk_automatic_transmission_ratio = [
        3.16,  # reverse
        3.59,  # 1st
        2.19,  # 2nd
        1.41,  # 3rd
        1.0,  # 4th
        0.83,  # 5th
    ]
    return jk_automatic_transmission_ratio


def jk_manual_trans_ratios():
    jk_manual_transmission_ratio = [
        0.797,  # reverse
        4.46,  # 1st
        2.61,  # 2nd
        1.72,  # 3rd
        1.25,  # 4th
        1.0,  # 5th
        0.797,  # 6th
    ]
    return (jk_manual_transmission_ratio)

def jl_automatic_trans_ratios():
    jl_automatic_transmission_ratio = [
        3.30,  # reverse
        4.71,  # 1st
        3.14,  # 2nd
        2.10,
        1.67,
        1.29,
        1.00,
        0.84,  # 7th
        0.67   # 8th
    ]
    return jl_automatic_transmission_ratio

def jl_manual_trans_ratios():
    jl_manual_transmission_ratio = [
        4.49,  # reverse
        5.13,  # 1st
        2.63,  # 2nd
        1.54,
        1.00,
        0.81,  # 5th
        0.72   # 6th
    ]
    return jl_manual_transmission_ratio
