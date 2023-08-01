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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vmware_node_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkeonprem.vmware_node_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `unreachable` | `array` | Locations that could not be reached. |
| `vmwareNodePools` | `array` | The node pools from the specified parent resource. |
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_vmware_clusters_vmware_node_pools_list` | `SELECT` | `locationsId, projectsId, vmwareClustersId` | Lists VMware node pools in a given project, location and VMWare cluster. |
| `projects_locations_vmware_clusters_vmware_node_pools_create` | `INSERT` | `locationsId, projectsId, vmwareClustersId` | Creates a new VMware node pool in a given project, location and VMWare cluster. |
| `projects_locations_vmware_clusters_vmware_node_pools_delete` | `DELETE` | `locationsId, projectsId, vmwareClustersId, vmwareNodePoolsId` | Deletes a single VMware node pool. |
| `projects_locations_vmware_clusters_vmware_node_pools_enroll` | `EXEC` | `locationsId, projectsId, vmwareClustersId` | Enrolls a VMware node pool to Anthos On-Prem API |
| `projects_locations_vmware_clusters_vmware_node_pools_get` | `EXEC` | `locationsId, projectsId, vmwareClustersId, vmwareNodePoolsId` | Gets details of a single VMware node pool. |
| `projects_locations_vmware_clusters_vmware_node_pools_patch` | `EXEC` | `locationsId, projectsId, vmwareClustersId, vmwareNodePoolsId` | Updates the parameters of a single VMware node pool. |
| `projects_locations_vmware_clusters_vmware_node_pools_unenroll` | `EXEC` | `locationsId, projectsId, vmwareClustersId, vmwareNodePoolsId` | Unenrolls a VMware node pool to Anthos On-Prem API |
