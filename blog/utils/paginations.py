from rest_framework.pagination import PageNumberPagination

class Pagination(PageNumberPagination):
    """Custom paginator that displays 6 items per page."""
    page_size = 6  
    page_query_param = "page" 
    page_size_query_param = None 
    max_page_size = 6 