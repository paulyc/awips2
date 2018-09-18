##
# This software was developed and / or modified by Raytheon Company,
# pursuant to Contract DG133W-05-CQ-1067 with the US Government.
# 
# U.S. EXPORT CONTROLLED TECHNICAL DATA
# This software product contains export-restricted data whose
# export/transfer/disclosure is restricted by U.S. law. Dissemination
# to non-U.S. persons whether in the United States or abroad requires
# an export license or other authorization.
# 
# Contractor Name:        Raytheon Company
# Contractor Address:     6825 Pine Street, Suite 340
#                         Mail Stop B8
#                         Omaha, NE 68106
#                         402.291.0100
# 
# See the AWIPS II Master Rights File ("Master Rights File.pdf") for
# further licensing information.
##
# ----------------------------------------------------------------------------
# This software is in the public domain, furnished "as is", without technical
# support, and with no warranty, express or implied, as to its usefulness for
# any purpose.
#
# Create Grids
#
# Author: hansen
# ----------------------------------------------------------------------------

import TestScript

Public_createGrids = [
        ("Fcst", "MaxT", "SCALAR", "MaxTBegin -24", "MaxTEnd -24", 60, "all"),
        ("Fcst", "MaxT", "SCALAR", "MaxTBegin", "MaxTEnd", 78, "all"),
        ("Fcst", "MaxT", "SCALAR", "MaxTBegin + 24", "MaxTEnd + 24", 79, "all"),
        ("Fcst", "MaxT", "SCALAR", "MaxTBegin + 48", "MaxTEnd + 48", 78, "all"),
        ("Fcst", "MaxT", "SCALAR", "MaxTBegin + 72", "MaxTEnd + 72", 80, "all"),
        ("Fcst", "MaxT", "SCALAR", "MaxTBegin + 96", "MaxTEnd + 96", 81, "all"),
        ("Fcst", "MaxT", "SCALAR", "MaxTBegin + 120", "MaxTEnd + 120", 83, "all"),
        ("Fcst", "MaxT", "SCALAR", "MaxTBegin + 144", "MaxTEnd + 144", 84, "all"),
        ("Fcst", "MaxT", "SCALAR", "MaxTBegin + 168", "MaxTEnd + 168", 86, "all"),

        ("Fcst", "MinT", "SCALAR", "MinTBegin-24", "MinTEnd-24", 40, "all"),        
        ("Fcst", "MinT", "SCALAR", "MinTBegin", "MinTEnd", 60, "all"),
        ("Fcst", "MinT", "SCALAR", "MinTBegin + 24", "MinTEnd + 24", 68, "all"),
        ("Fcst", "MinT", "SCALAR", "MinTBegin + 48", "MinTEnd + 48", 65, "all"),
        ("Fcst", "MinT", "SCALAR", "MinTBegin + 72", "MinTEnd + 72", 64, "all"),
        ("Fcst", "MinT", "SCALAR", "MinTBegin + 96", "MinTEnd + 96", 63, "all"),
        ("Fcst", "MinT", "SCALAR", "MinTBegin + 120", "MinTEnd + 120", 66, "all"),
        ("Fcst", "MinT", "SCALAR", "MinTBegin + 144", "MinTEnd + 144", 68, "all"),
        ("Fcst", "MinT", "SCALAR", "MinTBegin + 168", "MinTEnd + 168", 67, "all"),

        ("Fcst", "T", "SCALAR", 0, 12,  55, "all"),
        ("Fcst", "T", "SCALAR", 12, 24, 45, "all"),
        ("Fcst", "T", "SCALAR", 24, 36, 75, "all"),
        ("Fcst", "T", "SCALAR", 36, 48, 55, "all"),
        ("Fcst", "T", "SCALAR", 48, 60, 65, "all"),
        ("Fcst", "T", "SCALAR", 60, 72, 70, "all"),
        ("Fcst", "T", "SCALAR", 72, 84, 80, "all"),
        ("Fcst", "T", "SCALAR", 84, 96, 75, "all"),
        ("Fcst", "T", "SCALAR", 96, 108, 75 , "all"),

        ("Fcst", "Td", "SCALAR", 0, 12,  55, "all"),
        ("Fcst", "Td", "SCALAR", 12, 24, 45, "all"),
        ("Fcst", "Td", "SCALAR", 24, 36, 75, "all"),
        ("Fcst", "Td", "SCALAR", 36, 48, 55, "all"),
        ("Fcst", "Td", "SCALAR", 48, 60, 65, "all"),
        ("Fcst", "Td", "SCALAR", 60, 72, 70, "all"),
        ("Fcst", "Td", "SCALAR", 72, 84, 80, "all"),
        ("Fcst", "Td", "SCALAR", 84, 96, 75, "all"),
        ("Fcst", "Td", "SCALAR", 96, 108, 75 , "all"),

        ("Fcst", "HeatIndex", "SCALAR", 0, 12,  95, "all"),
        ("Fcst", "HeatIndex", "SCALAR", 12, 24, 105, "all"),
        ("Fcst", "HeatIndex", "SCALAR", 24, 36, 103, "all"),
        ("Fcst", "HeatIndex", "SCALAR", 36, 48, 85, "all"),
        ("Fcst", "HeatIndex", "SCALAR", 48, 60, 75, "all"),
        ("Fcst", "HeatIndex", "SCALAR", 60, 72, 110, "all"),
        ("Fcst", "HeatIndex", "SCALAR", 72, 84, 120, "all"),
        ("Fcst", "HeatIndex", "SCALAR", 84, 96, 108, "all"),
        ("Fcst", "HeatIndex", "SCALAR", 96, 108, 75 , "all"),

        ("Fcst", "WindChill", "SCALAR", 0, 12,  -20, "all"),
        ("Fcst", "WindChill", "SCALAR", 12, 24, 10, "all"),
        ("Fcst", "WindChill", "SCALAR", 24, 36, 20, "all"),
        ("Fcst", "WindChill", "SCALAR", 36, 48, 55, "all"),
        ("Fcst", "WindChill", "SCALAR", 48, 60, 65, "all"),
        ("Fcst", "WindChill", "SCALAR", 60, 72, -30, "all"),
        ("Fcst", "WindChill", "SCALAR", 72, 84, 30, "all"),
        ("Fcst", "WindChill", "SCALAR", 84, 96, 20, "all"),
        ("Fcst", "WindChill", "SCALAR", 96, 108, 10, "all"),

        ("Fcst", "Wind", "VECTOR", 0, 12, (10, "SW"), "all"),
        ("Fcst", "Wind", "VECTOR", 12, 24, (40, "SE"), "all"),
        ("Fcst", "Wind", "VECTOR", 24, 36, (35, "NW"), "all"),
        ("Fcst", "Wind", "VECTOR", 36, 48, (45, "W"), "all"),
        ("Fcst", "Wind", "VECTOR", 48, 60, (50, "SW"), "all"),
        ("Fcst", "Wind", "VECTOR", 60, 72, (45, "E"), "all"),
        ("Fcst", "Wind", "VECTOR", 72, 84, (60, "W"), "all"),
        ("Fcst", "Wind", "VECTOR", 84, 96,(55, "SW"), "all"),
        ("Fcst", "Wind", "VECTOR", 96, 108,(55, "SW"), "all"),
        ("Fcst", "Wind", "VECTOR", 108, 120, (42, "E"), "all"),
        ("Fcst", "Wind", "VECTOR", 120, 132, (45, "E"), "all"),
        ("Fcst", "Wind", "VECTOR", 132, 144, (46, "E"), "all"),
        ("Fcst", "Wind", "VECTOR", 144, 156, (48, "E"), "all"),
        ("Fcst", "Wind", "VECTOR", 156, 168, (60, "E"), "all"),
        ("Fcst", "Wind", "VECTOR", 168, 180, (35, "E"), "all"),
        ("Fcst", "Wind", "VECTOR", 180, 192, (50, "E"), "all"),

        ("Fcst", "WindGust", "SCALAR", 0, 12,  25, "all"),
        ("Fcst", "WindGust", "SCALAR", 12, 24, 0, "all"),
        ("Fcst", "WindGust", "SCALAR", 24, 36, 45, "all"),
        ("Fcst", "WindGust", "SCALAR", 36, 48, 0, "all"),
        ("Fcst", "WindGust", "SCALAR", 48, 60, 0, "all"),
        ("Fcst", "WindGust", "SCALAR", 60, 72, 0, "all"),
        ("Fcst", "WindGust", "SCALAR", 72, 84, 0, "all"),
        ("Fcst", "WindGust", "SCALAR", 84, 96, 0, "all"),
        ("Fcst", "WindGust", "SCALAR", 96, 108, 0, "all"),

        ("Fcst", "SnowAmt", "SCALAR", 0, 12,  2, "all"),
        ("Fcst", "SnowAmt", "SCALAR", 12, 24, 0, "all"),
        ("Fcst", "SnowAmt", "SCALAR", 24, 36, 3, "all"),
        ("Fcst", "SnowAmt", "SCALAR", 36, 48, 5, "all"),
        ("Fcst", "SnowAmt", "SCALAR", 48, 60, 10, "all"),
        ("Fcst", "SnowAmt", "SCALAR", 60, 72, 0, "all"),
        ("Fcst", "SnowAmt", "SCALAR", 72, 84, 2, "all"),
        ("Fcst", "SnowAmt", "SCALAR", 84, 96, 4, "all"),
        ("Fcst", "SnowAmt", "SCALAR", 96, 108, 0, "all"),

        ("Fcst", "IceAccum", "SCALAR", 0, 12,  2, "all"),
        ("Fcst", "IceAccum", "SCALAR", 12, 24, 0, "all"),
        ("Fcst", "IceAccum", "SCALAR", 24, 36, 3, "all"),
        ("Fcst", "IceAccum", "SCALAR", 36, 48, 5, "all"),
        ("Fcst", "IceAccum", "SCALAR", 48, 60, 5, "all"),
        ("Fcst", "IceAccum", "SCALAR", 60, 72, 0, "all"),
        ("Fcst", "IceAccum", "SCALAR", 72, 84, 2, "all"),
        ("Fcst", "IceAccum", "SCALAR", 84, 96, 4, "all"),
        ("Fcst", "IceAccum", "SCALAR", 96, 108, 0, "all"),

        ("Fcst", "SnowLevel", "SCALAR", 0, 12,  500, "all"),
        ("Fcst", "SnowLevel", "SCALAR", 12, 24, 50, "all"),
        ("Fcst", "SnowLevel", "SCALAR", 24, 36, 1000, "all"),
        ("Fcst", "SnowLevel", "SCALAR", 36, 48, 500, "all"),
        ("Fcst", "SnowLevel", "SCALAR", 48, 60, 100, "all"),
        ("Fcst", "SnowLevel", "SCALAR", 60, 72, 1000, "all"),
        ("Fcst", "SnowLevel", "SCALAR", 72, 84, 2000, "all"),
        ("Fcst", "SnowLevel", "SCALAR", 84, 96, 0, "all"),
        ("Fcst", "SnowLevel", "SCALAR", 96, 108, 0, "all"),
        
        ("Fcst", "FzLevel", "SCALAR", 0, 24, 5000, "all"),
        ("Fcst", "FzLevel", "SCALAR", 24, 48, 10000, "all"),
        ("Fcst", "FzLevel", "SCALAR", 48, 72, 4000, "all"),
        ("Fcst", "FzLevel", "SCALAR", 72, 96, 20000, "all"),
        ("Fcst", "FzLevel", "SCALAR", 96, 120, 3000, "all"),
        ("Fcst", "FzLevel", "SCALAR", 120, 144, 16000, "all"),
        ("Fcst", "FzLevel", "SCALAR", 144, 168, 18500, "all"),
        ("Fcst", "FzLevel", "SCALAR", 168, 192, 21000, "all"),

        ("Fcst", "Sky", "SCALAR", 0, 12, 100, "all"),
        ("Fcst", "Sky", "SCALAR", 12, 24, 95, "all"),
        ("Fcst", "Sky", "SCALAR", 24, 36, 0, "all"),
        ("Fcst", "Sky", "SCALAR", 36, 48, 15, "all"),
        ("Fcst", "Sky", "SCALAR", 48, 60, 30, "all"),
        ("Fcst", "Sky", "SCALAR", 60, 72, 55, "all"),
        ("Fcst", "Sky", "SCALAR", 72, 84, 65, "all"),
        ("Fcst", "Sky", "SCALAR", 84, 96, 70, "all"),
        ("Fcst", "Sky", "SCALAR", 96, 108, 30, "all"),
        ("Fcst", "Sky", "SCALAR", 108, 120, 48, "all"),
        ("Fcst", "Sky", "SCALAR", 120, 132, 100, "all"),
        ("Fcst", "Sky", "SCALAR", 132, 144, 10, "all"),
        ("Fcst", "Sky", "SCALAR", 144, 156, 75, "all"),
        ("Fcst", "Sky", "SCALAR", 156, 168, 25, "all"),
        ("Fcst", "Sky", "SCALAR", 168, 180, 20, "all"),
        ("Fcst", "Sky", "SCALAR", 180, 192, 87, "all"),
                
        ("Fcst", "Wx", "WEATHER", 0, 12, "Patchy:F:+:<NoVis>:", "all"),
        ("Fcst", "Wx", "WEATHER", 12, 24, "Wide:T:<NoInten>:<NoVis>:", "all"),
        ("Fcst", "Wx", "WEATHER", 24, 36, "Chc:RW:-:<NoVis>:", "all"),
        ("Fcst", "Wx", "WEATHER", 36, 48, "Frq:R:--:<NoVis>:", "all"),
        ("Fcst", "Wx", "WEATHER", 48, 60, "Wide:ZR:-:<NoVis>:", "all"),
        ("Fcst", "Wx", "WEATHER", 60, 72, "Lkly:S:--:<NoVis>:", "all"),
        ("Fcst", "Wx", "WEATHER", 72, 84, "Wide:IP:--:<NoVis>:", "all"),
        ("Fcst", "Wx", "WEATHER", 84, 96, "Areas:BS:<NoInten>:<NoVis>:", "all"),
        ("Fcst", "Wx", "WEATHER", 96, 108, "Patchy:F:<NoInten>:<NoVis>:", "all"),
        ("Fcst", "Wx", "WEATHER", 108, 120, "Lkly:L:--:<NoVis>:", "all"),
        ("Fcst", "Wx", "WEATHER", 120, 132, "SChc:ZL:--:<NoVis>:", "all"),
        ("Fcst", "Wx", "WEATHER", 132, 144, "Num:T:<NoInten>:<NoVis>:", "all"),
        ("Fcst", "Wx", "WEATHER", 144, 156, "Iso:ZY:-:<NoVis>:", "all"),
        ("Fcst", "Wx", "WEATHER", 156, 168, "Areas:FR:<NoInten>:<NoVis>:", "all"),
        ("Fcst", "Wx", "WEATHER", 168, 180, "Chc:RW:-:<NoVis>:", "all"),
        ("Fcst", "Wx", "WEATHER", 180, 192, "Brf:R:m:<NoVis>:", "all"),

        ("Fcst", "PoP", "SCALAR", 0, 12, 0, "all"),
        ("Fcst", "PoP", "SCALAR", 12, 24, 90 , "all"),
        ("Fcst", "PoP", "SCALAR", 24, 36, 90, "all"),
        ("Fcst", "PoP", "SCALAR", 36, 48, 90, "all"),
        ("Fcst", "PoP", "SCALAR", 48, 60, 90, "all"),
        ("Fcst", "PoP", "SCALAR", 60, 72, 70, "all"),
        ("Fcst", "PoP", "SCALAR", 72, 84, 90, "all"),
        ("Fcst", "PoP", "SCALAR", 84, 96, 0, "all"),
        ("Fcst", "PoP", "SCALAR", 96, 108, 0, "all"),
        ("Fcst", "PoP", "SCALAR", 108, 120, 70, "all"),
        ("Fcst", "PoP", "SCALAR", 120, 132, 20, "all"),
        ("Fcst", "PoP", "SCALAR", 132, 144, 70, "all"),
        ("Fcst", "PoP", "SCALAR", 144, 156, 20, "all"),
        ("Fcst", "PoP", "SCALAR", 156, 168, 0, "all"),
        ("Fcst", "PoP", "SCALAR", 168, 180, 40, "all"),
        ("Fcst", "PoP", "SCALAR", 180, 192, 90, "all"),

        ]

