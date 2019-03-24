from rest_framework.pagination import LimitOffsetPagination


class PaginationWithMaxlimit(LimitOffsetPagination):
    max_limit = 10
