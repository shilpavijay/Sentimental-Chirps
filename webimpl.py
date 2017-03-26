from flask import Flask, render_template, request, Response
import matplotlib.pyplot as plt, mpld3
import matplotlib.animation as animation
from matplotlib import style
import time
import json
# import twitterSentmtAlysis as tsa
app = Flask(__name__)

@app.route("/")
def twitterSenti():
	return render_template('landing.html')

@app.route('/<topic>/')
def mainpg(topic):
	print (topic)
	# tsa.on_streaming(topic)

	# plotting

	style.use("ggplot")

	figure = plt.figure()
	subpl = figure.add_subplot(1,1,1)

	def animate(i):
		pullData = open("twitter-out.txt","r").read()
		lines = pullData.split('\n')

		xl = []
		yl = []

		x = 0
		y = 0

		for l in lines[-500:]:
			x += 1
			if "pos" in l:
			    y += 1
			elif "neg" in l:
			    y -= 1

			xl.append(x)
			yl.append(y)

		subpl.clear()
		subpl.plot(xl,yl)
	anim = animation.FuncAnimation(figure, animate, interval=1000)
	# plt.show()
	try:
		json01 = json.dumps(mpld3.fig_to_dict(figure))
		# print (json01['json'])
	# mpld3.fig_to_html(figure, template_type="simple")
	# mpld3.save_html(figure,"test.html")
	except Exception as e:
		print (e)

	return render_template('landing.html',drawing=json01)