Hazard_createGrids = [
        ("Fcst", "Hazards", "DISCRETE", 0, 96, "CF.Y^FF.A^MA.S^FW.W^BZ.W", "all"),
        ]

Fire_createGrids = [
        ("Fcst", "MaxRH", "SCALAR", "MaxRHBegin-24", "MaxRHEnd-24", 60, "all"),
        ("Fcst", "MaxRH", "SCALAR", "MaxRHBegin", "MaxRHEnd", 78, "all"),
        ("Fcst", "MaxRH", "SCALAR", "MaxRHBegin + 24", "MaxRHEnd + 24", 80, "all"),
        ("Fcst", "MaxRH", "SCALAR", "MaxRHBegin + 48", "MaxRHEnd + 48", 85, "all"),
        ("Fcst", "MaxRH", "SCALAR", "MaxRHBegin + 72", "MaxRHEnd + 72", 90, "all"),
        ("Fcst", "MaxRH", "SCALAR", "MaxRHBegin + 96", "MaxRHEnd + 96", 87, "all"),
        ("Fcst", "MaxRH", "SCALAR", "MaxRHBegin + 120", "MaxRHEnd + 120", 88, "all"),
        ("Fcst", "MaxRH", "SCALAR", "MaxRHBegin + 144", "MaxRHEnd + 144", 89, "all"),
        ("Fcst", "MaxRH", "SCALAR", "MaxRHBegin + 168", "MaxRHEnd + 168", 90, "all"),
        
        ("Fcst", "MinRH", "SCALAR", "MinRHBegin-24", "MinRHEnd-24", 40, "all"),
        ("Fcst", "MinRH", "SCALAR", "MinRHBegin", "MinRHEnd", 65, "all"),
        ("Fcst", "MinRH", "SCALAR", "MinRHBegin + 24", "MinRHEnd + 24", 68, "all"),
        ("Fcst", "MinRH", "SCALAR", "MinRHBegin + 48", "MinRHEnd + 48", 70, "all"),
        ("Fcst", "MinRH", "SCALAR", "MinRHBegin + 72", "MinRHEnd + 72", 73, "all"), 
        ("Fcst", "MinRH", "SCALAR", "MinRHBegin + 96", "MinRHEnd + 96", 74, "all"),
        ("Fcst", "MinRH", "SCALAR", "MinRHBegin + 120", "MinRHEnd + 120", 72, "all"),
        ("Fcst", "MinRH", "SCALAR", "MinRHBegin + 144", "MinRHEnd + 144", 70, "all"),
        ("Fcst", "MinRH", "SCALAR", "MinRHBegin + 168", "MinRHEnd + 168", 71, "all"),
        
        ("Fcst", "RH", "SCALAR", 0, 12, 60, "all"),
        ("Fcst", "RH", "SCALAR", 12, 24, 78, "all"),
        ("Fcst", "RH", "SCALAR", 24, 36, 30, "all"),
        ("Fcst", "RH", "SCALAR", 36, 48, 45, "all"),
        ("Fcst", "RH", "SCALAR", 48, 60, 55, "all"),
        ("Fcst", "RH", "SCALAR", 60, 72, 65, "all"),
        ("Fcst", "RH", "SCALAR", 72, 84, 70, "all"),
        ("Fcst", "RH", "SCALAR", 84, 96, 45, "all"),
        ("Fcst", "RH", "SCALAR", 96, 108, 20, "all"),
        ("Fcst", "RH", "SCALAR", 108, 120, 25, "all"),
        ("Fcst", "RH", "SCALAR", 120, 132, 35, "all"),
        ("Fcst", "RH", "SCALAR", 132, 144, 43, "all"),
        ("Fcst", "RH", "SCALAR", 144, 156, 15, "all"),
        ("Fcst", "RH", "SCALAR", 156, 168, 3, "all"),
        ("Fcst", "RH", "SCALAR", 168, 180, 28, "all"),
        ("Fcst", "RH", "SCALAR", 180, 192, 90, "all"),

        ("Fcst", "TransWind", "VECTOR", 0, 12, (10, "SW"), "all"),
        ("Fcst", "TransWind", "VECTOR", 12, 24, (5, "W"), "all"),
        ("Fcst", "TransWind", "VECTOR", 24, 48, (10, "NW"), "all"),
        ("Fcst", "TransWind", "VECTOR", 48, 72, (20, "W"), "all"),
        ("Fcst", "TransWind", "VECTOR", 72, 96, (30, "W"), "all"),
        ("Fcst", "TransWind", "VECTOR", 96, 120, (40, "W"), "all"),
        ("Fcst", "TransWind", "VECTOR", 120, 144, (50, "W"), "all"),
        ("Fcst", "TransWind", "VECTOR", 144, 168, (60, "W"), "all"),
        ("Fcst", "TransWind", "VECTOR", 168, 192, (70, "W"), "all"),

        ("Fcst", "LAL", "SCALAR", 0, 12, 1, "all"),
        ("Fcst", "LAL", "SCALAR", 12, 24, 2, "all"),
        ("Fcst", "LAL", "SCALAR", 24, 36, 3, "all"),
        ("Fcst", "LAL", "SCALAR", 36, 48, 4, "all"),
        ("Fcst", "LAL", "SCALAR", 48, 60, 5, "all"),
        ("Fcst", "LAL", "SCALAR", 60, 72, 6, "all"),
        ("Fcst", "LAL", "SCALAR", 72, 84, 3, "all"),
        ("Fcst", "LAL", "SCALAR", 84, 96, 1, "all"),
        ("Fcst", "LAL", "SCALAR", 96, 108, 2, "all"),
        ("Fcst", "LAL", "SCALAR", 108, 120, 4, "all"),
        ("Fcst", "LAL", "SCALAR", 120, 132, 5, "all"),
        ("Fcst", "LAL", "SCALAR", 132, 144, 3, "all"),
        ("Fcst", "LAL", "SCALAR", 144, 156, 2, "all"),
        ("Fcst", "LAL", "SCALAR", 156, 168, 5, "all"),
        ("Fcst", "LAL", "SCALAR", 168, 180, 6, "all"),
        ("Fcst", "LAL", "SCALAR", 180, 192, 3, "all"),
                        
        ("Fcst", "CWR", "SCALAR", 0, 12, 0, "all"),
        ("Fcst", "CWR", "SCALAR", 12, 24, 20, "all"),
        ("Fcst", "CWR", "SCALAR", 24, 36, 30, "all"),
        ("Fcst", "CWR", "SCALAR", 36, 48, 30, "all"),
        ("Fcst", "CWR", "SCALAR", 48, 60, 45, "all"),
        ("Fcst", "CWR", "SCALAR", 60, 72, 60, "all"),
        ("Fcst", "CWR", "SCALAR", 72, 84, 25, "all"),
        ("Fcst", "CWR", "SCALAR", 84, 96, 47, "all"),
        ("Fcst", "CWR", "SCALAR", 96, 108, 34, "all"),
        ("Fcst", "CWR", "SCALAR", 108, 120, 60, "all"),
        ("Fcst", "CWR", "SCALAR", 120, 132, 55, "all"),
        ("Fcst", "CWR", "SCALAR", 132, 144, 50, "all"),
        ("Fcst", "CWR", "SCALAR", 144, 156, 20, "all"),
        ("Fcst", "CWR", "SCALAR", 156, 168, 10, "all"),
        ("Fcst", "CWR", "SCALAR", 168, 180, 5, "all"),
        ("Fcst", "CWR", "SCALAR", 180, 192, 40, "all"),
                
        ("Fcst", "QPF", "SCALAR", 0, 12, 0, "all"),
        ("Fcst", "QPF", "SCALAR", 12, 24, 0.05, "all"),
        ("Fcst", "QPF", "SCALAR", 24, 36, 0.1, "all"),
        ("Fcst", "QPF", "SCALAR", 36, 48, 0, "all"),
        ("Fcst", "QPF", "SCALAR", 48, 60, 5, "all"),
        ("Fcst", "QPF", "SCALAR", 60, 72, 4.5, "all"),
        ("Fcst", "QPF", "SCALAR", 72, 84, 1.5, "all"),
        ("Fcst", "QPF", "SCALAR", 84, 96, 2.5, "all"),
        ("Fcst", "QPF", "SCALAR", 96, 108, 3.5, "all"),
        ("Fcst", "QPF", "SCALAR", 108, 120, 4.0, "all"),
        ("Fcst", "QPF", "SCALAR", 120, 132, 1.0, "all"),
        ("Fcst", "QPF", "SCALAR", 132, 144, 2.0, "all"),
        ("Fcst", "QPF", "SCALAR", 144, 156, 3.0, "all"),
        ("Fcst", "QPF", "SCALAR", 156, 168, 1.3, "all"),
        ("Fcst", "QPF", "SCALAR", 168, 180, 0.12, "all"),
        ("Fcst", "QPF", "SCALAR", 180, 192, 0.34, "all"),
        
        ("Fcst", "Haines", "SCALAR", 0, 12, 2, "all"),
        ("Fcst", "Haines", "SCALAR", 12, 24, 3, "all"),
        ("Fcst", "Haines", "SCALAR", 24, 36, 4, "all"),
        ("Fcst", "Haines", "SCALAR", 36, 48, 6, "all"),
        ("Fcst", "Haines", "SCALAR", 48, 60, 2, "all"),
        ("Fcst", "Haines", "SCALAR", 60, 72, 3, "all"),
        ("Fcst", "Haines", "SCALAR", 72, 84, 2, "all"),
        ("Fcst", "Haines", "SCALAR", 84, 96, 3, "all"),
        ("Fcst", "Haines", "SCALAR", 96, 108, 5, "all"),
        ("Fcst", "Haines", "SCALAR", 108, 120, 6, "all"),
        ("Fcst", "Haines", "SCALAR", 120, 132, 3, "all"),
        ("Fcst", "Haines", "SCALAR", 132, 144, 2, "all"),
        ("Fcst", "Haines", "SCALAR", 144, 156, 3, "all"),
        ("Fcst", "Haines", "SCALAR", 156, 168, 4, "all"),
        ("Fcst", "Haines", "SCALAR", 168, 180, 3, "all"),
        ("Fcst", "Haines", "SCALAR", 180, 192, 6, "all"),
        
        ("Fcst", "MixHgt", "SCALAR", 0, 24, 5000, "all"),
        ("Fcst", "MixHgt", "SCALAR", 24, 48, 10000, "all"),
        ("Fcst", "MixHgt", "SCALAR", 48, 72, 4000, "all"),
        ("Fcst", "MixHgt", "SCALAR", 72, 96, 20000, "all"),
        ("Fcst", "MixHgt", "SCALAR", 96, 120, 3000, "all"),
        ("Fcst", "MixHgt", "SCALAR", 120, 144, 16000, "all"),
        ("Fcst", "MixHgt", "SCALAR", 144, 168, 18500, "all"),
        ("Fcst", "MixHgt", "SCALAR", 168, 192, 20000, "all"),

        ("Fcst", "MarineLayer", "SCALAR", 0, 24, 1000, "all"),
        ("Fcst", "MarineLayer", "SCALAR", 24, 48, 2000, "all"),
        ("Fcst", "MarineLayer", "SCALAR", 48, 72, 4000, "all"),
        ("Fcst", "MarineLayer", "SCALAR", 72, 96, 5280, "all"),
        ("Fcst", "MarineLayer", "SCALAR", 96, 120, 6500, "all"),
        ("Fcst", "MarineLayer", "SCALAR", 120, 144, 10000, "all"),
        ("Fcst", "MarineLayer", "SCALAR", 144, 168, 12300, "all"),
        ("Fcst", "MarineLayer", "SCALAR", 168, 192, 14500, "all"),

        ("Fcst", "Wind20ft", "VECTOR", 0, 12, (5, "N"), "all"),
        ("Fcst", "Wind20ft", "VECTOR", 12, 24, (40, "NE"), "all"),
        ("Fcst", "Wind20ft", "VECTOR", 24, 36, (10, "NW"), "all"),
        ("Fcst", "Wind20ft", "VECTOR", 36, 48, (0, "N"), "all"),
        ("Fcst", "Wind20ft", "VECTOR", 48, 60, (125, "E"), "all"),
        ("Fcst", "Wind20ft", "VECTOR", 60, 72, (90, "S"), "all"),
        ("Fcst", "Wind20ft", "VECTOR", 72, 84, (50, "S"), "all"),
        ("Fcst", "Wind20ft", "VECTOR", 84, 96, (100, "S"), "all"),
        ("Fcst", "Wind20ft", "VECTOR", 96, 108, (0, "S"), "all"),
        ("Fcst", "Wind20ft", "VECTOR", 108, 120, (10, "S"), "all"),
        ("Fcst", "Wind20ft", "VECTOR", 120, 132, (30, "S"), "all"),
        ("Fcst", "Wind20ft", "VECTOR", 132, 144, (60, "S"), "all"),
        ("Fcst", "Wind20ft", "VECTOR", 144, 156, (25, "S"), "all"),
        ("Fcst", "Wind20ft", "VECTOR", 156, 168, (68, "S"), "all"),
        ("Fcst", "Wind20ft", "VECTOR", 168, 180, (15, "S"), "all"),
        ("Fcst", "Wind20ft", "VECTOR", 180, 192, (2, "S"), "all"),
        
        ("Fcst", "VentRate", "SCALAR", 0, 12, 160000, "all"),
        ("Fcst", "VentRate", "SCALAR", 12, 24, 100000, "all"),
        ("Fcst", "VentRate", "SCALAR", 24, 36, 50000, "all"),
        ("Fcst", "VentRate", "SCALAR", 36, 48, 20000, "all"),
        ("Fcst", "VentRate", "SCALAR", 48, 60, 70000, "all"),
        ("Fcst", "VentRate", "SCALAR", 60, 144, 4000, "all"),
        ("Fcst", "VentRate", "SCALAR", 144, 168, 6900, "all"),
        ("Fcst", "VentRate", "SCALAR", 168, 192, 30000, "all"),
        
        ("Fcst", "Stability", "SCALAR", 0, 12, 1, "all"),
        ("Fcst", "Stability", "SCALAR", 12, 24, 2, "all"), 
        ("Fcst", "Stability", "SCALAR", 24, 36, 1, "all"),
        ("Fcst", "Stability", "SCALAR", 36, 48, 3, "all"),
        ("Fcst", "Stability", "SCALAR", 48, 60, 4, "all"),
        ("Fcst", "Stability", "SCALAR", 60, 72, 5, "all"),
        ("Fcst", "Stability", "SCALAR", 72, 84, 1, "all"),
        ("Fcst", "Stability", "SCALAR", 84, 96, 2, "all"),
        ("Fcst", "Stability", "SCALAR", 96, 108, 3, "all"),
        ("Fcst", "Stability", "SCALAR", 108, 120, 4, "all"),
        ("Fcst", "Stability", "SCALAR", 120, 132, 5, "all"),
        ("Fcst", "Stability", "SCALAR", 132, 144, 4, "all"),
        ("Fcst", "Stability", "SCALAR", 144, 156, 3, "all"),
        ("Fcst", "Stability", "SCALAR", 156, 168, 2, "all"),
        ("Fcst", "Stability", "SCALAR", 168, 180, 1, "all"),
        ("Fcst", "Stability", "SCALAR", 180, 192, 3, "all"),
        
        ("Fcst", "HrsOfSun", "SCALAR", 0, 24, 6, "all"),
        ("Fcst", "HrsOfSun", "SCALAR", 24, 48, 7, "all"),
        ("Fcst", "HrsOfSun", "SCALAR", 48, 72, 5, "all"),
        ("Fcst", "HrsOfSun", "SCALAR", 72, 96, 5, "all"),
        ("Fcst", "HrsOfSun", "SCALAR", 96, 120, 5, "all"),
        ("Fcst", "HrsOfSun", "SCALAR", 120, 144, 5, "all"),
        ("Fcst", "HrsOfSun", "SCALAR", 144, 168, 5, "all"),
        ("Fcst", "HrsOfSun", "SCALAR", 168, 192, 5, "all"),
        
        ("Fcst", "DSI", "SCALAR", 0, 12, 0, "all"),
        ("Fcst", "DSI", "SCALAR", 12, 24, 2, "all"),
        ("Fcst", "DSI", "SCALAR", 24, 36, 6, "all"),
        ("Fcst", "DSI", "SCALAR", 36, 48, 1, "all"),
        ("Fcst", "DSI", "SCALAR", 48, 60, 5, "all"),
        ("Fcst", "DSI", "SCALAR", 60, 72, 4, "all"),
        ("Fcst", "DSI", "SCALAR", 72, 84, 3, "all"),
        ("Fcst", "DSI", "SCALAR", 84, 96, 2, "all"),
        ("Fcst", "DSI", "SCALAR", 96, 108, 1, "all"),
        ("Fcst", "DSI", "SCALAR", 108, 120, 0, "all"),
        ("Fcst", "DSI", "SCALAR", 120, 132, 5, "all"),
        ("Fcst", "DSI", "SCALAR", 132, 144, 4, "all"),
        ("Fcst", "DSI", "SCALAR", 144, 156, 3, "all"),
        ("Fcst", "DSI", "SCALAR", 156, 168, 2, "all"),
        ("Fcst", "DSI", "SCALAR", 168, 180, 1, "all"),
        ("Fcst", "DSI", "SCALAR", 180, 192, 0, "all"),
        ]


