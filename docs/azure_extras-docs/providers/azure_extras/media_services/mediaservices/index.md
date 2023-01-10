---
title: mediaservices
hide_title: false
hide_table_of_contents: false
keywords:
  - mediaservices
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
<tr><td><b>Name</b></td><td><code>mediaservices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.media_services.mediaservices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `identity` | `object` |  |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of the Media Services account. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Mediaservices_Get` | `SELECT` | `accountName, api-version, resourceGroupName, subscriptionId` | Get the details of a Media Services account |
| `Mediaservices_List` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | List Media Services accounts in the resource group |
| `Mediaservices_ListBySubscription` | `SELECT` | `api-version, subscriptionId` | List Media Services accounts in the subscription. |
| `Mediaservices_CreateOrUpdate` | `INSERT` | `accountName, api-version, resourceGroupName, subscriptionId` | Creates or updates a Media Services account |
| `Mediaservices_Delete` | `DELETE` | `accountName, api-version, resourceGroupName, subscriptionId` | Deletes a Media Services account |
| `Mediaservices_ListEdgePolicies` | `EXEC` | `accountName, api-version, resourceGroupName, subscriptionId` | List all the media edge policies associated with the Media Services account. |
| `Mediaservices_SyncStorageKeys` | `EXEC` | `accountName, api-version, resourceGroupName, subscriptionId` | Synchronizes storage account keys for a storage account associated with the Media Service account. |
| `Mediaservices_Update` | `EXEC` | `accountName, api-version, resourceGroupName, subscriptionId` | Updates an existing Media Services account |
