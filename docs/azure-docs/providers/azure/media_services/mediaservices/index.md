---
title: mediaservices
hide_title: false
hide_table_of_contents: false
keywords:
  - mediaservices
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
<tr><td><b>Name</b></td><td><code>mediaservices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.media_services.mediaservices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` |  |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of the Media Services account. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, api-version, resourceGroupName, subscriptionId` | Get the details of a Media Services account |
| `list` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | List Media Services accounts in the resource group |
| `list_by_subscription` | `SELECT` | `api-version, subscriptionId` | List Media Services accounts in the subscription. |
| `create_or_update` | `INSERT` | `accountName, api-version, resourceGroupName, subscriptionId` | Creates or updates a Media Services account |
| `delete` | `DELETE` | `accountName, api-version, resourceGroupName, subscriptionId` | Deletes a Media Services account |
| `_list` | `EXEC` | `api-version, resourceGroupName, subscriptionId` | List Media Services accounts in the resource group |
| `_list_by_subscription` | `EXEC` | `api-version, subscriptionId` | List Media Services accounts in the subscription. |
| `sync_storage_keys` | `EXEC` | `accountName, api-version, resourceGroupName, subscriptionId` | Synchronizes storage account keys for a storage account associated with the Media Service account. |
| `update` | `EXEC` | `accountName, api-version, resourceGroupName, subscriptionId` | Updates an existing Media Services account |
