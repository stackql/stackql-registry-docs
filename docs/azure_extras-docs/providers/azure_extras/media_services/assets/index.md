---
title: assets
hide_title: false
hide_table_of_contents: false
keywords:
  - assets
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
<tr><td><b>Name</b></td><td><code>assets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.media_services.assets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | The Asset properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Assets_Get` | `SELECT` | `accountName, api-version, assetName, resourceGroupName, subscriptionId` | Get the details of an Asset in the Media Services account |
| `Assets_List` | `SELECT` | `accountName, api-version, resourceGroupName, subscriptionId` | List Assets in the Media Services account with optional filtering and ordering |
| `Assets_CreateOrUpdate` | `INSERT` | `accountName, api-version, assetName, resourceGroupName, subscriptionId` | Creates or updates an Asset in the Media Services account |
| `Assets_Delete` | `DELETE` | `accountName, api-version, assetName, resourceGroupName, subscriptionId` | Deletes an Asset in the Media Services account |
| `Assets_GetEncryptionKey` | `EXEC` | `accountName, api-version, assetName, resourceGroupName, subscriptionId` | Gets the Asset storage encryption keys used to decrypt content created by version 2 of the Media Services API |
| `Assets_ListContainerSas` | `EXEC` | `accountName, api-version, assetName, resourceGroupName, subscriptionId` | Lists storage container URLs with shared access signatures (SAS) for uploading and downloading Asset content. The signatures are derived from the storage account keys. |
| `Assets_ListStreamingLocators` | `EXEC` | `accountName, api-version, assetName, resourceGroupName, subscriptionId` | Lists Streaming Locators which are associated with this asset. |
| `Assets_Update` | `EXEC` | `accountName, api-version, assetName, resourceGroupName, subscriptionId` | Updates an existing Asset in the Media Services account |
