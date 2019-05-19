Feature: Search for Cbr

	Given I open Google.ru
	When I checked that the "search" field appeared
	And Input in the search field the value of the "Central Bank of Russia"
	And Clicked on the search button in google
	And Found the link “cbr.ru”
	And Clicked on the link "cbr.ru"
	And Checked that the desired site is open
	And Clicked on the link Internet reception
	And Opened the section "Write thanks"
	And In the field Your gratitude entered the value “some random text”
	And Put a tick “I agree”
	And Made a screenshot
	And Click on the “Three stripes” #(Top left that opens a menu)
	And Clicked on the about section
	And Clicked on the link warning
	And Remember the warning text
	And Changed the language of the page to en (top selection is)
	And Checked that the text is different from the previously memorized text
	Then Made a screenshot