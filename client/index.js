let likeBtn = document.getElementById("like");
let dislikeBtn = document.getElementById("dislike");
let likeCount = document.getElementById("like_count");
let dislikeCount = document.getElementById("dislike_count");

let res = axios.get("http://127.0.0.1:8000/getlikes/");
res.then((res) => {
	likeCount.textContent = res.data.likes ? res.data.likes : null;
	dislikeCount.textContent = res.data.dislikes ? res.data.dislikes : null;
});
likeBtn.addEventListener("click", (e) => {
	let res = axios.post("http://127.0.0.1:8000/addlike/");
	res.then((res) => {
		likeCount.textContent = res.data.likes ? res.data.likes : null;
		dislikeCount.textContent = res.data.dislikes ? res.data.dislikes : null;
	});
});
dislikeBtn.addEventListener("click", (e) => {
	console.log("hl");
	let res = axios.post("http://127.0.0.1:8000/adddislike/");
	res.then((res) => {
		likeCount.textContent = res.data.likes ? res.data.likes : null;
		dislikeCount.textContent = res.data.dislikes ? res.data.dislikes : null;
	});
});
