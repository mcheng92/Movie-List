from django.urls import path

from .views import (
    CastList,
    CastDetail,
    CastCreate,
    CastUpdate,
    CastDelete
)

urlpatterns = [
    path('', CastList.as_view(), name='cast-index'),
    path('<int:pk>', CastDetail.as_view(), name='cast-detail'),
    path('add', CastCreate.as_view(), name='add-cast'),
    path('edit/<int:pk>', CastUpdate.as_view(), name='edit-cast'),
    path('delete/<int:pk>', CastDelete.as_view(), name='delete-cast')

]
