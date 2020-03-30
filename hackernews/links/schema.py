import graphene
from graphene_django import DjangoObjectType

from .models import Link


class LinkType(DjangoObjectType):
    class Meta:
        model = Link



class Query(graphene.ObjectType):

    links = graphene.List(LinkType)
    linksfield = graphene.Field(LinkType,id =graphene.String())


    def resolve_links(self, info,**kwargs):

        return Link.objects.all()

    def resolve_linksfield(self,info,id)    :
        return Link.objects.get(pk = id)
