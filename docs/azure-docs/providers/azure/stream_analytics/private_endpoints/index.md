---
title: private_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoints
  - stream_analytics
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
<tr><td><b>Name</b></td><td><code>private_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.stream_analytics.private_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Unique opaque string (generally a GUID) that represents the metadata state of the resource (private endpoint) and changes whenever the resource is updated. Required on PUT (CreateOrUpdate) requests. |
| `properties` | `object` | The properties associated with a private endpoint. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterName, privateEndpointName, resourceGroupName, subscriptionId` | Gets information about the specified Private Endpoint. |
| `list_by_cluster` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Lists the private endpoints in the cluster. |
| `create_or_update` | `INSERT` | `clusterName, privateEndpointName, resourceGroupName, subscriptionId` | Creates a Stream Analytics Private Endpoint or replaces an already existing Private Endpoint. |
| `delete` | `DELETE` | `clusterName, privateEndpointName, resourceGroupName, subscriptionId` | Delete the specified private endpoint. |
| `_list_by_cluster` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Lists the private endpoints in the cluster. |
