function pw() {
	GenerateToTextField();
	var resultField = document.getElementById('hashedPassword');
	resultField.style.visibility = 'visible';
	resultField.focus();
	if (document.selection) {
		var sel = document.selection.createRange();
		sel.move(0, resultField.value.length);
		sel.select();
	}
	else {
		resultField.selectionStart = 0;
		resultField.selectionEnd = resultField.value.length;
	}
	document.getElementById('result').className = 'generated';
}

function init() {
	var domainField = document.getElementById('domain');
	if (navigator.userAgent.match(/iPhone/i) || navigator.userAgent.match(/iPod/i)) {
		domainField.type = 'url';
	}
	if (domainField.value == '') {
		domainField.focus();
	}
	else {
		document.getElementById('sitePassword').focus();
	}
}

function startOver() {
	document.getElementById('result').className = '';
	var resultField = document.getElementById('hashedPassword');
	resultField.value = '';
	resultField.style.visibility = 'hidden';
}

function domainToLower() {
	var domainField = document.getElementById('domain');
	domainField.value = domainField.value.toLowerCase();
}