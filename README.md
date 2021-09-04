## persistent_defaults

for erpnext persistent session defaults
installing App to ERPNext

`bench get-app persistent_defaults https://github.com/michaeleino/erpnext-persistent_defaults.git`

`bench install-app persistent_defaults`

## ERPNext modification for this to work:
  - User should be linked to an Employee, and company field is set correctly.

  - For the letter_head to work, go to  **Customize Form > Employee(Hr)**  
  Create a field with label `Default Letter Head` of type link to `Letter Head` set in options

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

GNU3
