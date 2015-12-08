# SSVF-Repositry-DQ-Processor
=================================================================================================
Latest Version: v1.22
Last Updated 12/8/2015

Author: David Katz-Wigmore
Company: Transition Projects Inc.

This program stream lines the processes of extracting HMIS client ID numbers from SSVF DQ reports.

Release Notes:
v.1.22--New Reporting Categories Update
Release Date: 12/08/2015
  What's New:
    Two new reporting categories, "VAMC Station Number" and "HP Screening Score", have been added to the Reporting
    Categories dropdown menu to keep the program up to date with the latest VA reporting requirements.

v.1.21--Minor Update
Release Date: 10/20/2015
  What's New:
      The column headings in the spreadsheet the program outputs now match the fields in ServicePoint, the HMIS 
      provider used in Portland, OR.  This change was entirely based upon user feedback and I would love to make 
      further updates to the program so that its output is the same as the HMIS fields used by every HMIS provider.  I
      can't do this without community input though so it is going on the back burner until people from outside the 
      Portland COC start using this program and providing feedback.

v.1.2--Back End Changes
Release Date: 7/15/2015
  What's New:
    Made numerous changes to the back end making the program usable by SSVF providers outside of Portland Oregon.
    I also did some clean up work on the code wrapping the GUI in a class and similar tasks that most people really 
    won't be interested in.  The end result is faster, cleaner code though which should make everone happy.

v1.11--Minor Update
Release Date: 7/14/2015

  What's New:
    Added "Very High Income (Entry)" and "Very High Income (Exit)" catagories to the dropdown menu.
    Cleaned up setup.py so that version information displays correctly in the compiled .exe

v1.1--Full Public Release
Release Date: 7/13/2015

  Added code documentation and increased regex efficiency with this release.
  
  There is still no internal testing in the code so that will be coming in a future release though I am quite
  confident that everything is working as it should based on the couple of times I used v1.0.
  
  At this point I'm releasing the program to the greater SSVF community.
  
  Please contact me with any issues you find in the software.  I hope this helps make those long VA .pdf files more o
  a usefull data quality tool.

v1.0--Full Release--Internal Only
Release Date: 04/11/2015

  All functionality is present in this version but the code is poorly documented and there are no internal tests.
  
