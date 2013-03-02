<script type="text/javascript">
$(document).ready(function() {
    $("#${w.selector}").${w.jqmethod}(${w.options});
	% if w.events:
	% for k in w.events:
	    % if k=='click' or k=='change':
	        $("#${w.selector} input").bind("${k}", ${w.events[k]});
	    % else:
    	    $("#${w.selector}").bind("${k}", ${w.events[k]});
    	% endif
	% endfor
	% endif
});
</script>


