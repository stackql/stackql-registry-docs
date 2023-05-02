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
| `healthDescription` | `string` | Output only. If this field is populated, it contains a description of why the TPU Node is unhealthy. |
| `networkEndpoints` | `array` | Output only. The network endpoints where TPU workers can be accessed and sent work. It is recommended that runtime clients of the node reach out to the 0th entry in this map first. |
| `dataDisks` | `array` | The additional data disks for the Node. |
| `cidrBlock` | `string` | The CIDR block that the TPU node will use when selecting an IP address. This CIDR block must be a /29 block; the Compute Engine networks API forbids a smaller block, and using a larger block would be wasteful (a node can only consume one IP address). Errors will occur if the CIDR block has already been used for a currently existing TPU node, the CIDR block conflicts with any subnetworks in the user's provided network, or the provided network is peered with another network that is using that CIDR block. |
| `acceleratorType` | `string` | Required. The type of hardware accelerators associated with this node. |
| `runtimeVersion` | `string` | Required. The runtime version running in the Node. |
| `apiVersion` | `string` | Output only. The API version that created this Node. |
| `tags` | `array` | Tags to apply to the TPU Node. Tags are used to identify valid sources or targets for network firewalls. |
| `health` | `string` | The health status of the TPU node. |
| `networkConfig` | `object` | Network related configurations. |
| `schedulingConfig` | `object` | Sets the scheduling options for this node. |
| `labels` | `object` | Resource labels to represent user-provided metadata. |
| `state` | `string` | Output only. The current state for the TPU Node. |
| `createTime` | `string` | Output only. The time when the node was created. |
| `serviceAccount` | `object` | A service account. |
| `shieldedInstanceConfig` | `object` | A set of Shielded Instance options. |
| `metadata` | `object` | Custom metadata to apply to the TPU Node. Can set startup-script and shutdown-script |
| `symptoms` | `array` | Output only. The Symptoms that have occurred to the TPU Node. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_nodes_get` | `SELECT` | `locationsId, nodesId, projectsId` | Gets the details of a node. |
| `projects_locations_nodes_list` | `SELECT` | `locationsId, projectsId` | Lists nodes. |
| `projects_locations_nodes_create` | `INSERT` | `locationsId, projectsId` | Creates a node. |
| `projects_locations_nodes_delete` | `DELETE` | `locationsId, nodesId, projectsId` | Deletes a node. |
| `projects_locations_nodes_patch` | `EXEC` | `locationsId, nodesId, projectsId` | Updates the configurations of a node. |
| `projects_locations_nodes_start` | `EXEC` | `locationsId, nodesId, projectsId` | Starts a node. |
| `projects_locations_nodes_stop` | `EXEC` | `locationsId, nodesId, projectsId` | Stops a node. This operation is only available with single TPU nodes. |
