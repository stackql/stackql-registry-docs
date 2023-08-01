---
title: bare_metal_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - bare_metal_clusters
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
<tr><td><b>Name</b></td><td><code>bare_metal_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkeonprem.bare_metal_clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `unreachable` | `array` | Locations that could not be reached. |
| `bareMetalClusters` | `array` | The list of bare metal Clusters. |
| `nextPageToken` | `string` | A token identifying a page of results the server should return. If the token is not empty this means that more results are available and should be retrieved by repeating the request with the provided page token. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_bare_metal_clusters_list` | `SELECT` | `locationsId, projectsId` | Lists bare metal clusters in a given project and location. |
| `projects_locations_bare_metal_clusters_create` | `INSERT` | `locationsId, projectsId` | Creates a new bare metal cluster in a given project and location. |
| `projects_locations_bare_metal_clusters_delete` | `DELETE` | `bareMetalClustersId, locationsId, projectsId` | Deletes a single bare metal Cluster. |
| `projects_locations_bare_metal_clusters_enroll` | `EXEC` | `locationsId, projectsId` | Enrolls an existing bare metal user cluster and its node pools to the Anthos On-Prem API within a given project and location. Through enrollment, an existing cluster will become Anthos On-Prem API managed. The corresponding GCP resources will be created and all future modifications to the cluster and/or its node pools will be expected to be performed through the API. |
| `projects_locations_bare_metal_clusters_get` | `EXEC` | `bareMetalClustersId, locationsId, projectsId` | Gets details of a single bare metal Cluster. |
| `projects_locations_bare_metal_clusters_patch` | `EXEC` | `bareMetalClustersId, locationsId, projectsId` | Updates the parameters of a single bare metal Cluster. |
| `projects_locations_bare_metal_clusters_query_version_config` | `EXEC` | `locationsId, projectsId` | Queries the bare metal user cluster version config. |
| `projects_locations_bare_metal_clusters_unenroll` | `EXEC` | `bareMetalClustersId, locationsId, projectsId` | Unenrolls an existing bare metal user cluster and its node pools from the Anthos On-Prem API within a given project and location. Unenrollment removes the Cloud reference to the cluster without modifying the underlying OnPrem Resources. Clusters and node pools will continue to run; however, they will no longer be accessible through the Anthos On-Prem API or its clients. |
