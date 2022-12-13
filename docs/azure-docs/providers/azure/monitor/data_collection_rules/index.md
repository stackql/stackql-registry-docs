---
title: data_collection_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - data_collection_rules
  - monitor
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
<tr><td><b>Name</b></td><td><code>data_collection_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.data_collection_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified ID of the resource. |
| `name` | `string` | The name of the resource. |
| `tags` | `object` | Resource tags. |
| `etag` | `string` | Resource entity tag (ETag). |
| `kind` | `string` | The kind of the resource. |
| `location` | `string` | The geo-location where the resource lives. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. |
| `properties` | `object` | Resource properties. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `DataCollectionRules_Get` | `SELECT` | `dataCollectionRuleName, resourceGroupName, subscriptionId` |
| `DataCollectionRules_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` |
| `DataCollectionRules_ListBySubscription` | `SELECT` | `subscriptionId` |
| `DataCollectionRules_Create` | `INSERT` | `dataCollectionRuleName, resourceGroupName, subscriptionId, data__location` |
| `DataCollectionRules_Delete` | `DELETE` | `dataCollectionRuleName, resourceGroupName, subscriptionId` |
| `DataCollectionRules_Update` | `EXEC` | `dataCollectionRuleName, resourceGroupName, subscriptionId` |
