---
title: access_review_history_definition_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - access_review_history_definition_instances
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
<tr><td><b>Name</b></td><td><code>access_review_history_definition_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.authorization.access_review_history_definition_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The access review history definition instance id. |
| `name` | `string` | The access review history definition instance unique id. |
| `properties` | `object` | Access Review History Definition Instance properties. |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `AccessReviewHistoryDefinitionInstances_List` | `SELECT` | `historyDefinitionId, subscriptionId` |
