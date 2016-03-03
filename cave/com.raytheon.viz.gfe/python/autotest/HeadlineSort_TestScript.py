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
# Headline Sorting
#
# Author:
# ----------------------------------------------------------------------------

scripts = [
    {
    "commentary": "Clear out all Hazards Table and Grids.",
    "name": "HeadlineSort_Init",
    "productType": None,
    "clearHazardsTable": 1,
    "checkStrings": [],
    },

# First set of tests for ROUTINE products (non-marine)

# need to generate the first event, so we can later test the NEW/CAN action
# grouping
    {
    "commentary": "Non-Marine Setup for action grouping - NEW/CAN, generating NEW event",
    "name": "HeadlineSort_nm1a",
    "drtTime": "20101203_0000",
    "gridsStartTime": "20101203_0000",
    "productType": "Hazard_NPW",
    "decodeVTEC": 1,
    "createGrids": [
       ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
       ("Fcst", "Hazards", "DISCRETE", 0, 36, "DS.W", ["FLZ139"]),
       ],
    "checkStrings": [
       "WWUS72 KTBW 030000",
       "NPWTBW",
       "URGENT - WEATHER MESSAGE",
       "National Weather Service Tampa Bay Ruskin FL",
       "700 PM EST Thu Dec 2 2010",
       "...|*Overview headline (must edit)*|...",
       ".|*Overview (must edit)*|.",
       "FLZ139-030800-",
       "/O.NEW.KTBW.DS.W.0001.101203T0000Z-101204T1200Z/",
       "Coastal Levy-",
       "700 PM EST Thu Dec 2 2010",
       "...DUST STORM WARNING IN EFFECT UNTIL 7 AM EST SATURDAY...",
       "The National Weather Service in Tampa Bay Ruskin has issued a Dust Storm Warning...which is in effect until 7 AM EST Saturday.",
#        "|* SEGMENT TEXT GOES HERE *|.",
       "A Dust Storm Warning means severely limited visibilities are expected with blowing dust. Travel could become extremely dangerous. Persons with respiratory problems should make preparations to stay indoors until the storm passes.",
       "$$",
       ],
    },

# downgrading DS.W to DU.Y will result in a NEW/CAN event for us to test
# the action grouping
    {
    "commentary": "Non-Marine Setup for action grouping - NEW/CAN, DS.W->DU.Y",
    "name": "HeadlineSort_nm1b",
    "drtTime": "20101203_0000",
    "gridsStartTime": "20101203_0000",
    "productType": "Hazard_NPW",
    "decodeVTEC": 0,
    "createGrids": [
       ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
       ("Fcst", "Hazards", "DISCRETE", 0, 36, "DU.Y", ["FLZ139"]),
       ],
    "checkStrings": [
       "WWUS72 KTBW 030000",
       "NPWTBW",
       "URGENT - WEATHER MESSAGE",
       "National Weather Service Tampa Bay Ruskin FL",
       "700 PM EST Thu Dec 2 2010",
       "...|*Overview headline (must edit)*|...",
       ".|*Overview (must edit)*|.",
       "FLZ139-030800-",
       "/O.CAN.KTBW.DS.W.0001.000000T0000Z-101204T1200Z/",
       "/O.NEW.KTBW.DU.Y.0001.101203T0000Z-101204T1200Z/",
       "Coastal Levy-",
       "700 PM EST Thu Dec 2 2010",
       "...BLOWING DUST ADVISORY IN EFFECT UNTIL 7 AM EST SATURDAY...",
       "...DUST STORM WARNING IS CANCELLED...",
       "The National Weather Service in Tampa Bay Ruskin has issued a Blowing Dust Advisory...which is in effect until 7 AM EST Saturday.",
#       "|*|* SEGMENT TEXT GOES HERE *|.*|",
       "A Blowing Dust Advisory means that blowing dust will restrict visibilities. Travelers are urged to use caution.",
       "$$",
       ],
    },

# Starting over with clean hazards task. Creating four events with different
# starting times to test the 2nd tier sort.
    {
    "commentary": "Non-Marine Setup for 2nd tier sort - NEW events with different start t",
    "name": "HeadlineSort_nm2",
    "drtTime": "20101203_0000",
    "gridsStartTime": "20101203_0000",
    "productType": "Hazard_NPW",
    "decodeVTEC": 1,
    "clearHazardsTable": 1,
    "createGrids": [
       ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
       ("Fcst", "Hazards", "DISCRETE", 0, 6, "HW.W", ["FLZ139"]),
       ("Fcst", "Hazards", "DISCRETE", 6, 9, "AF.Y", ["FLZ139"]),
       ("Fcst", "Hazards", "DISCRETE", 9, 36, "HT.Y", ["FLZ139"]),
       ],
    "checkStrings": [
       "WWUS72 KTBW 030000",
       "NPWTBW",
       "URGENT - WEATHER MESSAGE",
       "National Weather Service Tampa Bay Ruskin FL",
       "700 PM EST Thu Dec 2 2010",
       "...|*Overview headline (must edit)*|...",
       ".|*Overview (must edit)*|.",
       "FLZ139-030800-",
       "/O.NEW.KTBW.HW.W.0001.101203T0000Z-101203T0600Z/",
       "/O.NEW.KTBW.AF.Y.0001.101203T0600Z-101203T0900Z/",
       "/O.NEW.KTBW.HT.Y.0001.101203T0900Z-101204T1200Z/",
       "Coastal Levy-",
       "700 PM EST Thu Dec 2 2010",
       "...HIGH WIND WARNING IN EFFECT UNTIL 1 AM EST FRIDAY...",
       "...ASHFALL ADVISORY IN EFFECT FROM 1 AM TO 4 AM EST FRIDAY...",
       "...HEAT ADVISORY IN EFFECT FROM 4 AM FRIDAY TO 7 AM EST SATURDAY...",
       "The National Weather Service in Tampa Bay Ruskin has issued a High Wind Warning...which is in effect until 1 AM EST Friday. An Ashfall Advisory has also been issued. This Ashfall Advisory is in effect from 1 AM to 4 AM EST Friday. In addition...a Heat Advisory has been issued. This Heat Advisory is in effect from 4 AM Friday to 7 AM EST Saturday.",
#        "|* SEGMENT TEXT GOES HERE *|.",
       "A High Wind Warning means a hazardous high wind event is expected or occurring. Sustained wind speeds of at least 40 mph or gusts of 58 mph or more can lead to property damage.",
       "An Ashfall Advisory means that large amounts of ash will be deposited in the advisory area. Persons with respiratory illnesses should remain indoors to avoid inhaling the ash particles...and all persons outside should cover their mouth and nose with a mask or cloth.",
       "A Heat Advisory means that a period of hot temperatures is expected. The combination of hot temperatures and high humidity will combine to create a situation in which heat illnesses are possible. Drink plenty of fluids...stay in an air-conditioned room...stay out of the sun...and check up on relatives and neighbors.",
       "$$",
       ],
    },

# checking third tier sort, which is the action sort. We have three different
# NEW events and three different CON events.
    {
    "commentary": "Non-Marine Setup for 3rd tier sort - NEW/CON events",
    "name": "HeadlineSort_nm3",
    "drtTime": "20101203_0000",
    "gridsStartTime": "20101203_0000",
    "productType": "Hazard_NPW",
    "decodeVTEC": 0,
    "createGrids": [
       ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
       ("Fcst", "Hazards", "DISCRETE", 0, 6, "HW.W^FZ.W", ["FLZ139"]),
       ("Fcst", "Hazards", "DISCRETE", 6, 9, "AF.Y^EH.A", ["FLZ139"]),
       ("Fcst", "Hazards", "DISCRETE", 9, 36, "HT.Y^EC.A", ["FLZ139"]),
       ],
    "checkStrings": [
       "WWUS72 KTBW 030000",
       "NPWTBW",
       "URGENT - WEATHER MESSAGE",
       "National Weather Service Tampa Bay Ruskin FL",
       "700 PM EST Thu Dec 2 2010",
       "...|*Overview headline (must edit)*|...",
       ".|*Overview (must edit)*|.",
       "FLZ139-030800-",
       "/O.NEW.KTBW.FZ.W.0001.101203T0000Z-101203T0600Z/",
       "/O.NEW.KTBW.EH.A.0001.101203T0600Z-101203T0900Z/",
       "/O.NEW.KTBW.EC.A.0001.101203T0900Z-101204T1200Z/",
       "/O.CON.KTBW.HW.W.0001.000000T0000Z-101203T0600Z/",
       "/O.CON.KTBW.AF.Y.0001.101203T0600Z-101203T0900Z/",
       "/O.CON.KTBW.HT.Y.0001.101203T0900Z-101204T1200Z/",
       "Coastal Levy-",
       "700 PM EST Thu Dec 2 2010",
       "...FREEZE WARNING IN EFFECT UNTIL 1 AM EST FRIDAY...",
       "...HIGH WIND WARNING REMAINS IN EFFECT UNTIL 1 AM EST FRIDAY...",
       "...EXCESSIVE HEAT WATCH IN EFFECT FROM 1 AM TO 4 AM EST FRIDAY...",
       "...ASHFALL ADVISORY REMAINS IN EFFECT FROM 1 AM TO 4 AM EST FRIDAY...",
       "...EXTREME COLD WATCH IN EFFECT FROM 4 AM EST FRIDAY THROUGH SATURDAY MORNING...",
       "...HEAT ADVISORY REMAINS IN EFFECT FROM 4 AM FRIDAY TO 7 AM EST SATURDAY...",
       "The National Weather Service in Tampa Bay Ruskin has issued a Freeze Warning...which is in effect until 1 AM EST Friday. An Excessive Heat Watch has also been issued. This Excessive Heat Watch is in effect from 1 AM to 4 AM EST Friday. In addition...an Extreme Cold Watch has been issued. This Extreme Cold Watch is in effect from 4 AM EST Friday through Saturday morning.",
#        "|* SEGMENT TEXT GOES HERE *|.",
       "A High Wind Warning means a hazardous high wind event is expected or occurring. Sustained wind speeds of at least 40 mph or gusts of 58 mph or more can lead to property damage.",
       "An Ashfall Advisory means that large amounts of ash will be deposited in the advisory area. Persons with respiratory illnesses should remain indoors to avoid inhaling the ash particles...and all persons outside should cover their mouth and nose with a mask or cloth.",
       "A Heat Advisory means that a period of hot temperatures is expected. The combination of hot temperatures and high humidity will combine to create a situation in which heat illnesses are possible. Drink plenty of fluids...stay in an air-conditioned room...stay out of the sun...and check up on relatives and neighbors.",
       "A Freeze Warning means sub-freezing temperatures are imminent or highly likely. These conditions will kill crops and other sensitive vegetation.",
       "An Excessive Heat Watch means that a prolonged period of hot temperatures is expected. The combination of hot temperatures and high humidity will combine to create a DANGEROUS SITUATION in which heat illnesses are possible. Drink plenty of fluids...stay in an air-conditioned room...stay out of the sun...and check up on relatives and neighbors.",
       "An Extreme Cold Watch means that prolonged periods of very cold temperatures are expected. Ensure that outdoor animals have warm shelter...and that children wear a hat and gloves.",
       "$$",
       ],
    },

# Starting with clean hazards table. Three events all NEW, with same start
# time, sorted by significance.
    {
    "commentary": "Non-Marine Setup for 4th tier sort - significance",
    "name": "HeadlineSort_nm4",
    "drtTime": "20101203_0000",
    "gridsStartTime": "20101203_0000",
    "productType": "Hazard_NPW",
    "decodeVTEC": 0,
    "clearHazardsTable": 1,
    "createGrids": [
       ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
       ("Fcst", "Hazards", "DISCRETE", 0, 36, "EC.W^SM.Y^HW.A", ["FLZ139"]),
       ],
    "checkStrings": [
       "WWUS72 KTBW 030000",
       "NPWTBW",
       "URGENT - WEATHER MESSAGE",
       "National Weather Service Tampa Bay Ruskin FL",
       "700 PM EST Thu Dec 2 2010",
       "...|*Overview headline (must edit)*|...",
       ".|*Overview (must edit)*|.",
       "FLZ139-030800-",
       "/O.NEW.KTBW.EC.W.0001.101203T0000Z-101204T1200Z/",
       "/O.NEW.KTBW.SM.Y.0001.101203T0000Z-101204T1200Z/",
       "/O.NEW.KTBW.HW.A.0001.101203T0000Z-101204T1200Z/",
       "Coastal Levy-",
       "700 PM EST Thu Dec 2 2010",
       "...EXTREME COLD WARNING IN EFFECT UNTIL 7 AM EST SATURDAY...",
       "...DENSE SMOKE ADVISORY IN EFFECT UNTIL 7 AM EST SATURDAY...",
       "...HIGH WIND WATCH IN EFFECT THROUGH SATURDAY MORNING...",
       "The National Weather Service in Tampa Bay Ruskin has issued an Extreme Cold Warning...which is in effect until 7 AM EST Saturday. A Dense Smoke Advisory has also been issued. This Dense Smoke Advisory is in effect until 7 AM EST Saturday. In addition...a High Wind Watch has been issued. This High Wind Watch is in effect through Saturday morning.",
#        "|* SEGMENT TEXT GOES HERE *|.",
       "An Extreme Cold Warning means that dangerously low temperatures are expected for a prolonged period of time. Frostbite and hypothermia are likely if exposed to these temperatures...so make sure a hat...facemask...and heavy gloves or mittens are available.",
       "A Dense Smoke Advisory means widespread fires will create smoke...limiting visibilities. If driving...slow down...use your headlights...and leave plenty of distance ahead of you in case a sudden stop is needed.",
       "A High Wind Watch means there is the potential for a hazardous high wind event. Sustained winds of at least 40 mph...or gusts of 58 mph or stronger may occur. Continue to monitor the latest forecasts.",
       "$$",
       ],
    },

# Starting with clean hazards table. Three events all NEW, with same start
# time, same significance, sorted by alpha phenomena.
    {
    "commentary": "Non-Marine Setup for 5th tier sort - alphabetical phenomena",
    "name": "HeadlineSort_nm5",
    "drtTime": "20101203_0000",
    "gridsStartTime": "20101203_0000",
    "productType": "Hazard_NPW",
    "decodeVTEC": 0,
    "clearHazardsTable": 1,
    "createGrids": [
       ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
       ("Fcst", "Hazards", "DISCRETE", 0, 36, "AS.Y^AF.Y^WI.Y", ["FLZ139"]),
       ],
    "checkStrings": [
       "WWUS72 KTBW 030000",
       "NPWTBW",
       "URGENT - WEATHER MESSAGE",
       "National Weather Service Tampa Bay Ruskin FL",
       "700 PM EST Thu Dec 2 2010",
       "...|*Overview headline (must edit)*|...",
       ".|*Overview (must edit)*|.",
       "FLZ139-030800-",
       "/O.NEW.KTBW.AF.Y.0001.101203T0000Z-101204T1200Z/",
       "/O.NEW.KTBW.AS.Y.0001.101203T0000Z-101204T1200Z/",
       "/O.NEW.KTBW.WI.Y.0001.101203T0000Z-101204T1200Z/",
       "Coastal Levy-",
       "700 PM EST Thu Dec 2 2010",
       "...ASHFALL ADVISORY IN EFFECT UNTIL 7 AM EST SATURDAY...",
       "...AIR STAGNATION ADVISORY IN EFFECT UNTIL 7 AM EST SATURDAY...",
       "...WIND ADVISORY IN EFFECT UNTIL 7 AM EST SATURDAY...",
       "The National Weather Service in Tampa Bay Ruskin has issued an Air Stagnation Advisory...which is in effect until 7 AM EST Saturday. An Ashfall Advisory has also been issued. This Ashfall Advisory is in effect until 7 AM EST Saturday. In addition...a Wind Advisory has been issued. This Wind Advisory is in effect until 7 AM EST Saturday.",
#        "|* SEGMENT TEXT GOES HERE *|.",
       "An Air Stagnation Advisory indicates that due to limited movement of an air mass across the advisory area...pollution will increase to dangerous levels. Persons with respiratory illness should follow their physicians advice for dealing with high levels of air pollution.",
       "An Ashfall Advisory means that large amounts of ash will be deposited in the advisory area. Persons with respiratory illnesses should remain indoors to avoid inhaling the ash particles...and all persons outside should cover their mouth and nose with a mask or cloth.",
       "A Wind Advisory means that winds of 35 mph are expected. Winds this strong can make driving difficult...especially for high profile vehicles. Use extra caution.",
       "$$",
       ],
    },

# Second set of tests for MARINE products

# Starting over with clean hazards task. Creating four events with different
# starting times to test the 1st tier sort.
    {
    "commentary": "1st tier marine sort - events by starting time",
    "name": "HeadlineSort_m1",
    "drtTime": "20101203_0000",
    "gridsStartTime": "20101203_0000",
    "productType": "NSH",
    "decodeVTEC": 1,
    "comboFlag": 1,
    "combinations": [(["GMZ830"], "")],
    "cmdLineVars": "{('Product Issuance', 'productIssuance'): '430 AM', ('Issued By', 'issuedBy'): None}",
    "clearHazardsTable": 1,
    "createGrids": [
       ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
       ("Fcst", "Hazards", "DISCRETE", 3, 24, "SC.Y", ["GMZ830"]),
       ("Fcst", "Hazards", "DISCRETE", 27, 48, "SC.Y", ["GMZ830"]),
       ("Fcst", "Hazards", "DISCRETE", 51, 72, "SC.Y", ["GMZ830"]),
       ("Fcst", "Hazards", "DISCRETE", 75, 96, "SC.Y", ["GMZ830"]),
       ],
    "checkStrings": [
       "UFUS42 KTBW 030000",
       "NSHABC",
       "Nearshore Marine Forecast for Florida",
       "National Weather Service Tampa Bay Ruskin FL",
       "700 PM EST Thu Dec 2 2010",
       "For waters within five nautical miles of shore on Lake (name)",
       "GMZ830-030100-",
#       "/O.NEW.KTBW.SC.Y.0001.101203T0300Z-101204T0000Z/",
#       "/O.NEW.KTBW.SC.Y.0002.101204T0300Z-101205T0000Z/",
#       "/O.NEW.KTBW.SC.Y.0003.101205T0300Z-101206T0000Z/",
#       "/O.NEW.KTBW.SC.Y.0004.101206T0300Z-101207T0000Z/",
       "Tampa Bay waters-",
       "700 PM EST Thu Dec 2 2010",
       "...SMALL CRAFT ADVISORY IN EFFECT FROM 10 PM EST THIS EVENING THROUGH FRIDAY EVENING...",
       "...SMALL CRAFT ADVISORY IN EFFECT FROM FRIDAY EVENING THROUGH SATURDAY EVENING...",
       "...SMALL CRAFT ADVISORY IN EFFECT FROM SATURDAY EVENING THROUGH SUNDAY EVENING...",
       "...SMALL CRAFT ADVISORY IN EFFECT FROM SUNDAY EVENING THROUGH MONDAY EVENING...",
       "$$",
       ],
    },

    {
    "commentary": "Setup for 2nd tier marine sort - by action code",
    "name": "HeadlineSort_m2a",
    "drtTime": "20101203_0000",
    "gridsStartTime": "20101203_0000",
    "productType": "NSH",
    "decodeVTEC": 1,
    "clearHazardsTable": 1,
    "comboFlag": 1,
    "combinations": [(["GMZ830"], "")],
    "cmdLineVars": "{('Product Issuance', 'productIssuance'): '430 AM', ('Issued By', 'issuedBy'): None}",
    "createGrids": [
       ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
       ("Fcst", "Hazards", "DISCRETE", 3, 24, "SC.Y^MF.Y", ["GMZ830"]),
       ],
    "checkStrings": [
       "UFUS42 KTBW 030000",
       "NSHABC",
       "Nearshore Marine Forecast for Florida",
       "National Weather Service Tampa Bay Ruskin FL",
       "700 PM EST Thu Dec 2 2010",
       "For waters within five nautical miles of shore on Lake (name)",
       "GMZ830-030100-",
#       "/O.NEW.KTBW.MF.Y.0001.101203T0300Z-101204T0000Z/",
#       "/O.NEW.KTBW.SC.Y.0001.101203T0300Z-101204T0000Z/",
       "Tampa Bay waters-",
       "700 PM EST Thu Dec 2 2010",
       "...DENSE FOG ADVISORY IN EFFECT FROM 10 PM THIS EVENING TO 7 PM EST FRIDAY...",
       "...SMALL CRAFT ADVISORY IN EFFECT FROM 10 PM EST THIS EVENING THROUGH FRIDAY EVENING...",
       "$$",
       ],
    },

    {
    "commentary": "Setup for 2nd tier marine sort - by action code",
    "name": "HeadlineSort_m2b",
    "drtTime": "20101203_0000",
    "gridsStartTime": "20101203_0000",
    "productType": "NSH",
    "decodeVTEC": 1,
    "comboFlag": 1,
    "combinations": [(["GMZ830"], "")],
    "cmdLineVars": "{('Product Issuance', 'productIssuance'): '430 AM', ('Issued By', 'issuedBy'): None}",
    "createGrids": [
       ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
       ("Fcst", "Hazards", "DISCRETE", 3, 24, "SC.Y^MF.Y^UP.Y", ["GMZ830"]),
       ],
    "checkStrings": [
       "UFUS42 KTBW 030000",
       "NSHABC",
       "Nearshore Marine Forecast for Florida",
       "National Weather Service Tampa Bay Ruskin FL",
       "700 PM EST Thu Dec 2 2010",
       "For waters within five nautical miles of shore on Lake (name)",
       "GMZ830-030100-",
#       "/O.NEW.KTBW.UP.Y.0001.101203T0300Z-101204T0000Z/",
#       "/O.CON.KTBW.MF.Y.0001.101203T0300Z-101204T0000Z/",
#       "/O.CON.KTBW.SC.Y.0001.101203T0300Z-101204T0000Z/",
       "Tampa Bay waters-",
       "700 PM EST Thu Dec 2 2010",
       "...FREEZING SPRAY ADVISORY IN EFFECT FROM 10 PM EST THIS EVENING THROUGH FRIDAY EVENING...",
       "...DENSE FOG ADVISORY REMAINS IN EFFECT FROM 10 PM THIS EVENING TO 7 PM EST FRIDAY...",
       "...SMALL CRAFT ADVISORY REMAINS IN EFFECT FROM 10 PM EST THIS EVENING THROUGH FRIDAY EVENING...",
       "$$",
       ],
    },

# checking third tier sort, which is significance.  Start over with NEW events.
    {
    "commentary": "Setup for 3rd tier marine sort - significance",
    "name": "HeadlineSort_m3",
    "drtTime": "20101203_0000",
    "gridsStartTime": "20101203_0000",
    "productType": "NSH",
    "decodeVTEC": 0,
    "comboFlag": 1,
    "combinations": [(["GMZ830"], "")],
    "cmdLineVars": "{('Product Issuance', 'productIssuance'): '430 AM', ('Issued By', 'issuedBy'): None}",
    "clearHazardsTable": 1,
    "createGrids": [
       ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
       ("Fcst", "Hazards", "DISCRETE", 0, 36, "UP.W^SI.Y^TO.A:121", ["GMZ830"]),
       ],
    "checkStrings": [
       "UFUS42 KTBW 030000",
       "NSHABC",
       "Nearshore Marine Forecast for Florida",
       "National Weather Service Tampa Bay Ruskin FL",
       "700 PM EST Thu Dec 2 2010",
       "For waters within five nautical miles of shore on Lake (name)",
       "GMZ830-030100-",
#       "/O.NEW.KTBW.UP.W.0001.101203T0000Z-101204T1200Z/",
#       "/O.NEW.KTBW.SI.Y.0001.101203T0000Z-101204T1200Z/",
#       "/O.NEW.KTBW.TO.A.0121.101203T0000Z-101204T1200Z/",
       "Tampa Bay waters-",
       "700 PM EST Thu Dec 2 2010",
       "...HEAVY FREEZING SPRAY WARNING IN EFFECT THROUGH SATURDAY MORNING...",
       "...SMALL CRAFT ADVISORY FOR WINDS IN EFFECT THROUGH SATURDAY MORNING...",
       "...TORNADO WATCH 121 IN EFFECT UNTIL 7 AM EST SATURDAY...",
       "$$",
       ],
    },

# Starting with clean hazards table. Three events all NEW, with same start
# time, same significance, ordered by alpha pheonmena
    {
    "commentary": "Setup for 4th tier marine sort - alpha pheonmena",
    "name": "HeadlineSort_m4",
    "drtTime": "20101203_0000",
    "gridsStartTime": "20101203_0000",
    "productType": "NSH",
    "decodeVTEC": 0,
    "comboFlag": 1,
    "combinations": [(["GMZ830"], "")],
    "cmdLineVars": "{('Product Issuance', 'productIssuance'): '430 AM', ('Issued By', 'issuedBy'): None}",
    "clearHazardsTable": 1,
    "createGrids": [
       ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
       ("Fcst", "Hazards", "DISCRETE", 0, 36, "MF.Y^BW.Y^MS.Y", ["GMZ830"]),
       ],
    "checkStrings": [
       "UFUS42 KTBW 030000",
       "NSHABC",
       "Nearshore Marine Forecast for Florida",
       "National Weather Service Tampa Bay Ruskin FL",
       "700 PM EST Thu Dec 2 2010",
       "For waters within five nautical miles of shore on Lake (name)",
       "GMZ830-030100-",
#       "/O.NEW.KTBW.BW.Y.0001.101203T0000Z-101204T1200Z/",
#       "/O.NEW.KTBW.MF.Y.0001.101203T0000Z-101204T1200Z/",
#       "/O.NEW.KTBW.MS.Y.0001.101203T0000Z-101204T1200Z/",
       "Tampa Bay waters-",
       "700 PM EST Thu Dec 2 2010",
       "...BRISK WIND ADVISORY IN EFFECT THROUGH SATURDAY MORNING...",
       "...DENSE FOG ADVISORY IN EFFECT UNTIL 7 AM EST SATURDAY...",
       "...DENSE SMOKE ADVISORY IN EFFECT UNTIL 7 AM EST SATURDAY...",
       "$$",
       ],
    },

# Second set of tests for MARINE products

# Starting over with clean hazards task. Creating four events with different
# starting times to test the 1st tier sort.
    {
    "commentary": "1st tier marine sort - events by starting time",
    "name": "HeadlineSort_mww1",
    "drtTime": "20101203_0000",
    "gridsStartTime": "20101203_0000",
    "productType": "Hazard_MWW",
    "decodeVTEC": 1,
    "comboFlag": 1,
    "combinations": [(["GMZ830"], "")],
    "cmdLineVars": "{('Product Issuance', 'productIssuance'): 'Morning', ('Issued By', 'issuedBy'): None}",
    "clearHazardsTable": 1,
    "createGrids": [
       ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
       ("Fcst", "Hazards", "DISCRETE", 3, 24, "SC.Y", ["GMZ830"]),
       ("Fcst", "Hazards", "DISCRETE", 27, 48, "SC.Y", ["GMZ830"]),
       ("Fcst", "Hazards", "DISCRETE", 51, 72, "SC.Y", ["GMZ830"]),
       ("Fcst", "Hazards", "DISCRETE", 75, 96, "SC.Y", ["GMZ830"]),
       ],
    "checkStrings": [
      "WHUS72 KTBW 030000",
      "MWWTBW",
      "URGENT - MARINE WEATHER MESSAGE",
      "National Weather Service Tampa Bay Ruskin FL",
      "700 PM EST Thu Dec 2 2010",
      "...|*Overview headline (must edit)*|...",
      ".|*Overview (must edit)*|.",
      "GMZ830-030800-",
      "/O.NEW.KTBW.SC.Y.0001.101203T0300Z-101204T0000Z/",
      "/O.NEW.KTBW.SC.Y.0002.101204T0300Z-101205T0000Z/",
      "/O.NEW.KTBW.SC.Y.0003.101205T0300Z-101206T0000Z/",
      "/O.NEW.KTBW.SC.Y.0004.101206T0300Z-101207T0000Z/",
      "Tampa Bay waters-",
      "700 PM EST Thu Dec 2 2010",
      "...SMALL CRAFT ADVISORY IN EFFECT FROM 10 PM THIS EVENING TO 7 PM EST FRIDAY...",
      "...SMALL CRAFT ADVISORY IN EFFECT FROM 10 PM FRIDAY TO 7 PM EST SATURDAY...",
      "...SMALL CRAFT ADVISORY IN EFFECT FROM 10 PM SATURDAY TO 7 PM EST SUNDAY...",
      "...SMALL CRAFT ADVISORY IN EFFECT FROM 10 PM SUNDAY TO 7 PM EST MONDAY...",
#      "The National Weather Service in Tampa Bay Ruskin has issued a Small Craft Advisory...which is in effect from 10 PM this evening to 7 PM EST Friday. A Small Craft Advisory has also been issued. This Small Craft Advisory is in effect from 10 PM Friday to 7 PM EST Saturday. In addition...a Small Craft Advisory has been issued. This Small Craft Advisory is in effect from 10 PM Saturday to 7 PM EST Sunday. In addition...a Small Craft Advisory has been issued. This Small Craft Advisory is in effect from 10 PM Sunday to 7 PM EST Monday.",
#       "|* SEGMENT TEXT GOES HERE *|.",
      "PRECAUTIONARY/PREPAREDNESS ACTIONS...",
      "A Small Craft Advisory means that wind speeds of 21 to 33 knots are expected to produce hazardous wave conditions to small craft. Inexperienced mariners...especially those operating smaller vessels should avoid navigating in these conditions.",
      "&&",
      "$$",
       ],
    },

    {
    "commentary": "Setup for 2nd tier marine sort - by action code",
    "name": "HeadlineSort_mww2a",
    "drtTime": "20101203_0000",
    "gridsStartTime": "20101203_0000",
    "productType": "Hazard_MWW",
    "decodeVTEC": 1,
    "clearHazardsTable": 1,
    "comboFlag": 1,
    "combinations": [(["GMZ830"], "")],
    "cmdLineVars": "{('Product Issuance', 'productIssuance'): 'Morning', ('Issued By', 'issuedBy'): None}",
    "createGrids": [
       ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
       ("Fcst", "Hazards", "DISCRETE", 3, 24, "SC.Y^MF.Y", ["GMZ830"]),
       ],
    "checkStrings": [
       "WHUS72 KTBW 030000",
       "MWWTBW",
       "URGENT - MARINE WEATHER MESSAGE",
       "National Weather Service Tampa Bay Ruskin FL",
       "700 PM EST Thu Dec 2 2010",
       "...|*Overview headline (must edit)*|...",
       ".|*Overview (must edit)*|.",
       "GMZ830-030800-",
       "/O.NEW.KTBW.MF.Y.0001.101203T0300Z-101204T0000Z/",
       "/O.NEW.KTBW.SC.Y.0001.101203T0300Z-101204T0000Z/",
       "Tampa Bay waters-",
       "700 PM EST Thu Dec 2 2010",
       "...DENSE FOG ADVISORY IN EFFECT FROM 10 PM THIS EVENING TO 7 PM EST FRIDAY...",
       "...SMALL CRAFT ADVISORY IN EFFECT FROM 10 PM THIS EVENING TO 7 PM EST FRIDAY...",
       "The National Weather Service in Tampa Bay Ruskin has issued a Dense Fog Advisory...which is in effect from 10 PM this evening to 7 PM EST Friday. A Small Craft Advisory has also been issued. This Small Craft Advisory is in effect from 10 PM this evening to 7 PM EST Friday.",
#        "|* SEGMENT TEXT GOES HERE *|.",
       "PRECAUTIONARY/PREPAREDNESS ACTIONS...",
       "A Dense Fog Advisory means visibilities will frequently be reduced to less than one mile. Inexperienced mariners...especially those operating smaller vessels should avoid navigating in these conditions.",
       "A Small Craft Advisory means that wind speeds of 21 to 33 knots are expected to produce hazardous wave conditions to small craft. Inexperienced mariners...especially those operating smaller vessels should avoid navigating in these conditions.",
       "&&",
       "$$",
       ],
    },

    {
    "commentary": "Setup for 2nd tier marine sort - by action code",
    "name": "HeadlineSort_mww2b",
    "drtTime": "20101203_0000",
    "gridsStartTime": "20101203_0000",
    "productType": "Hazard_MWW_Local",
    "decodeVTEC": 1,
    "comboFlag": 1,
    "combinations": [(["GMZ830"], "")],
    "cmdLineVars": "{('Product Issuance', 'productIssuance'): 'Morning', ('Issued By', 'issuedBy'): None}",
    "createGrids": [
       ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
       ("Fcst", "Hazards", "DISCRETE", 3, 24, "SC.Y^MF.Y^UP.Y", ["GMZ830"]),
       ],
    "checkStrings": [
       "WHUS72 KTBW 030000",
       "MWWTBW",
       "URGENT - MARINE WEATHER MESSAGE",
       "National Weather Service Tampa Bay Ruskin FL",
       "700 PM EST Thu Dec 2 2010",
       "...|*Overview headline (must edit)*|...",
       ".|*Overview (must edit)*|.",
       "GMZ830-030800-",
       "/O.NEW.KTBW.UP.Y.0001.101203T0300Z-101204T0000Z/",
       "/O.CON.KTBW.MF.Y.0001.101203T0300Z-101204T0000Z/",
       "/O.CON.KTBW.SC.Y.0001.101203T0300Z-101204T0000Z/",
       "Tampa Bay waters-",
       "700 PM EST Thu Dec 2 2010",
       "...FREEZING SPRAY ADVISORY IN EFFECT FROM 10 PM THIS EVENING TO 7 PM EST FRIDAY...",
       "...DENSE FOG ADVISORY REMAINS IN EFFECT FROM 10 PM THIS EVENING TO 7 PM EST FRIDAY...",
       "...SMALL CRAFT ADVISORY REMAINS IN EFFECT FROM 10 PM THIS EVENING TO 7 PM EST FRIDAY...",
       "The National Weather Service in Tampa Bay Ruskin has issued a Freezing Spray Advisory...which is in effect from 10 PM this evening to 7 PM EST Friday.",
#       "|* SEGMENT TEXT GOES HERE *|.",
       "PRECAUTIONARY/PREPAREDNESS ACTIONS...",
       "A Dense Fog Advisory means visibilities will frequently be reduced to less than one mile. Inexperienced mariners...especially those operating smaller vessels should avoid navigating in these conditions.",
       "A Small Craft Advisory means that wind speeds of 21 to 33 knots are expected to produce hazardous wave conditions to small craft. Inexperienced mariners...especially those operating smaller vessels should avoid navigating in these conditions.",
       "A Freezing Spray Advisory means that light to moderate accumulation of ice is expected on vessels. Operating a vessel in freezing spray can be hazardous. It is recommended that vessels be prepared to take appropriate counter measures before putting to sea or enter the advisory area.",
       "&&",
       "$$",
       ],
    },

# checking third tier sort, which is significance.  Start over with NEW events.
    {
    "commentary": "Setup for 3rd tier marine sort - significance",
    "name": "HeadlineSort_mww3",
    "drtTime": "20101203_0000",
    "gridsStartTime": "20101203_0000",
    "productType": "Hazard_MWW",
    "decodeVTEC": 0,
    "comboFlag": 1,
    "combinations": [(["GMZ830"], "")],
    "cmdLineVars": "{('Product Issuance', 'productIssuance'): 'Morning', ('Issued By', 'issuedBy'): None}",
    "clearHazardsTable": 1,
    "createGrids": [
       ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
       ("Fcst", "Hazards", "DISCRETE", 0, 36, "UP.W^SI.Y^TO.A:121", ["GMZ830"]),
       ],
    "checkStrings": [
       "WHUS72 KTBW 030000",
       "MWWTBW",
       "URGENT - MARINE WEATHER MESSAGE",
       "National Weather Service Tampa Bay Ruskin FL",
       "700 PM EST Thu Dec 2 2010",
       "...|*Overview headline (must edit)*|...",
       ".|*Overview (must edit)*|.",
       "GMZ830-030800-",
       "/O.NEW.KTBW.UP.W.0001.101203T0000Z-101204T1200Z/",
       "/O.NEW.KTBW.SI.Y.0001.101203T0000Z-101204T1200Z/",
       "Tampa Bay waters-",
       "700 PM EST Thu Dec 2 2010",
       "...HEAVY FREEZING SPRAY WARNING IN EFFECT UNTIL 7 AM EST SATURDAY...",
       "...SMALL CRAFT ADVISORY FOR WINDS IN EFFECT UNTIL 7 AM EST SATURDAY...",
       "The National Weather Service in Tampa Bay Ruskin has issued a Heavy Freezing Spray Warning...which is in effect until 7 AM EST Saturday. A Small Craft Advisory for winds has also been issued. This Small Craft Advisory for winds is in effect until 7 AM EST Saturday.",
#        "|* SEGMENT TEXT GOES HERE *|.",
       "PRECAUTIONARY/PREPAREDNESS ACTIONS...",
       "A Small Craft Advisory for wind means that wind speeds of 21 to 33 knots are expected. Inexperienced mariners...especially those operating smaller vessels should avoid navigating in these conditions.",
       "&&",
       "$$",
       ],
    },

# Starting with clean hazards table. Three events all NEW, with same start
# time, same significance, ordered by alpha pheonmena
    {
    "commentary": "Setup for 4th tier marine sort - alpha pheonmena",
    "name": "HeadlineSort_mww4",
    "drtTime": "20101203_0000",
    "gridsStartTime": "20101203_0000",
    "productType": "Hazard_MWW",
    "decodeVTEC": 0,
    "comboFlag": 1,
    "combinations": [(["GMZ830"], "")],
    "cmdLineVars": "{('Product Issuance', 'productIssuance'): 'Morning', ('Issued By', 'issuedBy'): None}",
    "clearHazardsTable": 1,
    "createGrids": [
       ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
       ("Fcst", "Hazards", "DISCRETE", 0, 36, "UP.Y^MS.Y^BW.Y", ["GMZ830"]),
       ],
    "checkStrings": [
       "WHUS72 KTBW 030000",
       "MWWTBW",
       "URGENT - MARINE WEATHER MESSAGE",
       "National Weather Service Tampa Bay Ruskin FL",
       "700 PM EST Thu Dec 2 2010",
       "...|*Overview headline (must edit)*|...",
       ".|*Overview (must edit)*|.",
       "GMZ830-030800-",
       "/O.NEW.KTBW.BW.Y.0001.101203T0000Z-101204T1200Z/",
       "/O.NEW.KTBW.MS.Y.0001.101203T0000Z-101204T1200Z/",
       "/O.NEW.KTBW.UP.Y.0001.101203T0000Z-101204T1200Z/",
       "Tampa Bay waters-",
       "700 PM EST Thu Dec 2 2010",
       "...BRISK WIND ADVISORY IN EFFECT UNTIL 7 AM EST SATURDAY...",
       "...DENSE SMOKE ADVISORY IN EFFECT UNTIL 7 AM EST SATURDAY...",
       "...FREEZING SPRAY ADVISORY IN EFFECT UNTIL 7 AM EST SATURDAY...",
       "The National Weather Service in Tampa Bay Ruskin has issued a Brisk Wind Advisory...which is in effect until 7 AM EST Saturday. A Dense Smoke Advisory has also been issued. This Dense Smoke Advisory is in effect until 7 AM EST Saturday. In addition...a Freezing Spray Advisory has been issued. This Freezing Spray Advisory is in effect until 7 AM EST Saturday.",
#        "|* SEGMENT TEXT GOES HERE *|.",
       "PRECAUTIONARY/PREPAREDNESS ACTIONS...",
       "A Brisk Wind Advisory means that winds will reach Small Craft Advisory criteria in areas that are primarily ice covered. Moving ice floes could damage small craft.",
       "A Dense Smoke Advisory means widespread fires will create smoke...limiting visibilities. Inexperienced mariners...especially those operating smaller vessels should avoid navigating in these conditions.",
       "A Freezing Spray Advisory means that light to moderate accumulation of ice is expected on vessels. Operating a vessel in freezing spray can be hazardous. It is recommended that vessels be prepared to take appropriate counter measures before putting to sea or enter the advisory area.",
       "&&",
       "$$",
       ],
    },

    {
    "commentary": "Deleting hazard grids.",
    "name": "HeadlineSort_4c",
    "productType": None,
    "clearHazardsTable": 1,
    "checkStrings": [],
    },

    ]

       
import TestScript
def testScript(self, dataMgr):
    defaults = {
        "database": "<site>_GRID__Fcst_00000000_0000",
        "publishGrids": 0,
        "decodeVTEC": 0,
        "gridsStartTime": "20100101_0500",
        "orderStrings": 1,
        "vtecMode": "O",
        "comboFlag": 0,
        "deleteGrids": [("Fcst", "Hazards", "SFC", "all", "all")],
        }
    return TestScript.generalTestScript(self, dataMgr, scripts, defaults)




