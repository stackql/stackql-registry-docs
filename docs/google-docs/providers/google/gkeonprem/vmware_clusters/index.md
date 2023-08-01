---
title: vmware_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - vmware_clusters
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
<tr><td><b>Name</b></td><td><code>vmware_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkeonprem.vmware_clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `vmwareClusters` | `array` | The list of VMware Cluster. |
| `nextPageToken` | `string` | A token identifying a page of results the server should return. If the token is not empty this means that more results are available and should be retrieved by repeating the request with the provided page token. |
| `unreachable` | `array` | Locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_vmware_clusters_list` | `SELECT` | `locationsId, projectsId` | Lists VMware Clusters in a given project and location. |
| `projects_locations_vmware_clusters_create` | `INSERT` | `locationsId, projectsId` | Creates a new VMware user cluster in a given project and location. |
| `projects_locations_vmware_clusters_delete` | `DELETE` | `locationsId, projectsId, vmwareClustersId` | Deletes a single VMware Cluster. |
| `projects_locations_vmware_clusters_enroll` | `EXEC` | `locationsId, projectsId` | Enrolls an existing VMware user cluster and its node pools to the Anthos On-Prem API within a given project and location. Through enrollment, an existing cluster will become Anthos On-Prem API managed. The corresponding GCP resources will be created and all future modifications to the cluster and/or its node pools will be expected to be performed through the API. |
| `projects_locations_vmware_clusters_get` | `EXEC` | `locationsId, projectsId, vmwareClustersId` | Gets details of a single VMware Cluster. |
| `projects_locations_vmware_clusters_patch` | `EXEC` | `locationsId, projectsId, vmwareClustersId` | Updates the parameters of a single VMware cluster. |
| `projects_locations_vmware_clusters_query_version_config` | `EXEC` | `locationsId, projectsId` | Queries the VMware user cluster version config. |
| `projects_locations_vmware_clusters_unenroll` | `EXEC` | `locationsId, projectsId, vmwareClustersId` | Unenrolls an existing VMware user cluster and its node pools from the Anthos On-Prem API within a given project and location. Unenrollment removes the Cloud reference to the cluster without modifying the underlying OnPrem Resources. Clusters and node pools will continue to run; however, they will no longer be accessible through the Anthos On-Prem API or UI. |
