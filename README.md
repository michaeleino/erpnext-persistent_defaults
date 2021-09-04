## persistent_defaults

for erpnext persistent session defaults
installing App to ERPNext

`bench get-app persistent_defaults https://github.com/michaeleino/erpnext-persistent_defaults.git`

`bench install-app persistent_defaults`

## To update this app ONLY
use bench exlude-app for all apps that needed not to be updated for ex:

   `bench exclude-app erpnext`

   `bench exclude-app frappe`

then run

`bench update`

OR

`git -C apps/persistent_defaults/persistent_defaults pull`

then

`bench update --build --no-backup`

#### License

MIT
