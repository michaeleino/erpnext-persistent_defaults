# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "persistent_defaults"
app_title = "Persistent Defaults"
app_publisher = "Michael F"
app_description = "for erpnext persistent session defaults"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "michaeleino@hotmail.com"
app_license = "GNU3"

#app_include_css = "assets/persistent_defaults/css/custom.css"
# app_include_css = "/assets/css/custom_app.css"
app_include_js = "/assets/js/persistent_defaults.js"

web_include_js = "/assets/persistent_defaults/js/clear_persistent_defaults.js"


# boot_session = "persistent_defaults.overrides.start_session_defaults"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/persistent_defaults/css/persistent_defaults.css"
# app_include_js = "/assets/persistent_defaults/js/persistent_defaults.js"

# include js, css files in header of web template
# web_include_css = "/assets/persistent_defaults/css/persistent_defaults.css"
# web_include_js = "/assets/persistent_defaults/js/persistent_defaults.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "persistent_defaults.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "persistent_defaults.install.before_install"
# after_install = "persistent_defaults.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "persistent_defaults.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"persistent_defaults.tasks.all"
# 	],
# 	"daily": [
# 		"persistent_defaults.tasks.daily"
# 	],
# 	"hourly": [
# 		"persistent_defaults.tasks.hourly"
# 	],
# 	"weekly": [
# 		"persistent_defaults.tasks.weekly"
# 	]
# 	"monthly": [
# 		"persistent_defaults.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "persistent_defaults.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "persistent_defaults.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "persistent_defaults.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]
