---
title: managed_hsms_deleted
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_hsms_deleted
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
<tr><td><b>Name</b></td><td><code>managed_hsms_deleted</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.key_vault.managed_hsms_deleted</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The Azure Resource Manager resource ID for the deleted managed HSM Pool. |
| `name` | `string` | The name of the managed HSM Pool. |
| `properties` | `object` | Properties of the deleted managed HSM. |
| `type` | `string` | The resource type of the managed HSM Pool. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `location, name, subscriptionId` | Gets the specified deleted managed HSM. |
| `list` | `SELECT` | `subscriptionId` | The List operation gets information about the deleted managed HSMs associated with the subscription. |
| `_list` | `EXEC` | `subscriptionId` | The List operation gets information about the deleted managed HSMs associated with the subscription. |
