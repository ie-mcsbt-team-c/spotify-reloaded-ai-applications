const getSongs = () => {
    

    let stack = document.getElementById("stack");	
    let songcard = document.createElement("div");
    songcard.classList.add("card");
    

    let song = document.createElement("h3");
    song.classList.add("card-title")
    song.innerHTML = "Human After All"
    songcard.appendChild(song); 

    let artist = document.createElement("h4");
    artist.classList.add("card-text")
    artist.innerHTML = "Daft Punk"
    songcard.appendChild(artist)
    
    let songlink = document.createElement("a");
    songlink.classList.add("card-text")
    songlink.innerHTML = "Link"
    songlink.setAttribute("href", "https://open.spotify.com/track/3aCKAkMx3yfaj3AO5Gz47e")
    songcard.appendChild(songlink)

    let image = document.createElement("img");
    image.classList.add("card-img-top");
    image.setAttribute("src", "../static/img/spotify.png")
    songcard.appendChild(image)

    let frame = document.createElement("iframe")
    frame.setAttribute("src", "https://open.spotify.com/embed/album/2T7DdrOvsqOqU9bGTkjBYu")
    frame.setAttribute("width", "300")
    frame.setAttribute("height", "380")
    frame.setAttribute("frameborder", "0")
    frame.setAttribute("allowtransparency", "true")
    frame.setAttribute("allow", "encrypted-media")
    stack.appendChild(frame)

    stack.appendChild(songcard)
    console.log("im here"); 
}; 