---
title: sync_identity_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_identity_providers
  - redhat_openshift
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>sync_identity_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.redhat_openshift.sync_identity_providers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | SyncSetProperties represents the properties of a SyncSet |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `childResourceName, resourceGroupName, resourceName, subscriptionId` | The operation returns properties of a SyncIdentityProvider. |
| `list` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | The operation returns properties of each SyncIdentityProvider. |
| `create_or_update` | `INSERT` | `childResourceName, resourceGroupName, resourceName, subscriptionId` | The operation returns properties of a SyncIdentityProvider. |
| `delete` | `DELETE` | `childResourceName, resourceGroupName, resourceName, subscriptionId` | The operation returns nothing. |
| `_list` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | The operation returns properties of each SyncIdentityProvider. |
| `update` | `EXEC` | `childResourceName, resourceGroupName, resourceName, subscriptionId` | The operation returns properties of a SyncIdentityProvider. |
