---
title: mhsm_private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - mhsm_private_link_resources
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
<tr><td><b>Name</b></td><td><code>mhsm_private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.key_vault.mhsm_private_link_resources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The Azure Resource Manager resource ID for the managed HSM Pool. |
| `name` | `string` | The name of the managed HSM Pool. |
| `type` | `string` | The resource type of the managed HSM Pool. |
| `location` | `string` | The supported Azure location where the managed HSM Pool should be created. |
| `properties` | `object` | Properties of a private link resource. |
| `sku` | `object` | SKU details |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the key vault resource. |
| `tags` | `object` | Resource tags |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `MHSMPrivateLinkResources_ListByMHSMResource` | `SELECT` | `name, resourceGroupName, subscriptionId` |
