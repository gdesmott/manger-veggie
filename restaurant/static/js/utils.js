function tags_to_color(tags) {
  if (tags.indexOf('vegan') >= 0) {
    return 'darkgreen'
  } else if (tags.indexOf('vegetarian') >= 0) {
    return 'green'
  } else if (tags.indexOf('vegan-friendly') >= 0) {
    return 'orange'
  } else {
    return 'blue'
  }
}

/* add a link inside a menu either:
 - to the about page in order to explain how to add a shortcut (iPhone & co)
 - to the Android application, if the browser is using Android and if not already using the application */
function add_mobile_link() {
  // https://stackoverflow.com/questions/3514784/
  // https://stackoverflow.com/questions/6031412
  if(navigator.userAgent.toLowerCase().indexOf("android") > -1) {
    // cf app_name inside android/app/src/main/res/values/strings.xml
    if(navigator.userAgent.indexOf("Manger Veggie") > -1) {
      return;
    }
    $('<li><a href="https://play.google.com/store/apps/details?id=be.desmottes.mangerveggie"><img class="google-play-badge-menu" src="static/img/google-play-badge.png"/></a></li>').prependTo(".navbar-right");
  }
  else if(/webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
    $('<li><a href="/about#mobile_shortcut">Ajouter un raccourci vers vegOresto</a></li>').prependTo(".navbar-right");
  }
}
