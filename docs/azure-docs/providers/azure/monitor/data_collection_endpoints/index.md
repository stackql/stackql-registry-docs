---
title: data_collection_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - data_collection_endpoints
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
<tr><td><b>Name</b></td><td><code>data_collection_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.data_collection_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified ID of the resource. |
| `name` | `string` | The name of the resource. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | The type of the resource. |
| `etag` | `string` | Resource entity tag (ETag). |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `location` | `string` | The geo-location where the resource lives. |
| `properties` | `object` | Resource properties. |
| `kind` | `string` | The kind of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `DataCollectionEndpoints_Get` | `SELECT` | `dataCollectionEndpointName, resourceGroupName, subscriptionId` |
| `DataCollectionEndpoints_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` |
| `DataCollectionEndpoints_ListBySubscription` | `SELECT` | `subscriptionId` |
| `DataCollectionEndpoints_Create` | `INSERT` | `dataCollectionEndpointName, resourceGroupName, subscriptionId, data__location` |
| `DataCollectionEndpoints_Delete` | `DELETE` | `dataCollectionEndpointName, resourceGroupName, subscriptionId` |
| `DataCollectionEndpoints_Update` | `EXEC` | `dataCollectionEndpointName, resourceGroupName, subscriptionId` |
