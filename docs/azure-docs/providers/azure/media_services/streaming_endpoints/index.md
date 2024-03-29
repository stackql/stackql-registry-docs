---
title: streaming_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - streaming_endpoints
  - media_services
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
<tr><td><b>Name</b></td><td><code>streaming_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.media_services.streaming_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The streaming endpoint properties. |
| `sku` | `object` | The streaming endpoint current sku. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, api-version, resourceGroupName, streamingEndpointName, subscriptionId` | Gets a streaming endpoint. |
| `list` | `SELECT` | `accountName, api-version, resourceGroupName, subscriptionId` | Lists the streaming endpoints in the account. |
| `create` | `INSERT` | `accountName, api-version, resourceGroupName, streamingEndpointName, subscriptionId` | Creates a streaming endpoint. |
| `delete` | `DELETE` | `accountName, api-version, resourceGroupName, streamingEndpointName, subscriptionId` | Deletes a streaming endpoint. |
| `_list` | `EXEC` | `accountName, api-version, resourceGroupName, subscriptionId` | Lists the streaming endpoints in the account. |
| `_skus` | `EXEC` | `accountName, api-version, resourceGroupName, streamingEndpointName, subscriptionId` | List streaming endpoint supported skus. |
| `async_operation` | `EXEC` | `accountName, api-version, operationId, resourceGroupName, subscriptionId` | Get a streaming endpoint operation status. |
| `operation_location` | `EXEC` | `accountName, api-version, operationId, resourceGroupName, streamingEndpointName, subscriptionId` | Get a streaming endpoint operation status. |
| `scale` | `EXEC` | `accountName, api-version, resourceGroupName, streamingEndpointName, subscriptionId` | Scales an existing streaming endpoint. |
| `skus` | `EXEC` | `accountName, api-version, resourceGroupName, streamingEndpointName, subscriptionId` | List streaming endpoint supported skus. |
| `start` | `EXEC` | `accountName, api-version, resourceGroupName, streamingEndpointName, subscriptionId` | Starts an existing streaming endpoint. |
| `stop` | `EXEC` | `accountName, api-version, resourceGroupName, streamingEndpointName, subscriptionId` | Stops an existing streaming endpoint. |
| `update` | `EXEC` | `accountName, api-version, resourceGroupName, streamingEndpointName, subscriptionId` | Updates a existing streaming endpoint. |
