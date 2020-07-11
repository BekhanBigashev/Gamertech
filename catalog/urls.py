from django.contrib import admin
from django.urls import path, include
from  .views import*
from django.views.generic import RedirectView
urlpatterns = [
   
   path('computers/', ComputerListView.as_view(), name = 'computer_list'),
   path('', index, name = 'product_list'),
   path('computers/<int:pk>/', ComputerDetailView.as_view(), name = 'computer_detail'),
   path('processors/', ProcessorListView.as_view(), name = 'processor_list'),
   path('processors/<int:pk>/', ProcessorDetailView.as_view(), name = 'processor_detail'),
   path('motherboards/', MotherBoardListView.as_view(), name = 'motherboard_list'),
   path('motherboards/<int:pk>/', MotherBoardDetailView.as_view(), name = 'motherboard_detail'),
   path('graphicscards/', GraphicsCardListView.as_view(), name = 'graphicscard_list'),
   path('graphicscards/<int:pk>/', GraphicsCardDetailView.as_view(), name = 'graphicscard_detail'),
   path('rams/', RamListView.as_view(), name = 'ram_list'),
   path('rams/<int:pk>/', RamDetailView.as_view(), name = 'ram_detail'),
   path('harddisks/', HardDiskListView.as_view(), name = 'harddisk_list'),
   path('harddisks/<int:pk>/', HardDiskDetailView.as_view(), name = 'harddisk_detail'),
   path('powersupplies/', PowerSupplyListView.as_view(), name = 'powersupply_list'),
   path('powersupplies/<int:pk>/', PowerSupplyDetailView.as_view(), name = 'powersupply_detail'),
   path('coolers/', CoolerListView.as_view(), name = 'cooler_list'),
   path('coolers/<int:pk>/', CoolerDetailView.as_view(), name = 'cooler_detail'),
   path('corpuses/', CorpusListView.as_view(), name = 'corpus_list'),
   path('corpuses/<int:pk>/', CorpusDetailView.as_view(), name = 'corpus_detail'),
]