Marine_createGrids = [
        ("Fcst", "Swell", "VECTOR", 0, 3, (10, "SW"), "all"),
        ("Fcst", "Swell", "VECTOR", 3, 6, (20, "W"), "all"),
        ("Fcst", "Swell", "VECTOR", 6, 9, (30, "W"), "all"),
        ("Fcst", "Swell", "VECTOR", 9, 12, (20, "SW"), "all"),
        ("Fcst", "Swell", "VECTOR", 12, 18, (40, "SE"), "all"),
        ("Fcst", "Swell", "VECTOR", 18, 24, (40, "SW"), "all"),
        ("Fcst", "Swell", "VECTOR", 24, 36, (35, "NW"), "all"),
        ("Fcst", "Swell", "VECTOR", 36, 48, (45, "W"), "all"),
        ("Fcst", "Swell", "VECTOR", 48, 60, (50, "SW"), "all"),
        ("Fcst", "Swell", "VECTOR", 60, 72, (45, "E"), "all"),
        ("Fcst", "Swell", "VECTOR", 72, 84, (60, "W"), "all"),
        ("Fcst", "Swell", "VECTOR", 84, 96,(55, "SW"), "all"),
        ("Fcst", "Swell", "VECTOR", 96, 108,(55, "SW"), "all"),
        ("Fcst", "Swell", "VECTOR", 108, 120, (42, "E"), "all"),
        ("Fcst", "Swell", "VECTOR", 120, 132, (45, "E"), "all"),
        ("Fcst", "Swell", "VECTOR", 132, 144, (46, "E"), "all"),
        ("Fcst", "Swell", "VECTOR", 144, 156, (48, "E"), "all"),
        ("Fcst", "Swell", "VECTOR", 156, 168, (60, "E"), "all"),
        ("Fcst", "Swell", "VECTOR", 168, 180, (35, "E"), "all"),
        ("Fcst", "Swell", "VECTOR", 180, 192, (50, "E"), "all"),

        ("Fcst", "Swell2", "VECTOR", 0, 3, (10, "NE"), "all"),
        ("Fcst", "Swell2", "VECTOR", 3, 6, (20, "E"), "all"),
        ("Fcst", "Swell2", "VECTOR", 6, 9, (30, "E"), "all"),
        ("Fcst", "Swell2", "VECTOR", 9, 12, (20, "SE"), "all"),
        ("Fcst", "Swell2", "VECTOR", 12, 18, (40, "SW"), "all"),
        ("Fcst", "Swell2", "VECTOR", 18, 24, (40, "SE"), "all"),
        ("Fcst", "Swell2", "VECTOR", 24, 36, (35, "NE"), "all"),
        ("Fcst", "Swell2", "VECTOR", 36, 48, (45, "E"), "all"),
        ("Fcst", "Swell2", "VECTOR", 48, 60, (50, "SE"), "all"),
        ("Fcst", "Swell2", "VECTOR", 60, 72, (45, "W"), "all"),
        ("Fcst", "Swell2", "VECTOR", 72, 84, (60, "E"), "all"),
        ("Fcst", "Swell2", "VECTOR", 84, 96,(55, "SE"), "all"),
        ("Fcst", "Swell2", "VECTOR", 96, 108,(55, "SE"), "all"),
        ("Fcst", "Swell2", "VECTOR", 108, 120, (42, "W"), "all"),
        ("Fcst", "Swell2", "VECTOR", 120, 132, (45, "W"), "all"),
        ("Fcst", "Swell2", "VECTOR", 132, 144, (46, "W"), "all"),
        ("Fcst", "Swell2", "VECTOR", 144, 156, (48, "W"), "all"),
        ("Fcst", "Swell2", "VECTOR", 156, 168, (60, "W"), "all"),
        ("Fcst", "Swell2", "VECTOR", 168, 180, (35, "W"), "all"),
        ("Fcst", "Swell2", "VECTOR", 180, 192, (50, "W"), "all"),

        ("Fcst", "Period", "SCALAR", 0, 3,  10, "all"),
        ("Fcst", "Period", "SCALAR", 3, 6,  15, "all"),
        ("Fcst", "Period", "SCALAR", 6, 9,  20, "all"),
        ("Fcst", "Period", "SCALAR", 9, 12,  5, "all"),
        ("Fcst", "Period", "SCALAR", 12, 24, 10, "all"),
        ("Fcst", "Period", "SCALAR", 24, 36, 15, "all"),
        ("Fcst", "Period", "SCALAR", 36, 48, 20, "all"),
        ("Fcst", "Period", "SCALAR", 48, 60, 10, "all"),
        ("Fcst", "Period", "SCALAR", 60, 72, 17, "all"),
        ("Fcst", "Period", "SCALAR", 72, 84, 12, "all"),
        ("Fcst", "Period", "SCALAR", 84, 96, 13, "all"),
        ("Fcst", "Period", "SCALAR", 96, 108, 18, "all"),

        ("Fcst", "Period2", "SCALAR", 0, 3,  10, "all"),
        ("Fcst", "Period2", "SCALAR", 3, 6,  15, "all"),
        ("Fcst", "Period2", "SCALAR", 6, 9,  8, "all"),
        ("Fcst", "Period2", "SCALAR", 9, 12,  5, "all"),
        ("Fcst", "Period2", "SCALAR", 12, 24, 10, "all"),
        ("Fcst", "Period2", "SCALAR", 24, 36, 15, "all"),
        ("Fcst", "Period2", "SCALAR", 36, 48, 20, "all"),
        ("Fcst", "Period2", "SCALAR", 48, 60, 17, "all"),
        ("Fcst", "Period2", "SCALAR", 60, 72, 19, "all"),
        ("Fcst", "Period2", "SCALAR", 72, 84, 12, "all"),
        ("Fcst", "Period2", "SCALAR", 84, 96, 7, "all"),
        ("Fcst", "Period2", "SCALAR", 96, 108, 6, "all"),

        ("Fcst", "WindWaveHgt", "SCALAR", 0, 3,  10, "all"),
        ("Fcst", "WindWaveHgt", "SCALAR", 3, 6,  15, "all"),
        ("Fcst", "WindWaveHgt", "SCALAR", 6, 9,  25, "all"),
        ("Fcst", "WindWaveHgt", "SCALAR", 9, 12,  5, "all"),
        ("Fcst", "WindWaveHgt", "SCALAR", 12, 24, 10, "all"),
        ("Fcst", "WindWaveHgt", "SCALAR", 24, 36, 45, "all"),
        ("Fcst", "WindWaveHgt", "SCALAR", 36, 48, 20, "all"),
        ("Fcst", "WindWaveHgt", "SCALAR", 48, 60, 30, "all"),
        ("Fcst", "WindWaveHgt", "SCALAR", 60, 72, 40, "all"),
        ("Fcst", "WindWaveHgt", "SCALAR", 72, 84, 20, "all"),
        ("Fcst", "WindWaveHgt", "SCALAR", 84, 96, 20, "all"),
        ("Fcst", "WindWaveHgt", "SCALAR", 96, 108, 20, "all"),

        ("Fcst", "WaveHeight", "SCALAR", 0, 3,  10, "all"),
        ("Fcst", "WaveHeight", "SCALAR", 3, 6,  15, "all"),
        ("Fcst", "WaveHeight", "SCALAR", 6, 9,  25, "all"),
        ("Fcst", "WaveHeight", "SCALAR", 9, 12,  5, "all"),
        ("Fcst", "WaveHeight", "SCALAR", 12, 24, 10, "all"),
        ("Fcst", "WaveHeight", "SCALAR", 24, 36, 45, "all"),
        ("Fcst", "WaveHeight", "SCALAR", 36, 48, 20, "all"),
        ("Fcst", "WaveHeight", "SCALAR", 48, 60, 30, "all"),
        ("Fcst", "WaveHeight", "SCALAR", 60, 72, 40, "all"),
        ("Fcst", "WaveHeight", "SCALAR", 72, 84, 20, "all"),
        ("Fcst", "WaveHeight", "SCALAR", 84, 96, 20, "all"),
        ("Fcst", "WaveHeight", "SCALAR", 96, 108, 20, "all"),

    ]

