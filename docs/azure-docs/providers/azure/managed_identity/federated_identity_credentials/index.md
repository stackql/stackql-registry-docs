---
title: federated_identity_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - federated_identity_credentials
  - managed_identity
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
<tr><td><b>Name</b></td><td><code>federated_identity_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_identity.federated_identity_credentials</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `federatedIdentityCredentialResourceName, resourceGroupName, resourceName, subscriptionId` | Gets the federated identity credential. |
| `list` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Lists all the federated identity credentials under the specified user assigned identity. |
| `create_or_update` | `INSERT` | `federatedIdentityCredentialResourceName, resourceGroupName, resourceName, subscriptionId` | Create or update a federated identity credential under the specified user assigned identity. |
| `delete` | `DELETE` | `federatedIdentityCredentialResourceName, resourceGroupName, resourceName, subscriptionId` | Deletes the federated identity credential. |
| `_list` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Lists all the federated identity credentials under the specified user assigned identity. |
