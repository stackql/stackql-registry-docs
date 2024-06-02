---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - bigtableadmin
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
<tr><td><b>Id</b></td><td><CopyableCode code="bigtableadmin.clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The unique name of the cluster. Values are of the form `projects/&#123;project&#125;/instances/&#123;instance&#125;/clusters/a-z*`. |
| <CopyableCode code="clusterConfig" /> | `object` | Configuration for a cluster. |
| <CopyableCode code="defaultStorageType" /> | `string` | Immutable. The type of storage used by this cluster to serve its parent instance's tables, unless explicitly overridden. |
| <CopyableCode code="encryptionConfig" /> | `object` | Cloud Key Management Service (Cloud KMS) settings for a CMEK-protected cluster. |
| <CopyableCode code="location" /> | `string` | Immutable. The location where this cluster's nodes and storage reside. For best performance, clients should be located as close as possible to this cluster. Currently only zones are supported, so values should be of the form `projects/&#123;project&#125;/locations/&#123;zone&#125;`. |
| <CopyableCode code="serveNodes" /> | `integer` | The number of nodes in the cluster. If no value is set, Cloud Bigtable automatically allocates nodes based on your data footprint and optimized for 50% storage utilization. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the cluster. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clustersId, instancesId, projectsId" /> | Gets information about a cluster. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="instancesId, projectsId" /> | Lists information about clusters in an instance. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="instancesId, projectsId" /> | Creates a cluster within an instance. Note that exactly one of Cluster.serve_nodes and Cluster.cluster_config.cluster_autoscaling_config can be set. If serve_nodes is set to non-zero, then the cluster is manually scaled. If cluster_config.cluster_autoscaling_config is non-empty, then autoscaling is enabled. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clustersId, instancesId, projectsId" /> | Deletes a cluster from an instance. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="instancesId, projectsId" /> | Lists information about clusters in an instance. |
| <CopyableCode code="partial_update_cluster" /> | `EXEC` | <CopyableCode code="clustersId, instancesId, projectsId" /> | Partially updates a cluster within a project. This method is the preferred way to update a Cluster. To enable and update autoscaling, set cluster_config.cluster_autoscaling_config. When autoscaling is enabled, serve_nodes is treated as an OUTPUT_ONLY field, meaning that updates to it are ignored. Note that an update cannot simultaneously set serve_nodes to non-zero and cluster_config.cluster_autoscaling_config to non-empty, and also specify both in the update_mask. To disable autoscaling, clear cluster_config.cluster_autoscaling_config, and explicitly set a serve_node count via the update_mask. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="clustersId, instancesId, projectsId" /> | Updates a cluster within an instance. Note that UpdateCluster does not support updating cluster_config.cluster_autoscaling_config. In order to update it, you must use PartialUpdateCluster. |
