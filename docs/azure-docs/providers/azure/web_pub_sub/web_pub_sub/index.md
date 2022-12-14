---
title: web_pub_sub
hide_title: false
hide_table_of_contents: false
keywords:
  - web_pub_sub
  - web_pub_sub
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
<tr><td><b>Name</b></td><td><code>web_pub_sub</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.web_pub_sub.web_pub_sub</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `sku` | `object` | The billing information of the resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `identity` | `object` | A class represent managed identities used for request and response |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | A class that describes the properties of the resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WebPubSub_Get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Get the resource and its properties. |
| `WebPubSub_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Handles requests to list all resources in a resource group. |
| `WebPubSub_ListBySubscription` | `SELECT` | `subscriptionId` | Handles requests to list all resources in a subscription. |
| `WebPubSub_CreateOrUpdate` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Create or update a resource. |
| `WebPubSub_Delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Operation to delete a resource. |
| `WebPubSub_CheckNameAvailability` | `EXEC` | `location, subscriptionId, data__name, data__type` | Checks that the resource name is valid and is not already in use. |
| `WebPubSub_ListKeys` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Get the access keys of the resource. |
| `WebPubSub_ListSkus` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | List all available skus of the resource. |
| `WebPubSub_RegenerateKey` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Regenerate the access key for the resource. PrimaryKey and SecondaryKey cannot be regenerated at the same time. |
| `WebPubSub_Restart` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Operation to restart a resource. |
| `WebPubSub_Update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Operation to update an exiting resource. |
