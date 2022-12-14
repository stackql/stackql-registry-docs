---
title: entities
hide_title: false
hide_table_of_contents: false
keywords:
  - entities
  - security_insights
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
<tr><td><b>Name</b></td><td><code>entities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_insights.entities</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `kind` | `string` | The kind of the entity |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Entities_Get` | `SELECT` | `entityId, resourceGroupName, subscriptionId, workspaceName` | Gets an entity. |
| `Entities_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets all entities. |
| `Entities_Expand` | `EXEC` | `entityId, resourceGroupName, subscriptionId, workspaceName` | Expands an entity. |
| `Entities_GetInsights` | `EXEC` | `entityId, resourceGroupName, subscriptionId, workspaceName, data__endTime, data__startTime` | Execute Insights for an entity. |
| `Entities_Queries` | `EXEC` | `entityId, kind, resourceGroupName, subscriptionId, workspaceName` | Get Insights and Activities for an entity. |
