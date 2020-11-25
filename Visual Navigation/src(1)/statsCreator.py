from matplotlib import pyplot as plt


plt.style.use("dark_background")



default_data = [1,2,3]

class graphMaker():

	def __init__(self, graphs_row,graphs_col):
		self.grid = plt.GridSpec(graphs_row, graphs_col, wspace=0.5, hspace=0.5)


	def barGraph(self,x_axis, y_axis, title,graph_posx, graph_posy):

		ax1 = plt.subplot(self.grid[graph_posx, graph_posy])
		ax1.bar(x_axis, y_axis)
		ax1.set_title(title, weight ="bold")


	def pieGraph(self,data,legend,graph_posx, graph_posy):

		ax2 = plt.subplot(self.grid[graph_posx, graph_posy])
		ax2.pie(data, autopct='%1.0f%%', shadow=True)
		ax2.axis("equal")
		ax2.legend(legend)


	def plotGraph(self,x_axis, y_axis, title, graph_posx, graph_posy):

		ax4 = plt.subplot(self.grid[graph_posx, graph_posy])
		ax4.plot(x_axis, y_axis, "o-")
		ax4.set_title(title)


	def showImage(self,data,title,graph_posx, graph_posy):

		ax5 = plt.subplot(self.grid[graph_posx, graph_posy])
		ax5.imshow(data, aspect="auto", origin = "upper")
		ax5.set_title(title, weight ="bold")


	def showGraphs(self):
		plt.tight_layout()
		plt.show()

