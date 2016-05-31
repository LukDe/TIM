;(function () {
  'use strict'

	var Selection = {
		Search: 'TIM_LIST_PAGE_SEARCH',
		Offer: 'TIM_LIST_PAGE_OFFER',
	}

	var currentSelection = Selection.Search

	// Apply the callbacks when the document is ready.
	$(document).ready(function () {
		// On initialization.
		$('#tab-search').addClass('active')
		showTable(currentSelection)

		// Handlers for clicks on the tabs.
		$('#tab-search').click(function () {
			currentSelection = Selection.Search
			$(this).addClass('active')
			$('#tab-offer').removeClass('active')
			showTable(currentSelection)
		})

		$('#tab-offer').click(function () {
			currentSelection = Selection.Offer
			$(this).addClass('active')
			$('#tab-search').removeClass('active')
			showTable(currentSelection)
		})
	
	})

	function showTable (currentSelection) {
		switch (currentSelection) {
		case Selection.Search:
			$('#table-search').show()
			$('#table-offer').hide()
		break

		case Selection.Offer:
			$('#table-search').hide()
			$('#table-offer').show()
			break
			
		}
	}

})()
