---
title: file_shares
hide_title: false
hide_table_of_contents: false
keywords:
  - file_shares
  - storage
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
<tr><td><b>Name</b></td><td><code>file_shares</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage.file_shares</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Resource Etag. |
| `properties` | `object` | The properties of the file share. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `FileShares_Get` | `SELECT` | `accountName, resourceGroupName, shareName, subscriptionId` | Gets properties of a specified share. |
| `FileShares_List` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Lists all shares. |
| `FileShares_Create` | `INSERT` | `accountName, resourceGroupName, shareName, subscriptionId` | Creates a new share under the specified account as described by request body. The share resource includes metadata and properties for that share. It does not include a list of the files contained by the share.  |
| `FileShares_Delete` | `DELETE` | `accountName, resourceGroupName, shareName, subscriptionId` | Deletes specified share under its account. |
| `FileShares_Lease` | `EXEC` | `accountName, resourceGroupName, shareName, subscriptionId, data__action` | The Lease Share operation establishes and manages a lock on a share for delete operations. The lock duration can be 15 to 60 seconds, or can be infinite. |
| `FileShares_Restore` | `EXEC` | `accountName, resourceGroupName, shareName, subscriptionId, data__deletedShareName, data__deletedShareVersion` | Restore a file share within a valid retention days if share soft delete is enabled |
| `FileShares_Update` | `EXEC` | `accountName, resourceGroupName, shareName, subscriptionId` | Updates share properties as specified in request body. Properties not mentioned in the request will not be changed. Update fails if the specified share does not already exist.  |
