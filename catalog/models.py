from django.db import models

class Category(models.Model):
	name = models.CharField(max_length = 64, blank = True, null = True, default = None)


	def __str__(self):
		return self.name


	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'


class Processor(models.Model):
	model = models.CharField(max_length = 200, blank = True, null = True, default = None)
	socket = models.CharField(max_length = 200, blank = True, null = True, default = None)
	frequency = models.CharField(max_length = 200, blank = True, null = True, default = None)
	count_of_cores = models.CharField(max_length = 200, blank = True, null = True, default = None)
	price = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
	image = models.ImageField(upload_to = 'processors', default = None, blank = True, null = True)
	manufacturer = models.CharField(max_length = 200, blank = True, null = True, default = None)

	def __str__(self):
		return '%s %s %s' % (self.manufacturer, self.model, self.socket)

	class Meta:
		verbose_name = 'Процессор'
		verbose_name_plural = 'Процессоры'

class MotherBoard(models.Model):
	model = models.CharField(max_length = 200, blank = True, null = True, default = None)
	socket = models.CharField(max_length = 200, blank = True, null = True, default = None)
	image = models.ImageField(upload_to = 'motherboards/', default = None, blank = True, null = True)
	chipset = models.CharField(max_length = 200, blank = True, null = True, default = None)
	price = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
	manufacturer = models.CharField(max_length = 200, blank = True, null = True, default = None)
	def __str__(self):
		return '%s %s %s' % (self.manufacturer, self.model, self.socket)

	class Meta:
		verbose_name = 'Материнская плата'
		verbose_name_plural = 'Материнские платы'


class HardDisk(models.Model):
	model = models.CharField(max_length = 200, blank = True, null = True, default = None)
	memory = models.IntegerField(default = None, blank = True, null = True)
	price = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
	image = models.ImageField(upload_to = 'hards/', default = None, blank = True, null = True)
	manufacturer = models.CharField(max_length = 200, blank = True, null = True, default = None)
	def __str__(self):
		return '%s %s %s' % (self.manufacturer, self.model, self.memory)

	class Meta:
		verbose_name = 'Жесткий диск'
		verbose_name_plural = 'Жесткие диски'

class Ram(models.Model):
	model = models.CharField(max_length = 200, blank = True, null = True, default = None)
	type_of_ram = models.CharField(max_length = 20, blank = True, null = True, default = None)
	nmb = models.SmallIntegerField(default = None, blank = True, null = True)
	price = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
	memory = models.IntegerField(default = None, blank = True, null = True)
	image = models.ImageField(upload_to = 'rams/', default = None, blank = True, null = True)
	manufacturer = models.CharField(max_length = 200, blank = True, null = True, default = None)
	def __str__(self):
		return '%s %s' % (self.manufacturer, self.model)

	class Meta:
		verbose_name = 'ОЗУ'
		verbose_name_plural = 'ОЗУ'


	def save(self, *args, **kwargs):
		self.price = self.price*self.nmb


		super(Ram, self).save(*args, **kwargs)

class GraphicsCard(models.Model):
	model = models.CharField(max_length = 200, blank = True, null = True, default = None)
	memory = models.IntegerField(default = None, blank = True, null = True)
	price = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
	image = models.ImageField(upload_to = 'graphics/', default = None, blank = True, null = True)
	manufacturer = models.CharField(max_length = 200, blank = True, null = True, default = None)
	def __str__(self):
		return '%s %s %sGB' % (self.manufacturer, self.model, self.memory)

	class Meta:
		verbose_name = 'Видеокарта'
		verbose_name_plural = 'Видеокарты'

class Corpus(models.Model):
	model = models.CharField(max_length = 64, blank = True, null = True, default = None)
	color = models.CharField(max_length = 64, blank = True, null = True, default = None)
	gabarites = models.CharField(max_length = 200, blank = True, null = True, default = None)
	price = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
	image = models.ImageField(upload_to = 'corpuses/', default = None, blank = True, null = True)
	manufacturer = models.CharField(max_length = 200, blank = True, null = True, default = None)
	def __str__(self):
		return '%s %s %s' % (self.manufacturer, self.model, self.color)

	class Meta:
		verbose_name = 'Корпус'
		verbose_name_plural = 'Корпусы'

class PowerSupply(models.Model):
	model = models.CharField(max_length = 200, blank = True, null = True, default = None)
	power = models.IntegerField(default = None, blank = True, null = True)
	price = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
	image = models.ImageField(upload_to = 'powers/', default = None, blank = True, null = True)
	manufacturer = models.CharField(max_length = 200, blank = True, null = True, default = None)
	def __str__(self):
		return '%s %s %s' % (self.manufacturer, self.model, self.power)

	class Meta:
		verbose_name = 'Блок питания'
		verbose_name_plural = 'Блоки питания'

class Cooler(models.Model):
	model = models.CharField(max_length = 200, blank = True, null = True, default = None)
	price = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
	image = models.ImageField(upload_to = 'coolers/', default = None, blank = True, null = True)
	manufacturer = models.CharField(max_length = 200, blank = True, null = True, default = None)
	def __str__(self):
		return '%s %s' % (self.manufacturer, self.model)

	class Meta:
		verbose_name = 'Куллер'
		verbose_name_plural = 'Куллеры'

class Computer(models.Model):
	name = models.CharField(max_length = 200, blank = True, null = True, default = None)
	price = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0, blank = True, null = True)# общая стоимость всех комплектующих
	os = models.CharField(max_length = 64, blank = True, null = True, default = None)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now_add = True)
	is_active = models.BooleanField(default = True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default = None)
	processor = models.OneToOneField(Processor, on_delete = models.CASCADE, default = None)
	ram = models.OneToOneField(Ram, on_delete = models.CASCADE, default = None)
	graphics = models.OneToOneField(GraphicsCard, on_delete = models.CASCADE, default = None)
	corpus = models.OneToOneField(Corpus, on_delete = models.CASCADE, default = None)
	power = models.OneToOneField(PowerSupply, on_delete = models.CASCADE, default = None)
	cooler = models.OneToOneField(Cooler, on_delete = models.CASCADE, default = None)
	motherboard = models.OneToOneField(MotherBoard, on_delete = models.CASCADE, default = None, blank = True, null = True)
	hard = models.OneToOneField(HardDisk, on_delete = models.CASCADE, default = None, blank = True, null = True)

	def __str__(self):
		return '%s %stg' % (self.name, self.price)

	class Meta:
		verbose_name = 'Сборка'
		verbose_name_plural = 'Сборки'

	def save(self, *args, **kwargs):
		self.price = self.processor.price + self.ram.price + self.graphics.price + self.corpus.price + self.power.price + self.cooler.price


		super(Computer, self).save(*args, **kwargs)
