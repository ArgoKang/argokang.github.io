/*
	V-High site localization.

	- Short UI strings: elements with data-i18n="key" get their innerHTML from STRINGS.
	  data-i18n-placeholder / data-i18n-alt / data-i18n-content set that attribute instead.
	- Long documents (legal pages): each language lives in its own
	  <div data-lang-block lang="xx"> and only the current one is shown.
	- Language priority: ?lang= in the URL > saved choice > browser language > English.

	To add a language: add it to LANGS, add a STRINGS entry, and add
	data-lang-block sections to the pages under pages/.
*/

(function() {

	var LANGS = [
		{ code: 'en',    label: 'English' },
		{ code: 'ko',    label: '한국어' },
		{ code: 'pt-BR', label: 'Português (BR)' }
	];

	var DEFAULT_LANG = 'en';
	var STORAGE_KEY = 'vhigh-lang';

	var STRINGS = {

		'en': {
			'meta.title.home': 'V-High - Mobile Game Studio',
			'meta.title.tos': 'Terms of Service - V-High',
			'meta.title.privacy': 'Privacy Policy - V-High',
			'meta.title.deletion': 'Account Deletion Request - V-High',
			'meta.description': 'V-High is a mobile game studio. Our first game, Archmage Lugh: beat every boss, absorb it, and lead it in your legion.',

			'lang.label': 'Language',

			'nav.home': 'Home',
			'nav.games': 'Games',
			'nav.about': 'About',
			'nav.career': 'Career',
			'nav.contact': 'Contact',
			'nav.tos': 'Terms',
			'nav.privacy': 'Privacy',
			'nav.deletion': 'Account Deletion',

			'games.title': 'Games',
			'games.iconAlt': 'Archmage Lugh app icon',
			'games.learnMore': 'Learn More',
			'games.lugh1.title': 'Archmage Lugh',
			'games.lugh1.text': 'The legendary archmage who absorbs it all.',
			'games.lugh2.title': 'Beat it. Absorb it. Command it.',
			'games.lugh2.text': 'Every boss leaves something behind. Its body becomes a minion. Its weapon becomes your gear. Its power becomes an Archmagic. One victory. Three ways stronger.',
			'games.lugh3.title': '1 + 1 + 1 = &infin;',
			'games.lugh3.text': 'Pick a card. Summon an ally. Rewrite the rules with an Archmagic. Stack them right, and your legion fills the screen.',

			'about.title': 'About',
			'about.text': 'We make games you can start in a second and think about all day. Bright on the outside. Deep on the inside.',
			'about.f1.title': 'Easy to start. Endless to master.',
			'about.f1.text': 'One thumb is all it takes. The deeper you go, the more there is to discover.',
			'about.f2.title': 'Cute. With swagger.',
			'about.f2.text': 'Adorable at first glance. Commanding up close. Every character is styled down to the last detail.',
			'about.f3.title': 'Big moments. Every run.',
			'about.f3.text': 'Thousands of enemies. A legion that fights back. No two runs play out the same.',
			'about.f4.title': 'Your build. Your story.',
			'about.f4.text': 'Choices that matter. Combos you discover yourself. You win because you made it work.',
			'about.f5.title': 'Collect. Grow. Repeat.',
			'about.f5.text': 'A collection that keeps growing. Toys for grown-ups, made to come back to every day.',
			'about.f6.title': 'Made for your phone.',
			'about.f6.text': 'Quick sessions. Light download. Smooth play. All you need is a spare minute.',
			'about.cta': 'Say Hello',

			'career.title': 'Career',
			'career.text': 'Great games are made by people who can\'t stop playing them. If that\'s you, let\'s talk.',
			'career.f1.title': 'Engineers',
			'career.f1.text': 'Put thousands of units on a phone screen. Then make it feel effortless.',
			'career.f2.title': 'Artists &amp; Designers',
			'career.f2.text': 'Draw characters people fall for at first sight.',
			'career.f3.title': 'Team Players',
			'career.f3.text': 'Small team. Big ownership. Your ideas ship.',
			'career.f4.title': 'Curious Minds',
			'career.f4.text': 'Question everything. Prototype fast. Keep what\'s fun.',
			'career.cta': 'Send Us Your Work',

			'contact.title': 'Contact',
			'contact.text': 'Questions, ideas, or just want to say hi? We read every message.',
			'contact.name': 'Name',
			'contact.email': 'Email',
			'contact.message': 'Message',
			'contact.send': 'Send Message',
			'contact.note': 'Clicking the button opens your email app with this message addressed to help@v-high.com.',
			'contact.err.required': 'Please fill in your name, email and message.',
			'contact.err.email': 'Please check your email address.',
			'contact.info.email': 'Email',
			'contact.info.careers': 'Careers',

			'footer.tos': 'Terms of Service',
			'footer.privacy': 'Privacy Policy',
			'footer.deletion': 'Account Deletion Request'
		},

		'ko': {
			'meta.title.home': 'V-High - 모바일 게임 스튜디오',
			'meta.title.tos': '이용약관 - V-High',
			'meta.title.privacy': '개인정보처리방침 - V-High',
			'meta.title.deletion': '계정 삭제 요청 - V-High',
			'meta.description': 'V-High는 모바일 게임 스튜디오입니다. 첫 작품 대마법사 루 — 쓰러뜨린 보스를 흡수해 나의 군단으로.',

			'lang.label': '언어',

			'nav.home': '홈',
			'nav.games': '게임',
			'nav.about': '소개',
			'nav.career': '채용',
			'nav.contact': '문의',
			'nav.tos': '이용약관',
			'nav.privacy': '개인정보',
			'nav.deletion': '계정 삭제',

			'games.title': '게임',
			'games.iconAlt': 'Archmage Lugh 앱 아이콘',
			'games.learnMore': '자세히 보기',
			'games.lugh1.title': '대마법사 루',
			'games.lugh1.text': '모든 것을 흡수하는 전설의 대마법사.',
			'games.lugh2.title': '쓰러뜨리고. 흡수하고. 거느린다.',
			'games.lugh2.text': '보스는 모든 것을 남긴다. 본체는 하수인으로. 무기는 나의 장비로. 힘은 대마법으로. 한 번의 승리, 세 배의 성장.',
			'games.lugh3.title': '1 + 1 + 1 = &infin;',
			'games.lugh3.text': '카드를 고르고, 아군을 부르고, 대마법으로 판의 규칙을 바꾼다. 제대로 쌓이는 순간, 화면이 내 군단으로 가득 찬다.',

			'about.title': '소개',
			'about.text': '1초 만에 시작해서, 하루 종일 생각나는 게임을 만듭니다. 겉은 밝고 경쾌하게. 속은 깊고 단단하게.',
			'about.f1.title': '시작은 쉽게. 깊이는 끝없이.',
			'about.f1.text': '엄지 하나면 충분합니다. 오를수록 새로운 조합이 열립니다.',
			'about.f2.title': '귀엽게. 하지만 멋지게.',
			'about.f2.text': '한눈에 끌리는 귀여움, 눈을 뗄 수 없는 카리스마. 작은 캐릭터 하나에도 맵시를 담았습니다.',
			'about.f3.title': '매 판이 하이라이트.',
			'about.f3.text': '몰려오는 수천의 적, 맞서는 나의 군단. 같은 판은 두 번 오지 않습니다.',
			'about.f4.title': '나만의 빌드. 나만의 이야기.',
			'about.f4.text': '의미 있는 선택, 직접 찾아낸 조합. 운이 좋아서가 아니라, 내가 잘 짜서 이깁니다.',
			'about.f5.title': '모으고. 키우고. 또 모으고.',
			'about.f5.text': '끝없이 늘어나는 컬렉션. 매일 돌아오고 싶은, 어른들을 위한 장난감.',
			'about.f6.title': '손안에서 완성되는 게임.',
			'about.f6.text': '짧은 한 판, 가벼운 용량, 부드러운 플레이. 잠깐의 틈이면 충분합니다.',
			'about.cta': '연락하기',

			'career.title': '채용',
			'career.text': '좋은 게임은, 그 게임을 멈추지 못하는 사람들이 만듭니다. 당신이 그렇다면, 이야기 나눠요.',
			'career.f1.title': '엔지니어',
			'career.f1.text': '휴대폰 화면 위의 수천 개 유닛. 그리고 그걸 아무렇지 않게 느껴지게.',
			'career.f2.title': '아티스트 &amp; 디자이너',
			'career.f2.text': '첫눈에 반하는 캐릭터를 그려 주세요.',
			'career.f3.title': '팀 플레이어',
			'career.f3.text': '작은 팀, 큰 권한. 당신의 아이디어가 그대로 게임이 됩니다.',
			'career.f4.title': '호기심 많은 사람',
			'career.f4.text': '모든 걸 의심하고, 빠르게 만들어 보고, 재밌는 것만 남깁니다.',
			'career.cta': '포트폴리오 보내기',

			'contact.title': '문의',
			'contact.text': '궁금한 점, 제안, 그냥 인사라도 좋아요. 모든 메시지를 직접 읽습니다.',
			'contact.name': '이름',
			'contact.email': '이메일',
			'contact.message': '메시지',
			'contact.send': '메일 보내기',
			'contact.note': '버튼을 누르면 메일 앱이 열리고, 작성한 내용이 help@v-high.com 앞으로 채워집니다.',
			'contact.err.required': '이름, 이메일, 메시지를 모두 입력해 주세요.',
			'contact.err.email': '이메일 주소를 확인해 주세요.',
			'contact.info.email': '이메일',
			'contact.info.careers': '채용',

			'footer.tos': '이용약관',
			'footer.privacy': '개인정보처리방침',
			'footer.deletion': '계정 삭제 요청'
		},

		'pt-BR': {
			'meta.title.home': 'V-High - Estúdio de Jogos Mobile',
			'meta.title.tos': 'Termos de Serviço - V-High',
			'meta.title.privacy': 'Política de Privacidade - V-High',
			'meta.title.deletion': 'Solicitação de Exclusão de Conta - V-High',
			'meta.description': 'A V-High é um estúdio de jogos mobile. Nosso primeiro jogo, Archmage Lugh: derrote cada chefe, absorva-o e comande-o na sua legião.',

			'lang.label': 'Idioma',

			'nav.home': 'Início',
			'nav.games': 'Jogos',
			'nav.about': 'Sobre',
			'nav.career': 'Carreiras',
			'nav.contact': 'Contato',
			'nav.tos': 'Termos',
			'nav.privacy': 'Privacidade',
			'nav.deletion': 'Exclusão de Conta',

			'games.title': 'Jogos',
			'games.iconAlt': 'Ícone do app Archmage Lugh',
			'games.learnMore': 'Saiba mais',
			'games.lugh1.title': 'Archmage Lugh',
			'games.lugh1.text': 'O lendário arquimago que absorve tudo.',
			'games.lugh2.title': 'Derrote. Absorva. Comande.',
			'games.lugh2.text': 'Todo chefe deixa algo para trás. O corpo vira lacaio. A arma vira seu equipamento. O poder vira Arquimagia. Uma vitória. Três vezes mais forte.',
			'games.lugh3.title': '1 + 1 + 1 = &infin;',
			'games.lugh3.text': 'Escolha uma carta. Invoque um aliado. Mude as regras com uma Arquimagia. Combine do jeito certo e sua legião toma conta da tela.',

			'about.title': 'Sobre',
			'about.text': 'Fazemos jogos que você começa em um segundo e não para de pensar o dia todo. Leves por fora. Profundos por dentro.',
			'about.f1.title': 'Fácil de começar. Infinito para dominar.',
			'about.f1.text': 'Um polegar basta. Quanto mais você avança, mais há para descobrir.',
			'about.f2.title': 'Fofo. E cheio de estilo.',
			'about.f2.text': 'Fofo à primeira vista. Carismático de perto. Cada personagem tem estilo até no último detalhe.',
			'about.f3.title': 'Grandes momentos. Toda partida.',
			'about.f3.text': 'Milhares de inimigos. Uma legião à altura. Nenhuma partida é igual.',
			'about.f4.title': 'Sua build. Sua história.',
			'about.f4.text': 'Escolhas que importam. Combos que você mesmo descobre. Você vence porque fez dar certo.',
			'about.f5.title': 'Colecione. Evolua. Repita.',
			'about.f5.text': 'Uma coleção que não para de crescer. Brinquedos para adultos, feitos para voltar todo dia.',
			'about.f6.title': 'Feito para o seu celular.',
			'about.f6.text': 'Partidas rápidas. Download leve. Jogo fluido. Basta um minutinho livre.',
			'about.cta': 'Diga Oi',

			'career.title': 'Carreiras',
			'career.text': 'Grandes jogos são feitos por quem não consegue parar de jogá-los. Se é você, vamos conversar.',
			'career.f1.title': 'Engenharia',
			'career.f1.text': 'Milhares de unidades na tela do celular. E tudo parecendo fácil.',
			'career.f2.title': 'Artistas e Designers',
			'career.f2.text': 'Crie personagens que conquistam à primeira vista.',
			'career.f3.title': 'Espírito de Equipe',
			'career.f3.text': 'Time pequeno. Muita autonomia. Suas ideias viram jogo.',
			'career.f4.title': 'Mentes Curiosas',
			'career.f4.text': 'Questione tudo. Prototipe rápido. Fique com o que é divertido.',
			'career.cta': 'Envie seu Portfólio',

			'contact.title': 'Contato',
			'contact.text': 'Dúvidas, ideias ou só quer dizer oi? Lemos todas as mensagens.',
			'contact.name': 'Nome',
			'contact.email': 'E-mail',
			'contact.message': 'Mensagem',
			'contact.send': 'Enviar mensagem',
			'contact.note': 'Ao clicar no botão, seu app de e-mail será aberto com a mensagem pronta para help@v-high.com.',
			'contact.err.required': 'Preencha seu nome, e-mail e mensagem.',
			'contact.err.email': 'Verifique seu endereço de e-mail.',
			'contact.info.email': 'E-mail',
			'contact.info.careers': 'Carreiras',

			'footer.tos': 'Termos de Serviço',
			'footer.privacy': 'Política de Privacidade',
			'footer.deletion': 'Solicitação de Exclusão de Conta'
		}

	};

	function isSupported(code) {
		for (var i = 0; i < LANGS.length; i++)
			if (LANGS[i].code === code)
				return true;
		return false;
	}

	// Maps any browser/URL language tag (e.g. "ko-KR", "pt", "pt-PT") to a supported code.
	function normalize(tag) {
		if (!tag)
			return null;
		tag = String(tag).toLowerCase();
		if (tag.indexOf('ko') === 0) return 'ko';
		if (tag.indexOf('pt') === 0) return 'pt-BR';
		if (tag.indexOf('en') === 0) return 'en';
		return null;
	}

	function readSaved() {
		try { return localStorage.getItem(STORAGE_KEY); } catch (e) { return null; }
	}

	function save(code) {
		try { localStorage.setItem(STORAGE_KEY, code); } catch (e) {}
	}

	function detect() {
		var match = /[?&]lang=([^&#]+)/.exec(window.location.search);
		var fromUrl = match && normalize(decodeURIComponent(match[1]));
		if (fromUrl)
			return fromUrl;

		var saved = readSaved();
		if (saved && isSupported(saved))
			return saved;

		var browserLangs = navigator.languages || [navigator.language];
		for (var i = 0; i < browserLangs.length; i++) {
			var code = normalize(browserLangs[i]);
			if (code)
				return code;
		}

		return DEFAULT_LANG;
	}

	var current = DEFAULT_LANG;

	function t(key) {
		var table = STRINGS[current] || STRINGS[DEFAULT_LANG];
		if (key in table)
			return table[key];
		return STRINGS[DEFAULT_LANG][key] || key;
	}

	function applyAttr(attr) {
		var nodes = document.querySelectorAll('[data-i18n-' + attr + ']');
		for (var i = 0; i < nodes.length; i++)
			nodes[i].setAttribute(attr, t(nodes[i].getAttribute('data-i18n-' + attr)));
	}

	function apply(code) {
		current = isSupported(code) ? code : DEFAULT_LANG;
		document.documentElement.setAttribute('lang', current);

		var nodes = document.querySelectorAll('[data-i18n]');
		for (var i = 0; i < nodes.length; i++)
			nodes[i].innerHTML = t(nodes[i].getAttribute('data-i18n'));

		applyAttr('placeholder');
		applyAttr('alt');
		applyAttr('content');
		applyAttr('aria-label');

		var blocks = document.querySelectorAll('[data-lang-block]');
		for (var j = 0; j < blocks.length; j++)
			blocks[j].hidden = (blocks[j].getAttribute('lang') !== current);

		var select = document.getElementById('lang-select');
		if (select)
			select.value = current;
	}

	function buildSelector() {
		var header = document.getElementById('header');
		if (!header)
			return;

		var wrap = document.createElement('div');
		wrap.className = 'lang-switch';

		var icon = document.createElement('span');
		icon.className = 'icon solid fa-globe';
		icon.setAttribute('aria-hidden', 'true');

		var select = document.createElement('select');
		select.id = 'lang-select';
		select.setAttribute('data-i18n-aria-label', 'lang.label');

		for (var i = 0; i < LANGS.length; i++) {
			var option = document.createElement('option');
			option.value = LANGS[i].code;
			option.textContent = LANGS[i].label;
			select.appendChild(option);
		}

		select.addEventListener('change', function() {
			save(select.value);
			apply(select.value);
		});

		wrap.appendChild(icon);
		wrap.appendChild(select);
		header.appendChild(wrap);
	}

	window.I18N = {
		t: t,
		current: function() { return current; }
	};

	buildSelector();
	apply(detect());

})();
