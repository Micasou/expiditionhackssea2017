(() => {
	const {floor, random} = Math;

	function randomColor() {
		const whiten = 155;
		const main = [0, 0, 0]
			.map(c => floor(random() * (256 - whiten) + whiten))
			.join(',')
		return `rgb(${main})`;
	}

	function querify(obj) {
		const list = [];
		for (let key in obj) {
			if (obj.hasOwnProperty(key)) {
				list.push(`${key}=${obj[key]}`);
			}
		}

		if (list.length > 0) {
			return `?${list.join('&')}`;
		} else {
			return '';
		}
	}

	function async(gfn) {
		return function(...args) {
			const gen = gfn.apply(this, args);

			const win = (val) => Promise
				.resolve(gen.next(val))
				.then(proceed);
			const fail = (err) => Promise
				.resolve(gen.throw(err))
				.then(proceed);
			const proceed = ({done, value}) => done ?
				value : 
				Promise
					.resolve(value)
					.then(win, fail);
			return Promise
				.resolve(gen.next())
				.then(proceed);
		}
	}

	function post(endpoint, data = {}) {
		return new Promise((win, fail) => {
			const x = new XMLHttpRequest();

			x.onreadystatechange = () => {
				if (x.readyState === 4) {

					if (x.status === 200) {
						win(JSON.parse(x.responseText));
					} else {
						fail(new Error(`HTTP request failed with error ${x.status}`));
					}
				}
			}

			x.open('POST', endpoint, true);
			x.setRequestHeader('Content-Type', "application/json");
			x.send(JSON.stringify(data));
		});
	}

	function get(endpoint, data = {}) {
		return new Promise((win, fail) => {
			const x = new XMLHttpRequest();
			const query = querify(data);
			x.onreadystatechange = () => {
				if (x.readyState === 4) {

					if (x.status === 200) {
						win(JSON.parse(x.responseText));
					} else {
						fail(new Error(`HTTP request failed with error ${x.status}`));
					}
				}
			}

			x.open('GET', endpoint + querify(data), true);
			x.setRequestHeader('Content-Type', "application/json");
			x.send();
		});
	}

	window.onload = function() {
		const app = new Vue({
			el: '#app',
			data: {
				personaTitles: [
					"ICE Director",
					"Assistant Secretary of Defense for Nuclear, Chemical, and Biological Defense Programs (ASD(NCB))",
					"North Korea policy group",
					"Director; maritime security operations",
					"Director; wildfire division",
					"mission director; syria",
					"centCOM j2"
				],
				page: 0,
				persona: null,
				entry: -1,
				showAll: true
			},
			methods: {
				newKeyword() {
					this.persona.push({
						phrase: '',
						weight: 100
					});
				},
				/*
				editPersona() {
					post('/edit_persona/' + i, this.persona[0])
						.then(({persona}) => {
							this.persona = persona;
							this.entry = 0;
						});
				}
				*/
				nextEntry() {
					if (this.entry >= 0) {
						this.entry = (this.entry + 1) % this.feed.length;
					} else
						throw new Error('Ouch!')
				},
				loadPersona(i) {
					if (0 <= i && i < 7) {
						get('fetch_persona/' + i)
							.then(({persona}) => {
								console.log(persona);
								this.persona = persona;
							});
					}
				},
				toggleViewType() {
					this.showAll = !this.showAll;
				},
				randomColor
			}
		});
	}
})();