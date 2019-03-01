(function($) {
  "use strict"; // Start of use strict

  var $usernameInput = $('input#user-message-target'),
      $userList = $('div#user-search-results ul'),
      $userListDiv = $('div#user-search-results');

  $(document).ready(function(){
    $(this).scrollTop(0);
  });

  setTimeout(function() {
    $('#message').fadeOut('slow');
  }, 3000);

  var setupUserPicking = function() {
    var $nameItems = $('div#user-search-results ul li');
    $nameItems.on('click', function() {
      $usernameInput.val($(this).text());
      $userList.children().remove();
      $userListDiv.removeClass('show-list');
    });
  }

  var setupSearch = function() {
    $usernameInput.on('input', function() {
      var username = $(this).val();
      if (username) {
        $.get('/accounts/search_user?username='+username).done(function(data) {
          $userList.children().remove();
          if (data.users.length > 0) {
            for (name of data.users) {
              $userList.append('<li>'+ name +'</li>')
            }
            $userListDiv.addClass('show-list');
            setupUserPicking();
          }
        });
      } else {
        $userList.children().remove();
        $userListDiv.removeClass('show-list');
      }
    });
  }

  // Smooth scrolling using jQuery easing
  $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: (target.offset().top - 48)
        }, 1000, "easeInOutExpo");
        return false;
      }
    }
  });

  // Closes responsive menu when a scroll trigger link is clicked
  $('.js-scroll-trigger').click(function() {
    $('.navbar-collapse').collapse('hide');
  });

  // Activate scrollspy to add active class to navbar items on scroll
  $('body').scrollspy({
    target: '#mainNav',
    offset: 54
  });

  // Collapse Navbar
  var navbarCollapse = function() {
    if ($("#mainNav").offset().top > 100) {
      $("#mainNav").addClass("navbar-shrink");
    } else {
      $("#mainNav").removeClass("navbar-shrink");
    }
  };
  // Collapse now if page is not at top
  navbarCollapse();
  // Collapse the navbar when page is scrolled
  $(window).scroll(navbarCollapse);
  setupSearch();

})(jQuery); // End of use strict