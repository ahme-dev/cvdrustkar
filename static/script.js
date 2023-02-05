// add experience

var expNum = 2;
var addExpButton = document.getElementById('add-exp');

addExpButton.addEventListener('click', () => {
	if (expNum > 4) {
		addExpButton.style.display = 'none';
		return
	};
	document.getElementById('info-exp'+expNum).style.display = 'inherit';
	expNum++;
})

// add education

var eduNum = 2;
var addEduButton = document.getElementById('add-edu');

addEduButton.addEventListener('click', () => {
	if (eduNum > 4) {
		addEduButton.style.display = 'none';
		return
	};
	document.getElementById('info-edu'+eduNum).style.display = 'inherit';
	eduNum++;
})

// add skill

var skiNum = 2;
var addSkiButton = document.getElementById('add-ski');

addSkiButton.addEventListener('click', () => {
	if (skiNum > 8) {
		addSkiButton.style.display = 'none';
		return
	};
	document.getElementById('info-ski'+skiNum).style.display = 'inherit';
	skiNum++;
})