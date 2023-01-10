---
title: account_filters
hide_title: false
hide_table_of_contents: false
keywords:
  - account_filters
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
<tr><td><b>Name</b></td><td><code>account_filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.media_services.account_filters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | The Media Filter properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AccountFilters_Get` | `SELECT` | `accountName, api-version, filterName, resourceGroupName, subscriptionId` | Get the details of an Account Filter in the Media Services account. |
| `AccountFilters_List` | `SELECT` | `accountName, api-version, resourceGroupName, subscriptionId` | List Account Filters in the Media Services account. |
| `AccountFilters_CreateOrUpdate` | `INSERT` | `accountName, api-version, filterName, resourceGroupName, subscriptionId` | Creates or updates an Account Filter in the Media Services account. |
| `AccountFilters_Delete` | `DELETE` | `accountName, api-version, filterName, resourceGroupName, subscriptionId` | Deletes an Account Filter in the Media Services account. |
| `AccountFilters_Update` | `EXEC` | `accountName, api-version, filterName, resourceGroupName, subscriptionId` | Updates an existing Account Filter in the Media Services account. |
