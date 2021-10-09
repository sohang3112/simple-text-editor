/* TODO: Error Handling
 */

const editor = document.getElementById('editor');

function ajax(path, method='GET') {
	return new Promise(function (resolve, reject) {
		const xhttp = new XMLHttpRequest();
		xhttp.onload = function() {
			if (this.status == 200) {		// Status OK
				resolve(this.responseText); 
			} else { 						// Error 
				reject(this.status);
			}
		};
		xhttp.open(method, path);
		xhttp.send();
	});
}

function new_file() {
	editor.reset();
}

async function open_file() {
	const filename = prompt('Enter file name to open');
	try {
		editor.elements.content.value = await ajax('/open_file/' + filename);
		editor.elements.filename.value = filename;
	} catch (error) {
		if (typeof error == "number") {		// AJAX Error Status Code
			alert(`ERROR: File "${filename}" could not be opened.\nStatus Code: ${error}`);
		}
	}
}