---
title: vmware_node_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - vmware_node_pools
  - gkeonprem
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
<tr><td><b>Name</b></td><td><code>vmware_node_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.gkeonprem.vmware_node_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of this node pool. |
| <CopyableCode code="annotations" /> | `object` | Annotations on the node pool. This field has the same restrictions as Kubernetes annotations. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between. |
| <CopyableCode code="config" /> | `object` | Parameters that describe the configuration of all nodes within a given node pool. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which this node pool was created. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. The time at which this node pool was deleted. If the resource is not deleted, this must be empty |
| <CopyableCode code="displayName" /> | `string` | The display name for the node pool. |
| <CopyableCode code="etag" /> | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Allows clients to perform consistent read-modify-writes through optimistic concurrency control. |
| <CopyableCode code="nodePoolAutoscaling" /> | `object` | NodePoolAutoscaling config for the NodePool to allow for the kubernetes to scale NodePool. |
| <CopyableCode code="onPremVersion" /> | `string` | Anthos version for the node pool. Defaults to the user cluster version. |
| <CopyableCode code="reconciling" /> | `boolean` | Output only. If set, there are currently changes in flight to the node pool. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the node pool. |
| <CopyableCode code="status" /> | `object` | ResourceStatus describes why a cluster or node pool has a certain status. (e.g., ERROR or DEGRADED). |
| <CopyableCode code="uid" /> | `string` | Output only. The unique identifier of the node pool. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time at which this node pool was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_vmware_clusters_vmware_node_pools_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, vmwareClustersId, vmwareNodePoolsId" /> | Gets details of a single VMware node pool. |
| <CopyableCode code="projects_locations_vmware_clusters_vmware_node_pools_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, vmwareClustersId" /> | Lists VMware node pools in a given project, location and VMWare cluster. |
| <CopyableCode code="projects_locations_vmware_clusters_vmware_node_pools_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, vmwareClustersId" /> | Creates a new VMware node pool in a given project, location and VMWare cluster. |
| <CopyableCode code="projects_locations_vmware_clusters_vmware_node_pools_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, vmwareClustersId, vmwareNodePoolsId" /> | Deletes a single VMware node pool. |
| <CopyableCode code="_projects_locations_vmware_clusters_vmware_node_pools_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, vmwareClustersId" /> | Lists VMware node pools in a given project, location and VMWare cluster. |
| <CopyableCode code="projects_locations_vmware_clusters_vmware_node_pools_enroll" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, vmwareClustersId" /> | Enrolls a VMware node pool to Anthos On-Prem API |
| <CopyableCode code="projects_locations_vmware_clusters_vmware_node_pools_patch" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, vmwareClustersId, vmwareNodePoolsId" /> | Updates the parameters of a single VMware node pool. |
| <CopyableCode code="projects_locations_vmware_clusters_vmware_node_pools_unenroll" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, vmwareClustersId, vmwareNodePoolsId" /> | Unenrolls a VMware node pool to Anthos On-Prem API |
