---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - engagement_fabric
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
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.engagement_fabric.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The location of the resource |
| `sku` | `object` | The EngagementFabric SKU |
| `tags` | `object` | The tags of the resource |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Accounts_Get` | `SELECT` | `accountName, resourceGroupName, subscriptionId` |
| `Accounts_List` | `SELECT` | `subscriptionId` |
| `Accounts_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` |
| `Accounts_CreateOrUpdate` | `INSERT` | `accountName, resourceGroupName, subscriptionId, data__location, data__sku` |
| `Accounts_Delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` |
| `Accounts_ListChannelTypes` | `EXEC` | `accountName, resourceGroupName, subscriptionId` |
| `Accounts_ListKeys` | `EXEC` | `accountName, resourceGroupName, subscriptionId` |
| `Accounts_RegenerateKey` | `EXEC` | `accountName, resourceGroupName, subscriptionId, data__name, data__rank` |
| `Accounts_Update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` |
