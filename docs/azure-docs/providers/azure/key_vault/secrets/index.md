---
title: secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - secrets
  - key_vault
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
<tr><td><b>Name</b></td><td><code>secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.key_vault.secrets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified identifier of the key vault resource. |
| `name` | `string` | Name of the key vault resource. |
| `properties` | `object` | Properties of the secret |
| `tags` | `object` | Tags assigned to the key vault resource. |
| `type` | `string` | Resource type of the key vault resource. |
| `location` | `string` | Azure location of the key vault resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Secrets_Get` | `SELECT` | `resourceGroupName, secretName, subscriptionId, vaultName` | Gets the specified secret.  NOTE: This API is intended for internal use in ARM deployments. Users should use the data-plane REST service for interaction with vault secrets. |
| `Secrets_List` | `SELECT` | `resourceGroupName, subscriptionId, vaultName` | The List operation gets information about the secrets in a vault.  NOTE: This API is intended for internal use in ARM deployments. Users should use the data-plane REST service for interaction with vault secrets. |
| `Secrets_CreateOrUpdate` | `INSERT` | `resourceGroupName, secretName, subscriptionId, vaultName, data__properties` | Create or update a secret in a key vault in the specified subscription.  NOTE: This API is intended for internal use in ARM deployments. Users should use the data-plane REST service for interaction with vault secrets. |
| `Secrets_Update` | `EXEC` | `resourceGroupName, secretName, subscriptionId, vaultName` | Update a secret in the specified subscription.  NOTE: This API is intended for internal use in ARM deployments.  Users should use the data-plane REST service for interaction with vault secrets. |
