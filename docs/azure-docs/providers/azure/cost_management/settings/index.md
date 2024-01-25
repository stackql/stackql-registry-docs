---
title: settings
hide_title: false
hide_table_of_contents: false
keywords:
  - settings
  - cost_management
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cost_management.settings</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `scope` | List all cost management settings in the requested scope. |
| `delete_by_scope` | `DELETE` | `scope, type` | Delete a setting within the given scope. |
| `_list` | `EXEC` | `scope` | List all cost management settings in the requested scope. |
| `create_or_update_by_scope` | `EXEC` | `scope, type, data__kind` | Create or update a setting within the given scope. |
| `get_by_scope` | `EXEC` | `scope, type` | Get the setting from the given scope by name. |
