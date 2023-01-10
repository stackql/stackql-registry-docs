---
title: streaming_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - streaming_endpoints
  - media_services
  - azure_extras    
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
<tr><td><b>Id</b></td><td><code>azure_extras.media_services.streaming_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The streaming endpoint properties. |
| `sku` | `object` | The streaming endpoint current sku. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `StreamingEndpoints_Get` | `SELECT` | `accountName, api-version, resourceGroupName, streamingEndpointName, subscriptionId` | Gets a streaming endpoint. |
| `StreamingEndpoints_List` | `SELECT` | `accountName, api-version, resourceGroupName, subscriptionId` | Lists the streaming endpoints in the account. |
| `StreamingEndpoints_Create` | `INSERT` | `accountName, api-version, resourceGroupName, streamingEndpointName, subscriptionId` | Creates a streaming endpoint. |
| `StreamingEndpoints_Delete` | `DELETE` | `accountName, api-version, resourceGroupName, streamingEndpointName, subscriptionId` | Deletes a streaming endpoint. |
| `StreamingEndpoints_AsyncOperation` | `EXEC` | `accountName, api-version, operationId, resourceGroupName, subscriptionId` | Get a streaming endpoint operation status. |
| `StreamingEndpoints_OperationLocation` | `EXEC` | `accountName, api-version, operationId, resourceGroupName, streamingEndpointName, subscriptionId` | Get a streaming endpoint operation status. |
| `StreamingEndpoints_Scale` | `EXEC` | `accountName, api-version, resourceGroupName, streamingEndpointName, subscriptionId` | Scales an existing streaming endpoint. |
| `StreamingEndpoints_Skus` | `EXEC` | `accountName, api-version, resourceGroupName, streamingEndpointName, subscriptionId` | List streaming endpoint supported skus. |
| `StreamingEndpoints_Start` | `EXEC` | `accountName, api-version, resourceGroupName, streamingEndpointName, subscriptionId` | Starts an existing streaming endpoint. |
| `StreamingEndpoints_Stop` | `EXEC` | `accountName, api-version, resourceGroupName, streamingEndpointName, subscriptionId` | Stops an existing streaming endpoint. |
| `StreamingEndpoints_Update` | `EXEC` | `accountName, api-version, resourceGroupName, streamingEndpointName, subscriptionId` | Updates a existing streaming endpoint. |
