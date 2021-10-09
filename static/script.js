const editor = document.getElementById('editor');

function ajax(path, method='GET') {
	return new Promise(function (resolve, reject) {
		const xhttp = new XMLHttpRequest();
		xhttp.onload = function() {
			resolve(this.responseText); 
		};
		xhttp.open(method, path);
		xhttp.send();
	});
}

function new_file() {
	editor.reset();
}

async function open_file() {
	const name = prompt('Enter file name to open');
	editor.elements.content.value = await ajax('/open_file/' + name);
	editor.elements.name.value = name;
}