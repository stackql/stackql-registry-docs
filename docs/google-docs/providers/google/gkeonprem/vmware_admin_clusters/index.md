---
title: vmware_admin_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - vmware_admin_clusters
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
<tr><td><b>Name</b></td><td><code>vmware_admin_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkeonprem.vmware_admin_clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `unreachable` | `array` | Locations that could not be reached. |
| `vmwareAdminClusters` | `array` | The list of VMware admin cluster. |
| `nextPageToken` | `string` | A token identifying a page of results the server should return. If the token is not empty this means that more results are available and should be retrieved by repeating the request with the provided page token. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_vmware_admin_clusters_list` | `SELECT` | `locationsId, projectsId` | Lists VMware admin clusters in a given project and location. |
| `projects_locations_vmware_admin_clusters_enroll` | `EXEC` | `locationsId, projectsId` | Enrolls an existing VMware admin cluster to the Anthos On-Prem API within a given project and location. Through enrollment, an existing admin cluster will become Anthos On-Prem API managed. The corresponding GCP resources will be created and all future modifications to the cluster will be expected to be performed through the API. |
| `projects_locations_vmware_admin_clusters_get` | `EXEC` | `locationsId, projectsId, vmwareAdminClustersId` | Gets details of a single VMware admin cluster. |
| `projects_locations_vmware_admin_clusters_patch` | `EXEC` | `locationsId, projectsId, vmwareAdminClustersId` | Updates the parameters of a single VMware admin cluster. |
| `projects_locations_vmware_admin_clusters_unenroll` | `EXEC` | `locationsId, projectsId, vmwareAdminClustersId` | Unenrolls an existing VMware admin cluster from the Anthos On-Prem API within a given project and location. Unenrollment removes the Cloud reference to the cluster without modifying the underlying OnPrem Resources. Clusters will continue to run; however, they will no longer be accessible through the Anthos On-Prem API or its clients. |
