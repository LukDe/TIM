;(function () {
  'use strict'

  var Selection = {
    Register: 'TIM_LOGIN_PAGE_REGISTER',
    UserLogin: 'TIM_LOGIN_PAGE_USER_LOGIN',
    PhoneLogin: 'TIM_LOGIN_PAGE_PHONE_LOGIN'
  }

  var currentSelection = Selection.Register

  // Apply the callbacks when the document is ready.
  $(document).ready(function () {
    // On initialization.
    $('#tab-register').addClass('active')
    showForm(currentSelection)

    // Handlers for clicks on the tabs.
    $('#tab-register').click(function () {
      currentSelection = Selection.Register
      $(this).addClass('active')
      $('#tab-user-login').removeClass('active')
      $('#tab-phone-login').removeClass('active')

      showForm(currentSelection)
    })

    $('#tab-user-login').click(function () {
      currentSelection = Selection.UserLogin
      $(this).addClass('active')
      $('#tab-register').removeClass('active')
      $('#tab-phone-login').removeClass('active')

      showForm(currentSelection)
    })

    $('#tab-phone-login').click(function () {
      currentSelection = Selection.PhoneLogin
      $(this).addClass('active')
      $('#tab-register').removeClass('active')
      $('#tab-user-login').removeClass('active')

      showForm(currentSelection)
    })
  })

  function showForm (currentSelection) {
    switch (currentSelection) {
    case Selection.Register:
      $('#form-register').show()
      $('#form-user-login').hide()
      $('#form-phone-login').hide()
      break

    case Selection.UserLogin:
      $('#form-register').hide()
      $('#form-user-login').show()
      $('#form-phone-login').hide()
      break

    case Selection.PhoneLogin:
      $('#form-register').hide()
      $('#form-user-login').hide()
      $('#form-phone-login').show()
      break
    }
  }

})()