Delete_grids = [
        ("Fcst", "PoP", "SFC", "all", "all"),
        ("Fcst", "MaxT", "SFC", "all", "all"),
        ("Fcst", "MinT", "SFC", "all", "all"),
        ("Fcst", "T", "SFC", "all", "all"),
        ("Fcst", "Td", "SFC", "all", "all"),
        ("Fcst", "WindChill", "SFC", "all", "all"),
        ("Fcst", "HeatIndex", "SFC", "all", "all"),
        ("Fcst", "StormTotalSnow", "SFC", "all", "all"),
        ("Fcst", "SnowLevel", "SFC", "all", "all"),
        ("Fcst", "FzLevel", "SFC", "all", "all"),
        ("Fcst", "RH", "SFC", "all", "all"),
        ("Fcst", "Wind", "SFC", "all", "all"),
        ("Fcst", "Sky", "SFC", "all", "all"),
        ("Fcst", "WindGust", "SFC", "all", "all"),
        ("Fcst", "Wx", "SFC", "all", "all"),
        ("Fcst", "QPF", "SFC", "all", "all"),
        ("Fcst", "SnowAmt", "SFC", "all", "all"),
        ("Fcst", "IceAccum", "SFC", "all", "all"),

        ("Fcst", "MaxRH", "SFC", "all", "all"),
        ("Fcst", "MinRH", "SFC", "all", "all"),
        ("Fcst", "RH", "SFC", "all", "all"),
        ("Fcst", "TransWind", "SFC", "all", "all"),
        ("Fcst", "LAL", "SFC", "all", "all"),
        ("Fcst", "CWR", "SFC", "all", "all"),
        ("Fcst", "QPF", "SFC", "all", "all"),
        ("Fcst", "Haines", "SFC", "all", "all"),
        ("Fcst", "MixHgt", "SFC", "all", "all"),
        ("Fcst", "MarineLayer", "SFC", "all", "all"),
        ("Fcst", "Wind20ft", "SFC", "all", "all"),
        ("Fcst", "VentRate", "SFC", "all", "all"),
        ("Fcst", "Stability", "SFC", "all", "all"),
        ("Fcst", "HrsOfSun", "SFC", "all", "all"),
        ("Fcst", "DSI", "SFC", "all", "all"),

        ("Fcst", "Swell", "SFC", "all", "all"),
        ("Fcst", "Swell2", "SFC", "all", "all"),
        ("Fcst", "Period", "SFC", "all", "all"),
        ("Fcst", "Period2", "SFC", "all", "all"),
        ("Fcst", "WaveHeight", "SFC", "all", "all"),
        ("Fcst", "WindWaveHgt", "SFC", "all", "all"),
        
        ("Fcst", "Hazards", "SFC", "all", "all"),
        ("Fcst", "pwsD34", "SFC", "all", "all"),
        ("Fcst", "pwsN34", "SFC", "all", "all"),
        ("Fcst", "pwsD64", "SFC", "all", "all"),
        ("Fcst", "pwsN64", "SFC", "all", "all"),
        ]

