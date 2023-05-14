---
title: kernels
hide_title: false
hide_table_of_contents: false
keywords:
  - kernels
  - instances
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>kernels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.instances.kernels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique ID of this Kernel. |
| `version` | `string` | Linux Kernel version. |
| `xen` | `boolean` | If this Kernel is suitable for Xen Linodes. |
| `kvm` | `boolean` | If this Kernel is suitable for KVM Linodes. |
| `label` | `string` | The friendly name of this Kernel. |
| `deprecated` | `boolean` | If this Kernel is marked as deprecated, this field has a value of true; otherwise, this field is false. |
| `built` | `string` | The date on which this Kernel was built. |
| `pvops` | `boolean` | If this Kernel is suitable for paravirtualized operations. |
| `architecture` | `string` | The architecture of this Kernel. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getKernel` | `SELECT` | `kernelId` | Returns information about a single Kernel.<br /> |
| `getKernels` | `SELECT` |  | Lists available Kernels.<br /> |
| `_getKernel` | `EXEC` | `kernelId` | Returns information about a single Kernel.<br /> |
| `_getKernels` | `EXEC` |  | Lists available Kernels.<br /> |
