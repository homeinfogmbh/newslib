# ./newslib/dom.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:ab67edf53b6879c2b49324f31ca9c231f572488f
# Generated 2022-11-21 12:03:58.323255 by PyXB version 1.2.7-DEV using Python 3.10.8.final.0
# Namespace http://xml.homeinfo.de/schema/news

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:3289544c-698c-11ed-8416-7427eaa9df7d')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.7-DEV'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://xml.homeinfo.de/schema/news', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, fallback_namespace=None, location_base=None, default_namespace=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword fallback_namespace An absent L{pyxb.Namespace} instance
    to use for unqualified names when there is no default namespace in
    scope.  If unspecified or C{None}, the namespace of the module
    containing this function will be used, if it is an absent
    namespace.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.

    @keyword default_namespace An alias for @c fallback_namespace used
    in PyXB 1.1.4 through 1.2.6.  It behaved like a default namespace
    only for absent namespaces.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=fallback_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, fallback_namespace=None, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, fallback_namespace)


# Atomic simple type: {http://xml.homeinfo.de/schema/news}Provider
class Provider (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                Verfügbare Nachrichtendienste.
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Provider')
    _XSDLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 134, 4)
    _Documentation = '\n                Verfügbare Nachrichtendienste.\n            '
Provider._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Provider, enum_prefix=None)
Provider.DPA = Provider._CF_enumeration.addEnumeration(unicode_value='DPA', tag='DPA')
Provider.HOMEINFO = Provider._CF_enumeration.addEnumeration(unicode_value='HOMEINFO', tag='HOMEINFO')
Provider.spiegel_de = Provider._CF_enumeration.addEnumeration(unicode_value='spiegel.de', tag='spiegel_de')
Provider.welt_de = Provider._CF_enumeration.addEnumeration(unicode_value='welt.de', tag='welt_de')
Provider._InitializeFacetMap(Provider._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Provider', Provider)
_module_typeBindings.Provider = Provider

# Complex type {http://xml.homeinfo.de/schema/news}News with content type ELEMENT_ONLY
class News (pyxb.binding.basis.complexTypeDefinition):
    """
                Liste von Nachrichtenartikeln.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'News')
    _XSDLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 15, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element article uses Python identifier article
    __article = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'article'), 'article', '__httpxml_homeinfo_deschemanews_News_article', True, pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 22, 12), )

    
    article = property(__article.value, __article.set, None, '\n                      Die jeweiligen Nachrichtenartikel.\n                  ')

    
    # Attribute file_preview_token uses Python identifier file_preview_token
    __file_preview_token = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'file_preview_token'), 'file_preview_token', '__httpxml_homeinfo_deschemanews_News_file_preview_token', pyxb.binding.datatypes.string)
    __file_preview_token._DeclarationLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 30, 8)
    __file_preview_token._UseLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 30, 8)
    
    file_preview_token = property(__file_preview_token.value, __file_preview_token.set, None, '\n                    Temporäres Token zur Vorschau der Dateien.\n                ')

    _ElementMap.update({
        __article.name() : __article
    })
    _AttributeMap.update({
        __file_preview_token.name() : __file_preview_token
    })
_module_typeBindings.News = News
Namespace.addCategoryObject('typeBinding', 'News', News)


# Complex type {http://xml.homeinfo.de/schema/news}Attachment with content type SIMPLE
class Attachment (pyxb.binding.basis.complexTypeDefinition):
    """
                Dateianhang.
            """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Attachment')
    _XSDLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 100, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute sha256sum uses Python identifier sha256sum
    __sha256sum = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sha256sum'), 'sha256sum', '__httpxml_homeinfo_deschemanews_Attachment_sha256sum', pyxb.binding.datatypes.string, required=True)
    __sha256sum._DeclarationLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 108, 16)
    __sha256sum._UseLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 108, 16)
    
    sha256sum = property(__sha256sum.value, __sha256sum.set, None, '\n                            SHA-256 Prüfsumme.\n                        ')

    
    # Attribute mimetype uses Python identifier mimetype
    __mimetype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'mimetype'), 'mimetype', '__httpxml_homeinfo_deschemanews_Attachment_mimetype', pyxb.binding.datatypes.string, required=True)
    __mimetype._DeclarationLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 115, 16)
    __mimetype._UseLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 115, 16)
    
    mimetype = property(__mimetype.value, __mimetype.set, None, '\n                            MIME Typ des Bildes.\n                        ')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpxml_homeinfo_deschemanews_Attachment_id', pyxb.binding.datatypes.positiveInteger)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 122, 16)
    __id._UseLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 122, 16)
    
    id = property(__id.value, __id.set, None, '\n                            Datenbank-ID des Bildes.\n                        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __sha256sum.name() : __sha256sum,
        __mimetype.name() : __mimetype,
        __id.name() : __id
    })
_module_typeBindings.Attachment = Attachment
Namespace.addCategoryObject('typeBinding', 'Attachment', Attachment)


# Complex type {http://xml.homeinfo.de/schema/news}Article with content type ELEMENT_ONLY
class Article (pyxb.binding.basis.complexTypeDefinition):
    """
                Ein Nachrichtenartikel.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Article')
    _XSDLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 40, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'title'), 'title', '__httpxml_homeinfo_deschemanews_Article_title', False, pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 47, 12), )

    
    title = property(__title.value, __title.set, None, '\n                      Titel des Artikels.\n                  ')

    
    # Element subtitle uses Python identifier subtitle
    __subtitle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'subtitle'), 'subtitle', '__httpxml_homeinfo_deschemanews_Article_subtitle', False, pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 54, 12), )

    
    subtitle = property(__subtitle.value, __subtitle.set, None, '\n                      Untertitel.\n                  ')

    
    # Element text uses Python identifier text
    __text = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'text'), 'text', '__httpxml_homeinfo_deschemanews_Article_text', False, pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 61, 12), )

    
    text = property(__text.value, __text.set, None, '\n                      Nachrichtentext.\n                  ')

    
    # Element source uses Python identifier source
    __source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'source'), 'source', '__httpxml_homeinfo_deschemanews_Article_source', False, pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 68, 12), )

    
    source = property(__source.value, __source.set, None, '\n                      Quellenangabe.\n                  ')

    
    # Element published uses Python identifier published
    __published = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'published'), 'published', '__httpxml_homeinfo_deschemanews_Article_published', False, pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 75, 12), )

    
    published = property(__published.value, __published.set, None, '\n                      Datum und Uhrzeit der Veröffentlichung.\n                  ')

    
    # Element image uses Python identifier image
    __image = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'image'), 'image', '__httpxml_homeinfo_deschemanews_Article_image', False, pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 82, 12), )

    
    image = property(__image.value, __image.set, None, '\n                      Titelbild.\n                  ')

    
    # Attribute provider uses Python identifier provider
    __provider = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'provider'), 'provider', '__httpxml_homeinfo_deschemanews_Article_provider', _module_typeBindings.Provider, required=True)
    __provider._DeclarationLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 90, 8)
    __provider._UseLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 90, 8)
    
    provider = property(__provider.value, __provider.set, None, '\n                  Datenbank-ID.\n              ')

    _ElementMap.update({
        __title.name() : __title,
        __subtitle.name() : __subtitle,
        __text.name() : __text,
        __source.name() : __source,
        __published.name() : __published,
        __image.name() : __image
    })
    _AttributeMap.update({
        __provider.name() : __provider
    })