Delete_grids_specific = [
        ("Fcst", "PoP", "SFC", -300, 300),
        ("Fcst", "MaxT", "SFC", -300, 300),
        ("Fcst", "MinT", "SFC", -300, 300),
        ("Fcst", "T", "SFC", -300, 300),
        ("Fcst", "Td", "SFC", -300, 300),
        ("Fcst", "WindChill", "SFC", -300, 300),
        ("Fcst", "HeatIndex", "SFC", -300, 300),
        ("Fcst", "StormTotalSnow", "SFC", -300, 300),
        ("Fcst", "SnowLevel", "SFC", -300, 300),
        ("Fcst", "FzLevel", "SFC", -300, 300),
        ("Fcst", "RH", "SFC", -300, 300),
        ("Fcst", "Wind", "SFC", -300, 300),
        ("Fcst", "Sky", "SFC", -300, 300),
        ("Fcst", "WindGust", "SFC", -300, 300),
        ("Fcst", "Wx", "SFC", -300, 300),
        ("Fcst", "QPF", "SFC", -300, 300),
        ("Fcst", "SnowAmt", "SFC", -300, 300),
        ("Fcst", "IceAccum", "SFC", -300, 300),

        ("Fcst", "MaxRH", "SFC", -300, 300),
        ("Fcst", "MinRH", "SFC", -300, 300),
        ("Fcst", "RH", "SFC", -300, 300),
        ("Fcst", "TransWind", "SFC", -300, 300),
        ("Fcst", "LAL", "SFC", -300, 300),
        ("Fcst", "CWR", "SFC", -300, 300),
        ("Fcst", "QPF", "SFC", -300, 300),
        ("Fcst", "Haines", "SFC", -300, 300),
        ("Fcst", "MixHgt", "SFC", -300, 300),
        ("Fcst", "MarineLayer", "SFC", -300, 300),
        ("Fcst", "Wind20ft", "SFC", -300, 300),
        ("Fcst", "VentRate", "SFC", -300, 300),
        ("Fcst", "Stability", "SFC", -300, 300),
        ("Fcst", "HrsOfSun", "SFC", -300, 300),
        ("Fcst", "DSI", "SFC", -300, 300),

        ("Fcst", "Swell", "SFC", -300, 300),
        ("Fcst", "Swell2", "SFC", -300, 300),
        ("Fcst", "Period", "SFC", -300, 300),
        ("Fcst", "Period2", "SFC", -300, 300),
        ("Fcst", "WaveHeight", "SFC", -300, 300),
        ("Fcst", "WindWaveHgt", "SFC", -300, 300),
        
        ("Fcst", "Hazards", "SFC", -300, 300),
        ]


