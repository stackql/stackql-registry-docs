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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>kernels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.instances.kernels" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique ID of this Kernel. |
| <CopyableCode code="architecture" /> | `string` | The architecture of this Kernel. |
| <CopyableCode code="built" /> | `string` | The date on which this Kernel was built. |
| <CopyableCode code="deprecated" /> | `boolean` | If this Kernel is marked as deprecated, this field has a value of true; otherwise, this field is false. |
| <CopyableCode code="kvm" /> | `boolean` | If this Kernel is suitable for KVM Linodes. |
| <CopyableCode code="label" /> | `string` | The friendly name of this Kernel. |
| <CopyableCode code="pvops" /> | `boolean` | If this Kernel is suitable for paravirtualized operations. |
| <CopyableCode code="version" /> | `string` | Linux Kernel version. |
| <CopyableCode code="xen" /> | `boolean` | If this Kernel is suitable for Xen Linodes. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getKernel" /> | `SELECT` | <CopyableCode code="kernelId" /> | Returns information about a single Kernel.<br /> |
| <CopyableCode code="getKernels" /> | `SELECT` |  | Lists available Kernels.<br /> |
| <CopyableCode code="_getKernel" /> | `EXEC` | <CopyableCode code="kernelId" /> | Returns information about a single Kernel.<br /> |
| <CopyableCode code="_getKernels" /> | `EXEC` |  | Lists available Kernels.<br /> |
