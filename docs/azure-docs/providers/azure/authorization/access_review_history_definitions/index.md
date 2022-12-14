---
title: access_review_history_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - access_review_history_definitions
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
<tr><td><b>Name</b></td><td><code>access_review_history_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.authorization.access_review_history_definitions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The access review history definition id. |
| `name` | `string` | The access review history definition unique id. |
| `properties` | `object` | Access Review History Instances. |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AccessReviewHistoryDefinitions_List` | `SELECT` | `subscriptionId` | Lists the accessReviewHistoryDefinitions available from this provider, definition instances are only available for 30 days after creation. |
| `AccessReviewHistoryDefinitions_GetById` | `EXEC` | `historyDefinitionId, subscriptionId` | Get access review history definition by definition Id |
