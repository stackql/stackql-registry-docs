---
title: mhsm_regions
hide_title: false
hide_table_of_contents: false
keywords:
  - mhsm_regions
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
<tr><td><b>Name</b></td><td><code>mhsm_regions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.key_vault.mhsm_regions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of the geo replicated region. |
| `isPrimary` | `boolean` | A boolean value that indicates whether the region is the primary region or a secondary region. |
| `provisioningState` | `string` | The current provisioning state. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_by_resource` | `SELECT` | `name, resourceGroupName, subscriptionId` |
| `_list_by_resource` | `EXEC` | `name, resourceGroupName, subscriptionId` |
