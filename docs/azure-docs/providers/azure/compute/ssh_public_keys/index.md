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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ssh_public_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.ssh_public_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Properties of the SSH public key. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sshPublicKeyName, subscriptionId" /> | Retrieves information about an SSH public key. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the SSH public keys in the specified resource group. Use the nextLink property in the response to get the next page of SSH public keys. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all of the SSH public keys in the subscription. Use the nextLink property in the response to get the next page of SSH public keys. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, sshPublicKeyName, subscriptionId" /> | Creates a new SSH public key resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, sshPublicKeyName, subscriptionId" /> | Delete an SSH public key. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the SSH public keys in the specified resource group. Use the nextLink property in the response to get the next page of SSH public keys. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Lists all of the SSH public keys in the subscription. Use the nextLink property in the response to get the next page of SSH public keys. |
| <CopyableCode code="generate_key_pair" /> | `EXEC` | <CopyableCode code="resourceGroupName, sshPublicKeyName, subscriptionId" /> | Generates and returns a public/private key pair and populates the SSH public key resource with the public key. The length of the key will be 3072 bits. This operation can only be performed once per SSH public key resource. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, sshPublicKeyName, subscriptionId" /> | Updates a new SSH public key resource. |
