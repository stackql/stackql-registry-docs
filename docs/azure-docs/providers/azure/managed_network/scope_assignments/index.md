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
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ScopeAssignments_Get` | `SELECT` | `scope, scopeAssignmentName` | Get the specified scope assignment. |
| `ScopeAssignments_List` | `SELECT` | `scope` | Get the specified scope assignment. |
| `ScopeAssignments_CreateOrUpdate` | `INSERT` | `scope, scopeAssignmentName` | Creates a scope assignment. |
| `ScopeAssignments_Delete` | `DELETE` | `scope, scopeAssignmentName` | Deletes a scope assignment. |
