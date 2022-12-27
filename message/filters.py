from django_filters import rest_framework as filters


class SendMessageFiter(filters.FilterSet):
    receiver = filters.CharFilter(lookup_expr='username')


class ReceiveMessageFiter(filters.FilterSet):
    sender = filters.CharFilter(lookup_expr='username')
