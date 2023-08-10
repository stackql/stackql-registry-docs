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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.tpu.nodes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Output only. The unique identifier for the TPU Node. |
| `name` | `string` | Output only. Immutable. The name of the TPU. |
| `description` | `string` | The user-supplied description of the TPU. Maximum of 512 characters. |
| `networkConfig` | `object` | Network related configurations. |
| `dataDisks` | `array` | The additional data disks for the Node. |
| `labels` | `object` | Resource labels to represent user-provided metadata. |
| `state` | `string` | Output only. The current state for the TPU Node. |
| `metadata` | `object` | Custom metadata to apply to the TPU Node. Can set startup-script and shutdown-script |
| `createTime` | `string` | Output only. The time when the node was created. |
| `cidrBlock` | `string` | The CIDR block that the TPU node will use when selecting an IP address. This CIDR block must be a /29 block; the Compute Engine networks API forbids a smaller block, and using a larger block would be wasteful (a node can only consume one IP address). Errors will occur if the CIDR block has already been used for a currently existing TPU node, the CIDR block conflicts with any subnetworks in the user's provided network, or the provided network is peered with another network that is using that CIDR block. |
| `apiVersion` | `string` | Output only. The API version that created this Node. |
| `healthDescription` | `string` | Output only. If this field is populated, it contains a description of why the TPU Node is unhealthy. |
| `tags` | `array` | Tags to apply to the TPU Node. Tags are used to identify valid sources or targets for network firewalls. |
| `queuedResource` | `string` | Output only. The qualified name of the QueuedResource that requested this Node. |
| `acceleratorType` | `string` | Optional. The type of hardware accelerators associated with this node. |
| `networkEndpoints` | `array` | Output only. The network endpoints where TPU workers can be accessed and sent work. It is recommended that runtime clients of the node reach out to the 0th entry in this map first. |
| `serviceAccount` | `object` | A service account. |
| `symptoms` | `array` | Output only. The Symptoms that have occurred to the TPU Node. |
| `schedulingConfig` | `object` | Sets the scheduling options for this node. |
| `acceleratorConfig` | `object` | A TPU accelerator configuration. |
| `multisliceNode` | `boolean` | Output only. Whether the Node belongs to a Multislice group. |
| `runtimeVersion` | `string` | Required. The runtime version running in the Node. |
| `health` | `string` | The health status of the TPU node. |
| `shieldedInstanceConfig` | `object` | A set of Shielded Instance options. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, nodesId, projectsId` | Gets the details of a node. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists nodes. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a node. |
| `delete` | `DELETE` | `locationsId, nodesId, projectsId` | Deletes a node. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists nodes. |
| `patch` | `EXEC` | `locationsId, nodesId, projectsId` | Updates the configurations of a node. |
| `start` | `EXEC` | `locationsId, nodesId, projectsId` | Starts a node. |
| `stop` | `EXEC` | `locationsId, nodesId, projectsId` | Stops a node. This operation is only available with single TPU nodes. |
