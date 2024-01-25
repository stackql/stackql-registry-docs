---
title: asset_filters
hide_title: false
hide_table_of_contents: false
keywords:
  - asset_filters
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
<tr><td><b>Name</b></td><td><code>asset_filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.media_services.asset_filters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | The Media Filter properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, api-version, assetName, filterName, resourceGroupName, subscriptionId` | Get the details of an Asset Filter associated with the specified Asset. |
| `list` | `SELECT` | `accountName, api-version, assetName, resourceGroupName, subscriptionId` | List Asset Filters associated with the specified Asset. |
| `create_or_update` | `INSERT` | `accountName, api-version, assetName, filterName, resourceGroupName, subscriptionId` | Creates or updates an Asset Filter associated with the specified Asset. |
| `delete` | `DELETE` | `accountName, api-version, assetName, filterName, resourceGroupName, subscriptionId` | Deletes an Asset Filter associated with the specified Asset. |
| `_list` | `EXEC` | `accountName, api-version, assetName, resourceGroupName, subscriptionId` | List Asset Filters associated with the specified Asset. |
| `update` | `EXEC` | `accountName, api-version, assetName, filterName, resourceGroupName, subscriptionId` | Updates an existing Asset Filter associated with the specified Asset. |
