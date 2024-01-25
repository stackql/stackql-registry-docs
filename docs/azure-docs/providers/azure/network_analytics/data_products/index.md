---
title: data_products
hide_title: false
hide_table_of_contents: false
keywords:
  - data_products
  - network_analytics
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
<tr><td><b>Name</b></td><td><code>data_products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network_analytics.data_products</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The data product properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `dataProductName, resourceGroupName, subscriptionId` | Retrieve data product resource. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List data products by resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List data products by subscription. |
| `create` | `INSERT` | `dataProductName, resourceGroupName, subscriptionId` | Create data product resource. |
| `delete` | `DELETE` | `dataProductName, resourceGroupName, subscriptionId` | Delete data product resource. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List data products by resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List data products by subscription. |
| `add_user_role` | `EXEC` | `dataProductName, resourceGroupName, subscriptionId, data__dataTypeScope, data__principalId, data__principalType, data__role, data__roleId, data__userName` | Assign role to the data product. |
| `generate_storage_account_sas_token` | `EXEC` | `dataProductName, resourceGroupName, subscriptionId, data__expiryTimeStamp, data__ipAddress, data__startTimeStamp` | Generate sas token for storage account. |
| `remove_user_role` | `EXEC` | `dataProductName, resourceGroupName, subscriptionId, data__dataTypeScope, data__principalId, data__principalType, data__role, data__roleAssignmentId, data__roleId, data__userName` | Remove role from the data product. |
| `rotate_key` | `EXEC` | `dataProductName, resourceGroupName, subscriptionId, data__keyVaultUrl` | Initiate key rotation on Data Product. |
| `update` | `EXEC` | `dataProductName, resourceGroupName, subscriptionId` | Update data product resource. |
