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

USER_AGENT_ANDROID = 0  // Android browser
USER_AGENT_MOBILE = 1   // Another mobile browser
USER_AGENT_APP = 2      // Native app
USER_AGENT_OTHER = 3    // Don't know, probably a desktop

function detect_user_agent(){
  // https://stackoverflow.com/questions/3514784/
  // https://stackoverflow.com/questions/6031412
  if (navigator.userAgent.toLowerCase().indexOf("android") > -1) {
    // cf app_name inside android/app/src/main/res/values/strings.xml
    if (navigator.userAgent.indexOf("Manger Veggie") > -1)
      return USER_AGENT_APP;
    else
      return USER_AGENT_ANDROID;
  } else if(/webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
    return USER_AGENT_MOBILE;
  }

  return USER_AGENT_OTHER;
}

function update_mobile_links() {
  /* add a link inside a menu either:
   - to the about page in order to explain how to add a shortcut (iPhone & co)
   - to the Android application, if the browser is using Android and if not already using the application */
  ua = detect_user_agent();

  if (ua != USER_AGENT_ANDROID)
    $('#android-download-menu').hide();

  if (ua != USER_AGENT_MOBILE)
    $('#mobile-shortcut-menu').hide();
}

function on_navbar_ready() {
  update_mobile_links()
}
