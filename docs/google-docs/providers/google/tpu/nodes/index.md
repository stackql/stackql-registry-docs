---
title: nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - nodes
  - tpu
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.tpu.nodes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Output only. The unique identifier for the TPU Node. |
| <CopyableCode code="name" /> | `string` | Output only. Immutable. The name of the TPU. |
| <CopyableCode code="description" /> | `string` | The user-supplied description of the TPU. Maximum of 512 characters. |
| <CopyableCode code="acceleratorConfig" /> | `object` | A TPU accelerator configuration. |
| <CopyableCode code="acceleratorType" /> | `string` | Optional. The type of hardware accelerators associated with this node. |
| <CopyableCode code="apiVersion" /> | `string` | Output only. The API version that created this Node. |
| <CopyableCode code="cidrBlock" /> | `string` | The CIDR block that the TPU node will use when selecting an IP address. This CIDR block must be a /29 block; the Compute Engine networks API forbids a smaller block, and using a larger block would be wasteful (a node can only consume one IP address). Errors will occur if the CIDR block has already been used for a currently existing TPU node, the CIDR block conflicts with any subnetworks in the user's provided network, or the provided network is peered with another network that is using that CIDR block. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the node was created. |
| <CopyableCode code="dataDisks" /> | `array` | The additional data disks for the Node. |
| <CopyableCode code="health" /> | `string` | The health status of the TPU node. |
| <CopyableCode code="healthDescription" /> | `string` | Output only. If this field is populated, it contains a description of why the TPU Node is unhealthy. |
| <CopyableCode code="labels" /> | `object` | Resource labels to represent user-provided metadata. |
| <CopyableCode code="metadata" /> | `object` | Custom metadata to apply to the TPU Node. Can set startup-script and shutdown-script |
| <CopyableCode code="multisliceNode" /> | `boolean` | Output only. Whether the Node belongs to a Multislice group. |
| <CopyableCode code="networkConfig" /> | `object` | Network related configurations. |
| <CopyableCode code="networkEndpoints" /> | `array` | Output only. The network endpoints where TPU workers can be accessed and sent work. It is recommended that runtime clients of the node reach out to the 0th entry in this map first. |
| <CopyableCode code="queuedResource" /> | `string` | Output only. The qualified name of the QueuedResource that requested this Node. |
| <CopyableCode code="runtimeVersion" /> | `string` | Required. The runtime version running in the Node. |
| <CopyableCode code="schedulingConfig" /> | `object` | Sets the scheduling options for this node. |
| <CopyableCode code="serviceAccount" /> | `object` | A service account. |
| <CopyableCode code="shieldedInstanceConfig" /> | `object` | A set of Shielded Instance options. |
| <CopyableCode code="state" /> | `string` | Output only. The current state for the TPU Node. |
| <CopyableCode code="symptoms" /> | `array` | Output only. The Symptoms that have occurred to the TPU Node. |
| <CopyableCode code="tags" /> | `array` | Tags to apply to the TPU Node. Tags are used to identify valid sources or targets for network firewalls. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, nodesId, projectsId" /> | Gets the details of a node. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists nodes. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a node. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, nodesId, projectsId" /> | Deletes a node. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, nodesId, projectsId" /> | Updates the configurations of a node. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists nodes. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="locationsId, nodesId, projectsId" /> | Starts a node. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="locationsId, nodesId, projectsId" /> | Stops a node. This operation is only available with single TPU nodes. |
