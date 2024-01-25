---
title: vaults_deleted
hide_title: false
hide_table_of_contents: false
keywords:
  - vaults_deleted
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
<tr><td><b>Name</b></td><td><code>vaults_deleted</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.key_vault.vaults_deleted</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID for the deleted key vault. |
| `name` | `string` | The name of the key vault. |
| `properties` | `object` | Properties of the deleted vault. |
| `type` | `string` | The resource type of the key vault. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `location, subscriptionId, vaultName` | Gets the deleted Azure key vault. |
| `list` | `SELECT` | `subscriptionId` | Gets information about the deleted vaults in a subscription. |
| `_list` | `EXEC` | `subscriptionId` | Gets information about the deleted vaults in a subscription. |
