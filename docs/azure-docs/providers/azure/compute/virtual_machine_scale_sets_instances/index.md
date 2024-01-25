---
title: virtual_machine_scale_sets_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_scale_sets_instances
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
<tr><td><b>Name</b></td><td><code>virtual_machine_scale_sets_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.virtual_machine_scale_sets_instances</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, vmScaleSetName, data__instanceIds` | Deletes virtual machines in a VM scale set. |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName, data__instanceIds` | Upgrades one or more virtual machines to the latest SKU set in the VM scale set model. |
