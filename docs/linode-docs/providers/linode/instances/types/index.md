---
title: types
hide_title: false
hide_table_of_contents: false
keywords:
  - types
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
<tr><td><b>Name</b></td><td><code>types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.instances.types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID representing the Linode Type. |
| <CopyableCode code="addons" /> | `object` | A list of optional add-on services for Linodes and their associated costs.<br /> |
| <CopyableCode code="class" /> | `string` | The class of the Linode Type. We currently offer five classes of Linodes:<br /><br />  * nanode - Nanode instances are good for low-duty workloads,<br />    where performance isn't critical. **Note:** As of June 16th, 2020, Nanodes became<br />    1 GB Linodes in the Cloud Manager, however, the API, the CLI, and billing will<br />    continue to refer to these instances as Nanodes.<br />  * standard - Standard Shared instances are good for medium-duty workloads and<br />    are a good mix of performance, resources, and price. **Note:** As of June 16th, 2020,<br />    Standard Linodes in the Cloud Manager became Shared Linodes, however, the API, the CLI, and<br />    billing will continue to refer to these instances as Standard Linodes.<br />  * dedicated - Dedicated CPU instances are good for full-duty workloads<br />    where consistent performance is important.<br />  * gpu - Linodes with dedicated NVIDIA Quadro &reg; RTX 6000 GPUs accelerate highly<br />    specialized applications such as machine learning, AI, and video transcoding.<br />  * highmem - High Memory instances favor RAM over other resources, and can be<br />    good for memory hungry use cases like caching and in-memory databases.<br />    All High Memory plans contain dedicated CPU cores.<br /> |
| <CopyableCode code="disk" /> | `integer` | The Disk size, in MB, of the Linode Type.<br /> |
| <CopyableCode code="gpus" /> | `integer` | The number of GPUs this Linode Type offers.<br /> |
| <CopyableCode code="label" /> | `string` | The Linode Type's label is for display purposes only.<br /> |
| <CopyableCode code="memory" /> | `integer` | Amount of RAM included in this Linode Type.<br /> |
| <CopyableCode code="network_out" /> | `integer` | The Mbits outbound bandwidth allocation.<br /> |
| <CopyableCode code="price" /> | `object` | Cost in US dollars, broken down into hourly and monthly charges.<br /> |
| <CopyableCode code="successor" /> | `string` | The Linode Type that a [mutate](/docs/api/linode-instances/#linode-upgrade) will upgrade to for a Linode of this type.  If "null", a Linode of this type may not mutate.<br /> |
| <CopyableCode code="transfer" /> | `integer` | The monthly outbound transfer amount, in MB.<br /> |
| <CopyableCode code="vcpus" /> | `integer` | The number of VCPU cores this Linode Type offers.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getLinodeType" /> | `SELECT` | <CopyableCode code="typeId" /> | Returns information about a specific Linode Type, including pricing and specifications. This is used when [creating](/docs/api/linode-instances/#linode-create) or [resizing](/docs/api/linode-instances/#linode-resize) Linodes.<br /> |
| <CopyableCode code="getLinodeTypes" /> | `SELECT` |  | Returns collection of Linode Types, including pricing and specifications for each Type. These are used when [creating](/docs/api/linode-instances/#linode-create) or [resizing](/docs/api/linode-instances/#linode-resize) Linodes.<br /> |
| <CopyableCode code="_getLinodeType" /> | `EXEC` | <CopyableCode code="typeId" /> | Returns information about a specific Linode Type, including pricing and specifications. This is used when [creating](/docs/api/linode-instances/#linode-create) or [resizing](/docs/api/linode-instances/#linode-resize) Linodes.<br /> |
| <CopyableCode code="_getLinodeTypes" /> | `EXEC` |  | Returns collection of Linode Types, including pricing and specifications for each Type. These are used when [creating](/docs/api/linode-instances/#linode-create) or [resizing](/docs/api/linode-instances/#linode-resize) Linodes.<br /> |