_module_typeBindings.Article = Article
Namespace.addCategoryObject('typeBinding', 'Article', Article)


news = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'news'), News, location=pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 12, 4))
Namespace.addCategoryObject('elementBinding', news.name().localName(), news)



News._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'article'), Article, scope=News, documentation='\n                      Die jeweiligen Nachrichtenartikel.\n                  ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 22, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 22, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(News._UseForTag(pyxb.namespace.ExpandedName(None, 'article')), pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 22, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
News._Automaton = _BuildAutomaton()




Article._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'title'), pyxb.binding.datatypes.string, scope=Article, documentation='\n                      Titel des Artikels.\n                  ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 47, 12)))

Article._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'subtitle'), pyxb.binding.datatypes.string, scope=Article, documentation='\n                      Untertitel.\n                  ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 54, 12)))

Article._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'text'), pyxb.binding.datatypes.string, scope=Article, documentation='\n                      Nachrichtentext.\n                  ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 61, 12)))

Article._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'source'), pyxb.binding.datatypes.string, scope=Article, documentation='\n                      Quellenangabe.\n                  ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 68, 12)))

Article._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'published'), pyxb.binding.datatypes.dateTime, scope=Article, documentation='\n                      Datum und Uhrzeit der Veröffentlichung.\n                  ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 75, 12)))

Article._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'image'), Attachment, scope=Article, documentation='\n                      Titelbild.\n                  ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 82, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 54, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 68, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 75, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 82, 12))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Article._UseForTag(pyxb.namespace.ExpandedName(None, 'title')), pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 47, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Article._UseForTag(pyxb.namespace.ExpandedName(None, 'subtitle')), pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 54, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Article._UseForTag(pyxb.namespace.ExpandedName(None, 'text')), pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 61, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Article._UseForTag(pyxb.namespace.ExpandedName(None, 'source')), pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 68, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Article._UseForTag(pyxb.namespace.ExpandedName(None, 'published')), pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 75, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Article._UseForTag(pyxb.namespace.ExpandedName(None, 'image')), pyxb.utils.utility.Location('/home/neumann/Projekte/newslib/news.xsd', 82, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Article._Automaton = _BuildAutomaton_()

