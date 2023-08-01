---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - dataproc
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
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataproc.clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Output only. This token is included in the response if there are more results to fetch. To fetch additional results, provide this value as the page_token in a subsequent ListClustersRequest. |
| `clusters` | `array` | Output only. The clusters in the project. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_regions_clusters_list` | `SELECT` | `projectId, region` | Lists all regions/&#123;region&#125;/clusters in a project alphabetically. |
| `projects_regions_clusters_create` | `INSERT` | `projectId, region` | Creates a cluster in a project. The returned Operation.metadata will be ClusterOperationMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata). |
| `projects_regions_clusters_delete` | `DELETE` | `clusterName, projectId, region` | Deletes a cluster in a project. The returned Operation.metadata will be ClusterOperationMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata). |
| `projects_regions_clusters_diagnose` | `EXEC` | `clusterName, projectId, region` | Gets cluster diagnostic information. The returned Operation.metadata will be ClusterOperationMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata). After the operation completes, Operation.response contains DiagnoseClusterResults (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#diagnoseclusterresults). |
| `projects_regions_clusters_get` | `EXEC` | `clusterName, projectId, region` | Gets the resource representation for a cluster in a project. |
| `projects_regions_clusters_inject_credentials` | `EXEC` | `clustersId, projectsId, regionsId` | Inject encrypted credentials into all of the VMs in a cluster.The target cluster must be a personal auth cluster assigned to the user who is issuing the RPC. |
| `projects_regions_clusters_patch` | `EXEC` | `clusterName, projectId, region` | Updates a cluster in a project. The returned Operation.metadata will be ClusterOperationMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata). The cluster must be in a RUNNING state or an error is returned. |
| `projects_regions_clusters_repair` | `EXEC` | `clusterName, projectId, region` | Repairs a cluster. |
| `projects_regions_clusters_start` | `EXEC` | `clusterName, projectId, region` | Starts a cluster in a project. |
| `projects_regions_clusters_stop` | `EXEC` | `clusterName, projectId, region` | Stops a cluster in a project. |
