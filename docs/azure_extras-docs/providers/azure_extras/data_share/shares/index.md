---
title: shares
hide_title: false
hide_table_of_contents: false
keywords:
  - shares
  - data_share
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
<tr><td><b>Name</b></td><td><code>shares</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.data_share.shares</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id of the azure resource |
| `name` | `string` | Name of the azure resource |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | Type of the azure resource |
| `properties` | `object` | Share property bag. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Shares_Get` | `SELECT` | `accountName, api-version, resourceGroupName, shareName, subscriptionId` | Get a share  |
| `Shares_ListByAccount` | `SELECT` | `accountName, api-version, resourceGroupName, subscriptionId` | List shares in an account |
| `Shares_Create` | `INSERT` | `accountName, api-version, resourceGroupName, shareName, subscriptionId` | Create a share  |
| `Shares_Delete` | `DELETE` | `accountName, api-version, resourceGroupName, shareName, subscriptionId` | Delete a share  |
| `Shares_ListSynchronizationDetails` | `EXEC` | `accountName, api-version, resourceGroupName, shareName, subscriptionId` | List synchronization details |
| `Shares_ListSynchronizations` | `EXEC` | `accountName, api-version, resourceGroupName, shareName, subscriptionId` | List synchronizations of a share |
