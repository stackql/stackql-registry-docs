---
title: aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - aliases
  - directory
  - googleadmin    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and manage Google Workspace users and groups using SQL.
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleadmin.directory.aliases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `aliases` | `array` |
| `etag` | `string` |
| `kind` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `group_aliases_list` | `SELECT` | `groupKey` | Lists all aliases for a group. |
| `user_aliases_list` | `SELECT` | `userKey` | Lists all aliases for a user. |
| `group_aliases_insert` | `INSERT` | `groupKey` | Adds an alias for the group. |
| `user_aliases_insert` | `INSERT` | `userKey` | Adds an alias. |
| `group_aliases_delete` | `DELETE` | `alias, groupKey` | Removes an alias. |
| `user_aliases_delete` | `DELETE` | `alias, userKey` | Removes an alias. |
| `user_aliases_watch` | `EXEC` | `userKey` | Watches for changes in users list. |
