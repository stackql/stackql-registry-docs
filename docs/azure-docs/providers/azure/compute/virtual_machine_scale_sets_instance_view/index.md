---
title: virtual_machine_scale_sets_instance_view
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_scale_sets_instance_view
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
<tr><td><b>Name</b></td><td><code>virtual_machine_scale_sets_instance_view</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.virtual_machine_scale_sets_instance_view</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extensions` | `array` | The extensions information. |
| `orchestrationServices` | `array` | The orchestration services information. |
| `statuses` | `array` | The resource status information. |
| `virtualMachine` | `object` | Instance view statuses summary for virtual machines of a virtual machine scale set. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, vmScaleSetName` |
