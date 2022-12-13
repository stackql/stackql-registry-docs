---
title: virtual_machine_sizes
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_sizes
  - machine_learning_services
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
<tr><td><b>Name</b></td><td><code>virtual_machine_sizes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.machine_learning_services.virtual_machine_sizes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the virtual machine size. |
| `estimatedVMPrices` | `object` | The estimated price info for using a VM. |
| `supportedComputeTypes` | `array` | Specifies the compute types supported by the virtual machine size. |
| `family` | `string` | The family name of the virtual machine size. |
| `gpus` | `integer` | The number of gPUs supported by the virtual machine size. |
| `memoryGB` | `number` | The amount of memory, in GB, supported by the virtual machine size. |
| `vCPUs` | `integer` | The number of vCPUs supported by the virtual machine size. |
| `premiumIO` | `boolean` | Specifies if the virtual machine size supports premium IO. |
| `osVhdSizeMB` | `integer` | The OS VHD disk size, in MB, allowed by the virtual machine size. |
| `lowPriorityCapable` | `boolean` | Specifies if the virtual machine size supports low priority VMs. |
| `maxResourceVolumeMB` | `integer` | The resource volume size, in MB, allowed by the virtual machine size. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `VirtualMachineSizes_List` | `SELECT` | `location, subscriptionId` |
