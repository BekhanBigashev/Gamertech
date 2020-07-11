from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import*

def index(request):
	computers = Computer.objects.all()
	processors = Processor.objects.all()
	graphicscards = GraphicsCard.objects.all()
	motherboards = MotherBoard.objects.all()
	coolers = Cooler.objects.all()
	powersupplies = PowerSupply.objects.all()
	rams = Ram.objects.all()
	harddisks = HardDisk.objects.all()
	corpuses = Corpus.objects.all()
	return render(request, 'catalog/product_list.html', locals())

class ComputerListView(ListView):
	model = Computer
	queryset = Computer.objects.filter(is_active = True)


class ComputerDetailView(DetailView):
	model = Computer
	queryset = Computer.objects.filter(is_active = True)
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['product_list'] = Computer.objects.filter(is_active = True)
		return context




class ProcessorListView(ListView):
	model = Processor
	queryset = Processor.objects.all()

class ProcessorDetailView(DetailView):
	model = Processor
	queryset = Processor.objects.all()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['product_list'] = Processor.objects.all()
		return context




class MotherBoardListView(ListView):
	model = MotherBoard
	queryset = MotherBoard.objects.all()

class MotherBoardDetailView(DetailView):
	model = MotherBoard
	queryset = MotherBoard.objects.all()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['product_list'] = MotherBoard.objects.all()
		return context




class GraphicsCardListView(ListView):
	model = GraphicsCard
	queryset = GraphicsCard.objects.all()

class GraphicsCardDetailView(DetailView):
	model = GraphicsCard
	queryset = GraphicsCard.objects.all()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['product_list'] = GraphicsCard.objects.all()
		return context




class RamListView(ListView):
	model = Ram
	queryset = Ram.objects.all()

class RamDetailView(DetailView):
	model = Ram
	queryset = Ram.objects.all()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['product_list'] = Ram.objects.all()
		return context




class HardDiskListView(ListView):
	model = HardDisk
	queryset = HardDisk.objects.all()

class HardDiskDetailView(DetailView):
	model = HardDisk
	queryset = HardDisk.objects.all()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['product_list'] = HardDisk.objects.all()
		return context

class PowerSupplyListView(ListView):
	model = PowerSupply
	queryset = PowerSupply.objects.all()

class PowerSupplyDetailView(DetailView):
	model = PowerSupply
	queryset = PowerSupply.objects.all()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['product_list'] = PowerSupply.objects.all()
		return context

class CoolerListView(ListView):
	model = Cooler
	queryset = Cooler.objects.all()

class CoolerDetailView(DetailView):
	model = Cooler
	queryset = Cooler.objects.all()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['product_list'] = Cooler.objects.all()
		return context

class CorpusListView(ListView):
	model = Corpus
	queryset = Corpus.objects.all()

class CorpusDetailView(DetailView):
	model = Corpus
	queryset = Corpus.objects.all()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['product_list'] = Corpus.objects.all()
		return context
