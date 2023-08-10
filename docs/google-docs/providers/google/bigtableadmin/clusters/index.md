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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigtableadmin.clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The unique name of the cluster. Values are of the form `projects/&#123;project&#125;/instances/&#123;instance&#125;/clusters/a-z*`. |
| `encryptionConfig` | `object` | Cloud Key Management Service (Cloud KMS) settings for a CMEK-protected cluster. |
| `location` | `string` | Immutable. The location where this cluster's nodes and storage reside. For best performance, clients should be located as close as possible to this cluster. Currently only zones are supported, so values should be of the form `projects/&#123;project&#125;/locations/&#123;zone&#125;`. |
| `serveNodes` | `integer` | The number of nodes allocated to this cluster. More nodes enable higher throughput and more consistent performance. |
| `state` | `string` | Output only. The current state of the cluster. |
| `clusterConfig` | `object` | Configuration for a cluster. |
| `defaultStorageType` | `string` | Immutable. The type of storage used by this cluster to serve its parent instance's tables, unless explicitly overridden. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clustersId, instancesId, projectsId` | Gets information about a cluster. |
| `list` | `SELECT` | `instancesId, projectsId` | Lists information about clusters in an instance. |
| `create` | `INSERT` | `instancesId, projectsId` | Creates a cluster within an instance. Note that exactly one of Cluster.serve_nodes and Cluster.cluster_config.cluster_autoscaling_config can be set. If serve_nodes is set to non-zero, then the cluster is manually scaled. If cluster_config.cluster_autoscaling_config is non-empty, then autoscaling is enabled. |
| `delete` | `DELETE` | `clustersId, instancesId, projectsId` | Deletes a cluster from an instance. |
| `_list` | `EXEC` | `instancesId, projectsId` | Lists information about clusters in an instance. |
| `partial_update_cluster` | `EXEC` | `clustersId, instancesId, projectsId` | Partially updates a cluster within a project. This method is the preferred way to update a Cluster. To enable and update autoscaling, set cluster_config.cluster_autoscaling_config. When autoscaling is enabled, serve_nodes is treated as an OUTPUT_ONLY field, meaning that updates to it are ignored. Note that an update cannot simultaneously set serve_nodes to non-zero and cluster_config.cluster_autoscaling_config to non-empty, and also specify both in the update_mask. To disable autoscaling, clear cluster_config.cluster_autoscaling_config, and explicitly set a serve_node count via the update_mask. |
| `update` | `EXEC` | `clustersId, instancesId, projectsId` | Updates a cluster within an instance. Note that UpdateCluster does not support updating cluster_config.cluster_autoscaling_config. In order to update it, you must use PartialUpdateCluster. |
