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
