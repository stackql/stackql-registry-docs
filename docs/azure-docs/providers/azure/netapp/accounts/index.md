---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - netapp
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
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.netapp.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Identity for the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | NetApp account properties |
| `tags` | `object` | Resource tags. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Accounts_Get` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Get the NetApp account |
| `Accounts_List` | `SELECT` | `resourceGroupName, subscriptionId` | List and describe all NetApp accounts in the resource group. |
| `Accounts_ListBySubscription` | `SELECT` | `subscriptionId` | List and describe all NetApp accounts in the subscription. |
| `Accounts_CreateOrUpdate` | `INSERT` | `accountName, resourceGroupName, subscriptionId, data__location` | Create or update the specified NetApp account within the resource group |
| `Accounts_Delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Delete the specified NetApp account |
| `Accounts_RenewCredentials` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Renew identity credentials that are used to authenticate to key vault, for customer-managed key encryption. If encryption.identity.principalId does not match identity.principalId, running this operation will fix it. |
| `Accounts_Update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Patch the specified NetApp account |
