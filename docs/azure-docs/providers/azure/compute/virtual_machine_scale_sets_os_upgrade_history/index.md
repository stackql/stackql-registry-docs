---
title: virtual_machine_scale_sets_os_upgrade_history
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_scale_sets_os_upgrade_history
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
<tr><td><b>Name</b></td><td><code>virtual_machine_scale_sets_os_upgrade_history</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.virtual_machine_scale_sets_os_upgrade_history</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | Resource location |
| `properties` | `object` | Describes each OS upgrade on the Virtual Machine Scale Set. |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, vmScaleSetName` |
| `_get` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName` |
