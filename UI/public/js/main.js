(() => {
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

	function post(endpoint, data) {
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

	window.onload = function() {
		const app = new Vue({
			el: '#app',
			data: {
				page: 'create-persona',
				persona: [{phrase: '', weight: 100}], // {phrase: <str>, weight: <int>}
				feed: [], // {summary: <str>, full: <str>, score: <int>}
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
				implementPersona() {
					post('/add_persona', this.persona[0])
						.then(({feed}) => {
							this.feed = feed;
							this.entry = 0;
						});
				},
				nextEntry() {
					if (this.entry >= 0) {
						this.entry = (this.entry + 1) % this.feed.length;
					} else
						throw new Error('Ouch!')
				}
			}
		});
	}
})();