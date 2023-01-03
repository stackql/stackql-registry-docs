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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `name` | `string` | Output only. Immutable. The name of the TPU |
| `description` | `string` | The user-supplied description of the TPU. Maximum of 512 characters. |
| `useServiceNetworking` | `boolean` | Whether the VPC peering for the node is set up through Service Networking API. The VPC Peering should be set up before provisioning the node. If this field is set, cidr_block field should not be specified. If the network, that you want to peer the TPU Node to, is Shared VPC networks, the node must be created with this this field enabled. |
| `networkEndpoints` | `array` | Output only. The network endpoints where TPU workers can be accessed and sent work. It is recommended that Tensorflow clients of the node reach out to the 0th entry in this map first. |
| `port` | `string` | Output only. DEPRECATED! Use network_endpoints instead. The network port for the TPU Node as visible to Compute Engine instances. |
| `network` | `string` | The name of a network they wish to peer the TPU node to. It must be a preexisting Compute Engine network inside of the project on which this API has been activated. If none is provided, "default" will be used. |
| `createTime` | `string` | Output only. The time when the node was created. |
| `schedulingConfig` | `object` | Sets the scheduling options for this node. |
| `apiVersion` | `string` | Output only. The API version that created this Node. |
| `tensorflowVersion` | `string` | Required. The version of Tensorflow running in the Node. |
| `symptoms` | `array` | Output only. The Symptoms that have occurred to the TPU Node. |
| `serviceAccount` | `string` | Output only. The service account used to run the tensor flow services within the node. To share resources, including Google Cloud Storage data, with the Tensorflow job running in the Node, this account must have permissions to that data. |
| `acceleratorType` | `string` | Required. The type of hardware accelerators associated with this node. |
| `labels` | `object` | Resource labels to represent user-provided metadata. |
| `health` | `string` | The health status of the TPU node. |
| `ipAddress` | `string` | Output only. DEPRECATED! Use network_endpoints instead. The network address for the TPU Node as visible to Compute Engine instances. |
| `cidrBlock` | `string` | The CIDR block that the TPU node will use when selecting an IP address. This CIDR block must be a /29 block; the Compute Engine networks API forbids a smaller block, and using a larger block would be wasteful (a node can only consume one IP address). Errors will occur if the CIDR block has already been used for a currently existing TPU node, the CIDR block conflicts with any subnetworks in the user's provided network, or the provided network is peered with another network that is using that CIDR block. |
| `state` | `string` | Output only. The current state for the TPU Node. |
| `healthDescription` | `string` | Output only. If this field is populated, it contains a description of why the TPU Node is unhealthy. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_nodes_get` | `SELECT` | `locationsId, nodesId, projectsId` | Gets the details of a node. |
| `projects_locations_nodes_list` | `SELECT` | `locationsId, projectsId` | Lists nodes. |
| `projects_locations_nodes_create` | `INSERT` | `locationsId, projectsId` | Creates a node. |
| `projects_locations_nodes_delete` | `DELETE` | `locationsId, nodesId, projectsId` | Deletes a node. |
| `projects_locations_nodes_reimage` | `EXEC` | `locationsId, nodesId, projectsId` | Reimages a node's OS. |
| `projects_locations_nodes_start` | `EXEC` | `locationsId, nodesId, projectsId` | Starts a node. |
| `projects_locations_nodes_stop` | `EXEC` | `locationsId, nodesId, projectsId` | Stops a node, this operation is only available with single TPU nodes. |
