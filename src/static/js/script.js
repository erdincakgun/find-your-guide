function filterGuides() {
  const language = document.getElementById('language').value.toLowerCase();
  const location = document.getElementById('location').value.toLowerCase();
  const guides = document.querySelectorAll('.guide');

  guides.forEach(guide => {
    const guideLanguages = guide.getAttribute('data-language').toLowerCase();
    const guideLocation = guide.getAttribute('data-location').toLowerCase();

    if ((language === "" || guideLanguages.includes(language)) && (location === "" || guideLocation.includes(location))) {
      guide.style.display = "";
    } else {
      guide.style.display = "none";
    }
  });
}