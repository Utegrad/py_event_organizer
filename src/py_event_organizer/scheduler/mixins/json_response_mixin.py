from django.core.serializers import json
from django.http import JsonResponse


class JsonResponseMixin(object):
    """
    INCOMPLETE : A mixin used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        :param context:
        :param response_kwargs:
        :return:
        """
        return JsonResponse(self.get_data(context), **response_kwargs)

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps()
        :param context:
        :return:
        """
        return json.dumps(context)
