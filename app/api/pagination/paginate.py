from fastapi.encoders import jsonable_encoder
from api.pagination.pagination_schema import *


def paginate(page_params: PageParams, query):
    print(query)
    offset_min = page_params.page * page_params.size
    offset_max = (page_params.page + 1) * page_params.size
    paginated_query = query[offset_min:offset_max]
    return {
        'total': len(query) + 1,
        'page': page_params.page,
        'size': page_params.size,
        'results': [jsonable_encoder(item) for item in paginated_query],
    }
