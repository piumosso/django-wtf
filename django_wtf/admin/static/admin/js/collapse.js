(function($) {
	$(document).ready(function() {
		// Add anchor tag for Show/Hide link
		$(".form__fieldset.collapse").each(function(i, elem) {
			// Don't hide if fields in this fieldset have errors
			if ($(elem).find(".form__row_errors").length == 0) {
				$(elem).addClass("collapsed").find(".module__header").first().append(' (<a id="fieldsetcollapser' +
					i +'" class="form__fieldset-collapse-toggle" href="#">' + gettext("Show") +
					'</a>)');
			}
		});
		// Add toggle to anchor tag
		$(".form__fieldset.collapse .form__fieldset-collapse-toggle").toggle(
			function() { // Show
				$(this).text(gettext("Hide")).closest("fieldset").removeClass("collapsed").trigger("show.fieldset", [$(this).attr("id")]);
				return false;
			},
			function() { // Hide
				$(this).text(gettext("Show")).closest("fieldset").addClass("collapsed").trigger("hide.fieldset", [$(this).attr("id")]);
				return false;
			}
		);
	});
})(django.jQuery);
