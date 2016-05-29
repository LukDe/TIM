;(function () {
  'use strict'

	var Selection = {
		Search: 'TIM_LIST_PAGE_SEARCH',
		Offer: 'TIM_LIST_PAGE_OFFER',
		Data: 'TIM_LIST_PAGE_DATA',
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
			$('#tab-user-data').removeClass('active')
			showTable(currentSelection)
		})

		$('#tab-offer').click(function () {
			currentSelection = Selection.Offer
			$(this).addClass('active')
			$('#tab-search').removeClass('active')
			$('#tab-user-data').removeClass('active')
			showTable(currentSelection)
		})

		$('#tab-user-data').click(function () {
			currentSelection = Selection.Data
			$(this).addClass('active')
			$('#tab-search').removeClass('active')
			$('#tab-offer').removeClass('active')
			showTable(currentSelection)
		})
	
	})

	function showTable (currentSelection) {
		switch (currentSelection) {
		case Selection.Search:
			$('#table-search').show()
			$('#table-offer').hide()
			$('#user-data').hide()
		break

		case Selection.Offer:
			$('#table-search').hide()
			$('#table-offer').show()
			$('#user-data').hide()
			break
		case Selection.Data:
			$('#table-search').hide()
			$('#table-offer').hide()
			$('#user-data').show()
			
		}
	}

})()
