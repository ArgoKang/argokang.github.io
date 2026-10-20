/*
	V-High — page behavior. Runs after i18n.js (uses window.I18N for form messages).
	- Header turns solid once the page scrolls; mobile menu toggle.
	- Highlights the nav link of the section in view.
	- Fades sections in as they scroll into view.
	- Contact form opens the visitor's email app with the message filled in.
*/

(function() {

	var root = document.documentElement;
	root.classList.remove('no-js');

	// Header: solid background after scrolling.
	var header = document.getElementById('header');

	function onScroll() {
		if (header)
			header.classList.toggle('is-scrolled', window.scrollY > 24);
	}

	window.addEventListener('scroll', onScroll, { passive: true });
	onScroll();

	// Mobile menu.
	var toggle = header && header.querySelector('.menu-toggle');

	function setMenu(open) {
		header.classList.toggle('is-open', open);
		toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
	}

	if (toggle) {
		toggle.addEventListener('click', function() {
			setMenu(!header.classList.contains('is-open'));
		});

		header.querySelectorAll('.nav a').forEach(function(link) {
			link.addEventListener('click', function() { setMenu(false); });
		});

		document.addEventListener('keydown', function(event) {
			if (event.key === 'Escape')
				setMenu(false);
		});
	}

	// Active nav link (only links that point at a section on this page).
	var navLinks = Array.prototype.filter.call(document.querySelectorAll('.nav a'), function(link) {
		return link.getAttribute('href').charAt(0) === '#';
	});

	if (navLinks.length && 'IntersectionObserver' in window) {
		var byId = {};
		navLinks.forEach(function(link) { byId[link.getAttribute('href').slice(1)] = link; });

		var sectionObserver = new IntersectionObserver(function(entries) {
			entries.forEach(function(entry) {
				if (!entry.isIntersecting)
					return;
				navLinks.forEach(function(link) { link.classList.remove('active'); });
				var link = byId[entry.target.id];
				if (link)
					link.classList.add('active');
			});
		}, { rootMargin: '-45% 0px -50% 0px' });

		Object.keys(byId).forEach(function(id) {
			var section = document.getElementById(id);
			if (section)
				sectionObserver.observe(section);
		});
	}

	// Scroll reveal.
	var reveals = document.querySelectorAll('.reveal');

	if ('IntersectionObserver' in window) {
		var revealObserver = new IntersectionObserver(function(entries) {
			entries.forEach(function(entry) {
				if (entry.isIntersecting) {
					entry.target.classList.add('is-in');
					revealObserver.unobserve(entry.target);
				}
			});
		}, { rootMargin: '0px 0px -10% 0px' });

		reveals.forEach(function(el) { revealObserver.observe(el); });
	}
	else {
		reveals.forEach(function(el) { el.classList.add('is-in'); });
	}

	// Monster cards: tilt toward the pointer and move the holo sheen (mouse only).
	var canTilt = window.matchMedia('(hover: hover) and (pointer: fine)').matches
		&& !window.matchMedia('(prefers-reduced-motion: reduce)').matches;

	if (canTilt) {
		document.querySelectorAll('.mcard').forEach(function(card) {
			card.addEventListener('pointermove', function(event) {
				var rect = card.getBoundingClientRect();
				var x = (event.clientX - rect.left) / rect.width;
				var y = (event.clientY - rect.top) / rect.height;
				card.style.setProperty('--rx', ((x - 0.5) * 16).toFixed(2) + 'deg');
				card.style.setProperty('--ry', ((0.5 - y) * 16).toFixed(2) + 'deg');
				card.style.setProperty('--mx', (x * 100).toFixed(1) + '%');
				card.style.setProperty('--my', (y * 100).toFixed(1) + '%');
			});

			card.addEventListener('pointerleave', function() {
				['--rx', '--ry', '--mx', '--my'].forEach(function(name) { card.style.removeProperty(name); });
			});
		});
	}

	// Contact form.
	var form = document.getElementById('contact-form');

	if (form) {
		var t = window.I18N ? window.I18N.t : function(key) { return key; };
		var errorBox = document.getElementById('contact-error');

		function showError(key) {
			errorBox.textContent = t(key);
			errorBox.hidden = false;
		}

		form.addEventListener('submit', function(event) {
			event.preventDefault();

			var name = form.name.value.trim();
			var email = form.email.value.trim();
			var message = form.message.value.trim();

			if (!name || !email || !message)
				return showError('contact.err.required');

			if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email))
				return showError('contact.err.email');

			errorBox.hidden = true;

			var lang = window.I18N ? window.I18N.current() : root.lang;
			var subject = '[V-High Contact] ' + name;
			var body = 'Name: ' + name + '\nEmail: ' + email + '\nLanguage: ' + lang + '\n\n' + message;

			window.location.href = 'mailto:help@v-high.com'
				+ '?subject=' + encodeURIComponent(subject)
				+ '&body=' + encodeURIComponent(body);
		});
	}

})();
