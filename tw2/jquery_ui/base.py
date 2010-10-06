
# TW2 proper imports
import tw2.core as twc
from tw2.core.resources import encoder

# tw2.jquery_core imports
from tw2.jquery_core import JQueryWidget
from tw2.jquery_core.base import jQueryJSLink
from tw2.jquery_core.base import jQueryPluginLinkMixin
from tw2.jquery_core.version import JSLinkMixin

# import from *this* package
from tw2.jquery_ui import defaults

### Links, etc...
class jQueryUIMixin(jQueryPluginLinkMixin):
    dirname = defaults._ui_dirname_
    basename='jquery-ui'
    modname = 'tw2.jquery_ui'

class jQueryUIJSLink(twc.JSLink, jQueryUIMixin):
    subdir = 'js'

class jQueryUIThemeCSSLink(jQueryUIMixin, twc.CSSLink):
    name = twc.Param('(string) Specify the name of the theme that you wish to use.  Default: %s' % defaults._ui_theme_name_, default=defaults._ui_theme_name_)
    @property
    def subdir(self):
        return 'css/%(name)s' % dict(name=self.name)
    extension = 'css'

### Resources
jquery_js = jQueryJSLink()
jquery_ui_css = jQueryUIThemeCSSLink(
    name=defaults._ui_theme_name_, version=defaults._ui_version_)
jquery_ui_catcomplete_js = jQueryUIJSLink(version='custom',
                                          basename='catcomplete')
jquery_ui_js = jQueryUIJSLink(version=defaults._ui_version_)
jquery_ui = jQueryJSLink(resources = [jquery_ui_css, jquery_ui_js])

### Widgets
class JQueryUIWidget(JQueryWidget):
    """ Base JQueryUIWidget """
    resources = [ jquery_js, jquery_ui_js, jquery_ui_css ]

    jqmethod = twc.Variable("(str) Name of this widget's jQuery init method")

    options = twc.Param(
        '(dict) A dict of options to pass to the widget', default={})

    # TODO - Refactor this out to tw2.jquery_core
    # http://github.com/ralphbean/tw2.jquery_core/commit/7f0071d0b92ba518cb7bee82c9bcbb3333f2e8a3
    click = twc.Param(
        '(str) javascript callback for generic click event', default=None)
    
    def prepare(self):
        self.options = encoder.encode(self.options)
        super(JQueryUIWidget, self).prepare()