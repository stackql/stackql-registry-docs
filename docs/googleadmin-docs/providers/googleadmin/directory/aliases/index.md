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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="googleadmin.directory.aliases" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="aliases" /> | `array` |
| <CopyableCode code="etag" /> | `string` |
| <CopyableCode code="kind" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="group_aliases_list" /> | `SELECT` | <CopyableCode code="groupKey" /> | Lists all aliases for a group. |
| <CopyableCode code="user_aliases_list" /> | `SELECT` | <CopyableCode code="userKey" /> | Lists all aliases for a user. |
| <CopyableCode code="group_aliases_insert" /> | `INSERT` | <CopyableCode code="groupKey" /> | Adds an alias for the group. |
| <CopyableCode code="user_aliases_insert" /> | `INSERT` | <CopyableCode code="userKey" /> | Adds an alias. |
| <CopyableCode code="group_aliases_delete" /> | `DELETE` | <CopyableCode code="alias, groupKey" /> | Removes an alias. |
| <CopyableCode code="user_aliases_delete" /> | `DELETE` | <CopyableCode code="alias, userKey" /> | Removes an alias. |
| <CopyableCode code="user_aliases_watch" /> | `EXEC` | <CopyableCode code="userKey" /> | Watches for changes in users list. |
