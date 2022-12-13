---
title: scope_access_review_instance
hide_title: false
hide_table_of_contents: false
keywords:
  - scope_access_review_instance
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
<tr><td><b>Name</b></td><td><code>scope_access_review_instance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.authorization.scope_access_review_instance</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ScopeAccessReviewInstance_ApplyDecisions` | `EXEC` | `id, scheduleDefinitionId, scope` | An action to apply all decisions for an access review instance. |
| `ScopeAccessReviewInstance_RecordAllDecisions` | `EXEC` | `id, scheduleDefinitionId, scope` | An action to approve/deny all decisions for a review with certain filters. |
| `ScopeAccessReviewInstance_ResetDecisions` | `EXEC` | `id, scheduleDefinitionId, scope` | An action to reset all decisions for an access review instance. |
| `ScopeAccessReviewInstance_SendReminders` | `EXEC` | `id, scheduleDefinitionId, scope` | An action to send reminders for an access review instance. |
| `ScopeAccessReviewInstance_Stop` | `EXEC` | `id, scheduleDefinitionId, scope` | An action to stop an access review instance. |