scripts = [
    {    
    "name":"CreateGrids_Today",
    "commentary": "Create Grids starting Today",
    "productType": None,
    "createGrids": TestScript.general_createGrids,
    "gridsStartTime": "6am Local Today",
    "drtTime": "6am Local Today",
    },
    {    
    "name":"CreatePublicGrids_Today",
    "commentary": "Create Grids for All Products starting Today",
    "productType": None,
    "createGrids": Public_createGrids,
    "gridsStartTime": "6am Local Today",
    "drtTime": "6am Local Today",
    },
    {    
    "name":"CreateFireGrids_Today",
    "commentary": "Create Grids for All Products starting Today",
    "productType": None,
    "createGrids": Fire_createGrids,
    "gridsStartTime": "6am Local Today",
    "drtTime": "6am Local Today",
    },
    {    
    "name":"CreateMarineGrids_Today",
    "commentary": "Create Grids for All Products starting Today",
    "productType": None,
    "createGrids": Marine_createGrids,
    "gridsStartTime": "6am Local Today",
    "drtTime": "6am Local Today",
    },
    {    
    "name":"CreateHazardGrids_Today",
    "commentary": "Create Grids for All Products starting Today",
    "productType": None,
    "createGrids": Hazard_createGrids,
    "gridsStartTime": "6am Local Today",
    "drtTime": "6am Local Today",
    },
    {    
    "name":"DeleteGrids",
    "commentary": "Delete ALL Grids",
    "productType": None,
    "deleteGrids": Delete_grids,
    },
    {    
    "name":"DeleteGrids_Today",
    "commentary": "Delete Grids from -300 to 300",
    "productType": None,
    "deleteGrids": Delete_grids_specific,
    "gridsStartTime": "6am Local Today",
    "drtTime": "6am Local Today",
    },
    {    
    "name":"DeleteGrids_2010",
    "commentary": "Delete Grids from -300 to 300",
    "productType": None,
    "deleteGrids": Delete_grids_specific, 
    "gridsStartTime": "6am Local",
    "drtTime": "6am Local",
    },
    {    
    "name":"CreateGrids_2010",
    "commentary": "Create Grids starting in 2010",
    "productType": None,
    "createGrids": TestScript.general_createGrids,
    "gridsStartTime": "6am Local",
    "drtTime": "6am Local",
    },

    
    {    
    "name":"WxProb1",  
    "commentary": """
           To test the WxProb_QC_Tool (Spriggs, Barker)
           SChc RW -- SChc RW Areas F -- Areas F
           
        Quick Summary of Rules:
        --Probability terms stay probability after change (if any)
        --Coverage terms stay coverage after change (if any)
        --Non-PoP-related Wx always gets a "free pass" and is preserved as-is
        --PoP < 15:  Any PoP-related Wx becomes <NoWx>
        --PoP > 14 AND PoP-related Wx types are not present:  create a default Wx type (RW-)
        --Only "high" key and its equivalent values are changed unless PoP becomes
          less than coverage index's implied value
""",
    "productType": None,
    "createGrids": [
       # No RW where PoP < 15
       ("Fcst", "PoP", "SCALAR", 0, 12, 20, ["AboveElev"]),
       ("Fcst", "PoP", "SCALAR", 0, 12, 10, ["BelowElev"]),
       ("Fcst", "Wx", "WEATHER", 0, 12, "SChc:RW:-:<NoVis>:", "all"),

       # No RW where PoP < 15 -- Fog everywhere
       ("Fcst", "PoP", "SCALAR", 12, 24, 20, ["AboveElev"]),
       ("Fcst", "PoP", "SCALAR", 12, 24, 10, ["BelowElev"]),
       ("Fcst", "Wx", "WEATHER", 12, 24,
        "SChc:RW:-:<NoVis>:^Areas:F:<NoInten>:<NoVis>:", "all"),

       # RW where PoP > 15Fog everywhere
       ("Fcst", "PoP", "SCALAR", 24, 36, 20, ["AboveElev"]),
       ("Fcst", "PoP", "SCALAR", 24, 36, 10, ["BelowElev"]),
       ("Fcst", "Wx", "WEATHER", 24, 36,
        "Areas:F:<NoInten>:<NoVis>:", "all"),

       # RW where PoP > 15
       ("Fcst", "PoP", "SCALAR", 36, 48, 20, ["AboveElev"]),
       ("Fcst", "PoP", "SCALAR", 36, 48, 10, ["BelowElev"]),
       ("Fcst", "Wx", "WEATHER", 36, 48,
        "NoWx", "all"),
       
       # RW where PoP > 15, retain F and BS 
       ("Fcst", "PoP", "SCALAR", 48, 60, 20, ["AboveElev"]),
       ("Fcst", "PoP", "SCALAR", 48, 60, 10, ["BelowElev"]),
       ("Fcst", "Wx", "WEATHER", 48, 60,
        "Wide:F:+:1/4SM:^Def:BS:<NoInten>:1/4SM:", "all"),
       
       # RW where PoP > 15,  
       ("Fcst", "PoP", "SCALAR", 60, 72, 20, ["AboveElev"]),
       ("Fcst", "PoP", "SCALAR", 60, 72, 10, ["BelowElev"]),
       ("Fcst", "Wx", "WEATHER", 60, 72, 
        "Lkly:RW:-:<NoVis>:^Chc:T:<NoInten>:<NoVis>:^Wide:F:<NoInten>:1SM:", "all"),
       
       ],
    },
    ]

def testScript(self, dataMgr, level="Site"):
    time_6am = self.getAbsFromLocal(2010, 1, 1, 0, 0)
    todayTR = self.getTimeRange("Today")
    time_6am_today = todayTR.startTime()
    print("time", time_6am_today)
    for script in scripts:
        for entry in ["gridsStartTime", "drtTime"]:
            if script.get(entry, None) == "6am Local":
                script[entry] = time_6am
            elif script.get(entry, None) == "6am Local Today":
                script[entry] = time_6am_today
    return TestScript.generalTestScript(self, dataMgr, scripts, {}, level=level)


