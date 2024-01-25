---
title: assets
hide_title: false
hide_table_of_contents: false
keywords:
  - assets
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
<tr><td><b>Name</b></td><td><code>assets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.media_services.assets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | The Asset properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, api-version, assetName, resourceGroupName, subscriptionId` | Get the details of an Asset in the Media Services account |
| `list` | `SELECT` | `accountName, api-version, resourceGroupName, subscriptionId` | List Assets in the Media Services account with optional filtering and ordering |
| `create_or_update` | `INSERT` | `accountName, api-version, assetName, resourceGroupName, subscriptionId` | Creates or updates an Asset in the Media Services account |
| `delete` | `DELETE` | `accountName, api-version, assetName, resourceGroupName, subscriptionId` | Deletes an Asset in the Media Services account |
| `_list` | `EXEC` | `accountName, api-version, resourceGroupName, subscriptionId` | List Assets in the Media Services account with optional filtering and ordering |
| `update` | `EXEC` | `accountName, api-version, assetName, resourceGroupName, subscriptionId` | Updates an existing Asset in the Media Services account |
