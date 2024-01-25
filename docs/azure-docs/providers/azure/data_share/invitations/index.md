---
title: invitations
hide_title: false
hide_table_of_contents: false
keywords:
  - invitations
  - data_share
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
<tr><td><b>Name</b></td><td><code>invitations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_share.invitations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id of the azure resource |
| `name` | `string` | Name of the azure resource |
| `properties` | `object` | Invitation property bag. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | Type of the azure resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, api-version, invitationName, resourceGroupName, shareName, subscriptionId` | Get an invitation in a share |
| `list_by_share` | `SELECT` | `accountName, api-version, resourceGroupName, shareName, subscriptionId` | List invitations in a share |
| `create` | `INSERT` | `accountName, api-version, invitationName, resourceGroupName, shareName, subscriptionId` | Create an invitation  |
| `delete` | `DELETE` | `accountName, api-version, invitationName, resourceGroupName, shareName, subscriptionId` | Delete an invitation in a share |
| `_list_by_share` | `EXEC` | `accountName, api-version, resourceGroupName, shareName, subscriptionId` | List invitations in a share |
