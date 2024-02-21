
from django.urls import path
from .views import (
    UserCreateApiView,
    UserUpdateApiView, 
    UserRetrieveApiView,
    UserDeleteApiView
)

urlpatterns = [
    path('create-user/', UserCreateApiView.as_view()),
    path('update-user/<uuid:pk>/', UserUpdateApiView.as_view()),
    path('retrieve-user/<uuid:pk>/', UserRetrieveApiView.as_view()),
    path('delete/', UserDeleteApiView.as_view())
]

# df= ## read_excel('ssdd.xlsx')

# for index, row in df.iterrows():
#     print(row)
#     print(row[3])
#     print(row.loc(3))
#     print(row.iloc(3))
