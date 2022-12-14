---
title: vault_extended_info
hide_title: false
hide_table_of_contents: false
keywords:
  - vault_extended_info
  - recovery_services
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
<tr><td><b>Name</b></td><td><code>vault_extended_info</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services.vault_extended_info</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id represents the complete path to the resource. |
| `name` | `string` | Resource name associated with the resource. |
| `etag` | `string` | Optional ETag. |
| `properties` | `object` | Vault extended information. |
| `type` | `string` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VaultExtendedInfo_Get` | `SELECT` | `api-version, resourceGroupName, subscriptionId, vaultName` | Get the vault extended info. |
| `VaultExtendedInfo_CreateOrUpdate` | `INSERT` | `api-version, resourceGroupName, subscriptionId, vaultName` | Create vault extended info. |
| `VaultExtendedInfo_Update` | `EXEC` | `api-version, resourceGroupName, subscriptionId, vaultName` | Update vault extended info. |
