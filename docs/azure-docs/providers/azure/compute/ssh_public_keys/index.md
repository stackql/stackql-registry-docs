---
title: ssh_public_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - ssh_public_keys
  - compute
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
<tr><td><b>Name</b></td><td><code>ssh_public_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.ssh_public_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `location` | `string` | Resource location |
| `properties` | `object` | Properties of the SSH public key. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SshPublicKeys_Get` | `SELECT` | `resourceGroupName, sshPublicKeyName, subscriptionId` | Retrieves information about an SSH public key. |
| `SshPublicKeys_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all of the SSH public keys in the specified resource group. Use the nextLink property in the response to get the next page of SSH public keys. |
| `SshPublicKeys_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all of the SSH public keys in the subscription. Use the nextLink property in the response to get the next page of SSH public keys. |
| `SshPublicKeys_Create` | `INSERT` | `resourceGroupName, sshPublicKeyName, subscriptionId` | Creates a new SSH public key resource. |
| `SshPublicKeys_Delete` | `DELETE` | `resourceGroupName, sshPublicKeyName, subscriptionId` | Delete an SSH public key. |
| `SshPublicKeys_GenerateKeyPair` | `EXEC` | `resourceGroupName, sshPublicKeyName, subscriptionId` | Generates and returns a public/private key pair and populates the SSH public key resource with the public key. The length of the key will be 3072 bits. This operation can only be performed once per SSH public key resource. |
| `SshPublicKeys_Update` | `EXEC` | `resourceGroupName, sshPublicKeyName, subscriptionId` | Updates a new SSH public key resource. |
