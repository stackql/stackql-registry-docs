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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `labels` | `object` | Optional. The labels to associate with this cluster. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a cluster. |
| `statusHistory` | `array` | Output only. The previous cluster status. |
| `clusterName` | `string` | Required. The cluster name, which must be unique within a project. The name must start with a lowercase letter, and can contain up to 51 lowercase letters, numbers, and hyphens. It cannot end with a hyphen. The name of a deleted cluster can be reused. |
| `metrics` | `object` | Contains cluster daemon metrics, such as HDFS and YARN stats.Beta Feature: This report is available for testing purposes only. It may be changed before final release. |
| `clusterUuid` | `string` | Output only. A cluster UUID (Unique Universal Identifier). Dataproc generates this value when it creates the cluster. |
| `virtualClusterConfig` | `object` | The Dataproc cluster config for a cluster that does not directly control the underlying compute resources, such as a Dataproc-on-GKE cluster (https://cloud.google.com/dataproc/docs/guides/dpgke/dataproc-gke). |
| `projectId` | `string` | Required. The Google Cloud Platform project ID that the cluster belongs to. |
| `config` | `object` | The cluster config. |
| `status` | `object` | The status of a cluster and its instances. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_regions_clusters_get` | `SELECT` | `clusterName, projectId, region` | Gets the resource representation for a cluster in a project. |
| `projects_regions_clusters_list` | `SELECT` | `projectId, region` | Lists all regions/{region}/clusters in a project alphabetically. |
| `projects_regions_clusters_create` | `INSERT` | `projectId, region` | Creates a cluster in a project. The returned Operation.metadata will be ClusterOperationMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata). |
| `projects_regions_clusters_delete` | `DELETE` | `clusterName, projectId, region` | Deletes a cluster in a project. The returned Operation.metadata will be ClusterOperationMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata). |
| `projects_regions_clusters_diagnose` | `EXEC` | `clusterName, projectId, region` | Gets cluster diagnostic information. The returned Operation.metadata will be ClusterOperationMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata). After the operation completes, Operation.response contains DiagnoseClusterResults (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#diagnoseclusterresults). |
| `projects_regions_clusters_injectCredentials` | `EXEC` | `clustersId, projectsId, regionsId` | Inject encrypted credentials into all of the VMs in a cluster.The target cluster must be a personal auth cluster assigned to the user who is issuing the RPC. |
| `projects_regions_clusters_patch` | `EXEC` | `clusterName, projectId, region` | Updates a cluster in a project. The returned Operation.metadata will be ClusterOperationMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata). The cluster must be in a RUNNING state or an error is returned. |
| `projects_regions_clusters_repair` | `EXEC` | `clusterName, projectId, region` | Repairs a cluster. |
| `projects_regions_clusters_start` | `EXEC` | `clusterName, projectId, region` | Starts a cluster in a project. |
| `projects_regions_clusters_stop` | `EXEC` | `clusterName, projectId, region` | Stops a cluster in a project. |
