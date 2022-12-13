---
title: storage_insight_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_insight_configs
  - operational_insights
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
<tr><td><b>Name</b></td><td><code>storage_insight_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.operational_insights.storage_insight_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `eTag` | `string` | The ETag of the storage insight. |
| `properties` | `object` | Storage insight properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `StorageInsightConfigs_Get` | `SELECT` | `resourceGroupName, storageInsightName, subscriptionId, workspaceName` | Gets a storage insight instance. |
| `StorageInsightConfigs_ListByWorkspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Lists the storage insight instances within a workspace |
| `StorageInsightConfigs_CreateOrUpdate` | `INSERT` | `resourceGroupName, storageInsightName, subscriptionId, workspaceName` | Create or update a storage insight. |
| `StorageInsightConfigs_Delete` | `DELETE` | `resourceGroupName, storageInsightName, subscriptionId, workspaceName` | Deletes a storageInsightsConfigs resource |
