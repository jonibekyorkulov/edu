from django.urls import path
from .views import UserCreateApiView

urlpatterns = [
    path('create-user/', UserCreateApiView.as_view())
]

# df= ## read_excel('ssdd.xlsx')

# for index, row in df.iterrows():
#     print(row)
#     print(row[3])
#     print(row.loc(3))
#     print(row.iloc(3))
