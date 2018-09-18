# ---------------------------------------------------------------------
# This software is in the public domain, furnished "as is", without
# technical support, and with no warranty, express or implied, as to
# its usefulness for any purpose.
# ---------------------------------------------------------------------
##
# HighSeas
#
#  This file should not be edited by the site.
#  Site changes should go in HighSeas_Overrides for methods and
#       HighSeas_Definition to set up Product
#       Definition Settings.
#
# SOFTWARE HISTORY
#  Date        Ticket#    Engineer    Description
#  ----------- ---------- ----------- --------------------------
#  12/20/2017  DCS17686   tlefebvre   Initial baseline version.
#
##
# ---------------------------------------------------------------------

import HSF
import sys, copy, types, string

# Construct the names of the definition and override TextUtilities
siteDefinition = "HighSeas_AT2_Definition"
siteOverrides = "HighSeas_AT2_Overrides"

# Import the local site's Product Definition specifications
exec("import "+siteDefinition)

# Import the local site's Overrides
exec("import "+siteOverrides)

# Import Regional Overrides
#exec "import "+regionOverrides

# Patches
import Patch_Overrides


# These statements get the class object for the region and site overrides class
# The class and the module name (the file name) must be the same!

siteOverrides_object=sys.modules[siteOverrides].__dict__[siteOverrides]

# Get the region and site definitions into a known variable name
exec("localDefinition = " + siteDefinition + ".Definition")

class TextProduct(
                 siteOverrides_object,
                 Patch_Overrides.Patch_Overrides,
                 HSF.TextProduct
                ):
    Definition = copy.deepcopy(HSF.TextProduct.Definition)


    # Get the Site Definition Settings
    for key in list(localDefinition.keys()):
       Definition[key] = localDefinition[key]

    # Get the VariableList if overridden in Site
    try:
       exec("VariableList = "+siteDefinition+".VariableList")
    except:
       pass

    # Definition overrides should go in OFF_NH2_NT4 Definition
    # but may be put here for testing.
    # Most common would be the need to set a unique display name


    def __init__(self):
       HSF.TextProduct.__init__(self)
