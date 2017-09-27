var url = window.location.href;
var origin = window.location.origin;

try {
    window.location.replace(
        origin + '/en/weight/getweight/' + url.split('#')[1].split('=')[1].split('&')[0]
    );
} catch (error) {
    console.log(error);
}