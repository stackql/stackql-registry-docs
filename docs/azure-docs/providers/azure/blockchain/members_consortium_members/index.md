---
title: members_consortium_members
hide_title: false
hide_table_of_contents: false
keywords:
  - members_consortium_members
  - blockchain
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
<tr><td><b>Name</b></td><td><code>members_consortium_members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.blockchain.members_consortium_members</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Gets the consortium member name. |
| `dateModified` | `string` | Gets the consortium member modified date. |
| `displayName` | `string` | Gets the consortium member display name. |
| `joinDate` | `string` | Gets the consortium member join date. |
| `role` | `string` | Gets the consortium member role. |
| `status` | `string` | Gets the consortium member status. |
| `subscriptionId` | `string` | Gets the consortium member subscription id. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `blockchainMemberName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `blockchainMemberName, resourceGroupName, subscriptionId` |
