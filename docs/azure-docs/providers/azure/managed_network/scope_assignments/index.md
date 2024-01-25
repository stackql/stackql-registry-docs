---
title: scope_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - scope_assignments
  - managed_network
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
<tr><td><b>Name</b></td><td><code>scope_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_network.scope_assignments</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `scope, scopeAssignmentName` | Get the specified scope assignment. |
| `list` | `SELECT` | `scope` | Get the specified scope assignment. |
| `create_or_update` | `INSERT` | `scope, scopeAssignmentName` | Creates a scope assignment. |
| `delete` | `DELETE` | `scope, scopeAssignmentName` | Deletes a scope assignment. |
| `_list` | `EXEC` | `scope` | Get the specified scope assignment. |
