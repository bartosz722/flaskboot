function gotoBuyItem(elem, ev) {
  if (ev.target.tagName.toLowerCase() != 'a') {
    elem.getElementsByTagName('a')[0].click()
  }
}
