---
title: signalr
hide_title: false
hide_table_of_contents: false
keywords:
  - signalr
  - signalr
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
<tr><td><b>Name</b></td><td><code>signalr</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.signalr.signalr</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | A class represent managed identities used for request and response |
| `kind` | `string` | The kind of the service, it can be SignalR or RawWebSockets |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | A class that describes the properties of the resource |
| `sku` | `object` | The billing information of the resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SignalR_Get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Get the resource and its properties. |
| `SignalR_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Handles requests to list all resources in a resource group. |
| `SignalR_ListBySubscription` | `SELECT` | `subscriptionId` | Handles requests to list all resources in a subscription. |
| `SignalR_CreateOrUpdate` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Create or update a resource. |
| `SignalR_Delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Operation to delete a resource. |
| `SignalR_CheckNameAvailability` | `EXEC` | `location, subscriptionId, data__name, data__type` | Checks that the resource name is valid and is not already in use. |
| `SignalR_ListKeys` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Get the access keys of the resource. |
| `SignalR_ListSkus` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | List all available skus of the resource. |
| `SignalR_RegenerateKey` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Regenerate the access key for the resource. PrimaryKey and SecondaryKey cannot be regenerated at the same time. |
| `SignalR_Restart` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Operation to restart a resource. |
| `SignalR_Update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Operation to update an exiting resource. |
