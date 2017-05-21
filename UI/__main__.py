from kivy.uix.boxlayout import BoxLayout
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.label import Label

# Note the special nature of indentation in the adapter declaration, where
# the adapter: is on one line, then the value side must be given at one
# level of indentation.

class MyListView(BoxLayout):
	word_list = []
	def add_word(self):
		list_view = self.ids['word_list_view']
		list_view.adapter.data.append({
			'word': 'hobo'
		})

if __name__ == '__main__':
	Builder.load_file('uix/main.kv')
	app = MyListView()
	runTouchApp(app)