---
title: virtual_machine_sizes
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_sizes
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
<tr><td><b>Name</b></td><td><code>virtual_machine_sizes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.virtual_machine_sizes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the virtual machine size. |
| `memoryInMB` | `integer` | The amount of memory, in MB, supported by the virtual machine size. |
| `numberOfCores` | `integer` | The number of cores supported by the virtual machine size. For Constrained vCPU capable VM sizes, this number represents the total vCPUs of quota that the VM uses. For accurate vCPU count, please refer to https://docs.microsoft.com/azure/virtual-machines/constrained-vcpu or https://docs.microsoft.com/rest/api/compute/resourceskus/list |
| `osDiskSizeInMB` | `integer` | The OS disk size, in MB, allowed by the virtual machine size. |
| `resourceDiskSizeInMB` | `integer` | The resource disk size, in MB, allowed by the virtual machine size. |
| `maxDataDiskCount` | `integer` | The maximum number of data disks that can be attached to the virtual machine size. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `VirtualMachineSizes_List` | `SELECT` | `location, subscriptionId` |
