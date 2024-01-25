---
title: access_review_instance
hide_title: false
hide_table_of_contents: false
keywords:
  - access_review_instance
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
<tr><td><b>Name</b></td><td><code>access_review_instance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.authorization.access_review_instance</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accept_recommendations` | `EXEC` | `id, scheduleDefinitionId` | An action to accept recommendations for decision in an access review instance. |
| `apply_decisions` | `EXEC` | `id, scheduleDefinitionId, subscriptionId` | An action to apply all decisions for an access review instance. |
| `reset_decisions` | `EXEC` | `id, scheduleDefinitionId, subscriptionId` | An action to reset all decisions for an access review instance. |
| `send_reminders` | `EXEC` | `id, scheduleDefinitionId, subscriptionId` | An action to send reminders for an access review instance. |
| `stop` | `EXEC` | `id, scheduleDefinitionId, subscriptionId` | An action to stop an access review instance. |
