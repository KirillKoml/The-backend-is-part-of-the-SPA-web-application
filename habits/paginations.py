from rest_framework.pagination import PageNumberPagination


class UserRetrievePagination(PageNumberPagination):
    page_size = 5
