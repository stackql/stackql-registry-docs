---
title: scope_access_review_history_definition
hide_title: false
hide_table_of_contents: false
keywords:
  - scope_access_review_history_definition
  - authorization
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
<tr><td><b>Name</b></td><td><code>scope_access_review_history_definition</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.authorization.scope_access_review_history_definition</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ScopeAccessReviewHistoryDefinition_Create` | `INSERT` | `historyDefinitionId, scope` | Create a scheduled or one-time Access Review History Definition |
| `ScopeAccessReviewHistoryDefinition_DeleteById` | `DELETE` | `historyDefinitionId, scope` | Delete an access review history definition |
