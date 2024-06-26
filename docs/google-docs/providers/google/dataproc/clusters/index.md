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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataproc.clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="clusterName" /> | `string` | Required. The cluster name, which must be unique within a project. The name must start with a lowercase letter, and can contain up to 51 lowercase letters, numbers, and hyphens. It cannot end with a hyphen. The name of a deleted cluster can be reused. |
| <CopyableCode code="clusterUuid" /> | `string` | Output only. A cluster UUID (Unique Universal Identifier). Dataproc generates this value when it creates the cluster. |
| <CopyableCode code="config" /> | `object` | The cluster config. |
| <CopyableCode code="labels" /> | `object` | Optional. The labels to associate with this cluster. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a cluster. |
| <CopyableCode code="metrics" /> | `object` | Contains cluster daemon metrics, such as HDFS and YARN stats.Beta Feature: This report is available for testing purposes only. It may be changed before final release. |
| <CopyableCode code="projectId" /> | `string` | Required. The Google Cloud Platform project ID that the cluster belongs to. |
| <CopyableCode code="status" /> | `object` | The status of a cluster and its instances. |
| <CopyableCode code="statusHistory" /> | `array` | Output only. The previous cluster status. |
| <CopyableCode code="virtualClusterConfig" /> | `object` | The Dataproc cluster config for a cluster that does not directly control the underlying compute resources, such as a Dataproc-on-GKE cluster (https://cloud.google.com/dataproc/docs/guides/dpgke/dataproc-gke-overview). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_regions_clusters_get" /> | `SELECT` | <CopyableCode code="clusterName, projectId, region" /> | Gets the resource representation for a cluster in a project. |
| <CopyableCode code="projects_regions_clusters_list" /> | `SELECT` | <CopyableCode code="projectId, region" /> | Lists all regions/&#123;region&#125;/clusters in a project alphabetically. |
| <CopyableCode code="projects_regions_clusters_create" /> | `INSERT` | <CopyableCode code="projectId, region" /> | Creates a cluster in a project. The returned Operation.metadata will be ClusterOperationMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata). |
| <CopyableCode code="projects_regions_clusters_delete" /> | `DELETE` | <CopyableCode code="clusterName, projectId, region" /> | Deletes a cluster in a project. The returned Operation.metadata will be ClusterOperationMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata). |
| <CopyableCode code="projects_regions_clusters_patch" /> | `UPDATE` | <CopyableCode code="clusterName, projectId, region" /> | Updates a cluster in a project. The returned Operation.metadata will be ClusterOperationMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata). The cluster must be in a RUNNING state or an error is returned. |
| <CopyableCode code="_projects_regions_clusters_list" /> | `EXEC` | <CopyableCode code="projectId, region" /> | Lists all regions/&#123;region&#125;/clusters in a project alphabetically. |
| <CopyableCode code="projects_regions_clusters_diagnose" /> | `EXEC` | <CopyableCode code="clusterName, projectId, region" /> | Gets cluster diagnostic information. The returned Operation.metadata will be ClusterOperationMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata). After the operation completes, Operation.response contains DiagnoseClusterResults (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#diagnoseclusterresults). |
| <CopyableCode code="projects_regions_clusters_inject_credentials" /> | `EXEC` | <CopyableCode code="clustersId, projectsId, regionsId" /> | Inject encrypted credentials into all of the VMs in a cluster.The target cluster must be a personal auth cluster assigned to the user who is issuing the RPC. |
| <CopyableCode code="projects_regions_clusters_repair" /> | `EXEC` | <CopyableCode code="clusterName, projectId, region" /> | Repairs a cluster. |
| <CopyableCode code="projects_regions_clusters_start" /> | `EXEC` | <CopyableCode code="clusterName, projectId, region" /> | Starts a cluster in a project. |
| <CopyableCode code="projects_regions_clusters_stop" /> | `EXEC` | <CopyableCode code="clusterName, projectId, region" /> | Stops a cluster in a project. |
