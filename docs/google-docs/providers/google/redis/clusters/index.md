---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - redis
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.redis.clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Unique name of the resource in this scope including project and location using the form: `projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/clusters/&#123;cluster_id&#125;` |
| <CopyableCode code="authorizationMode" /> | `string` | Optional. The authorization mode of the Redis cluster. If not provided, auth feature is disabled for the cluster. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp associated with the cluster creation request. |
| <CopyableCode code="deletionProtectionEnabled" /> | `boolean` | Optional. The delete operation will fail when the value is set to true. |
| <CopyableCode code="discoveryEndpoints" /> | `array` | Output only. Endpoints created on each given network, for Redis clients to connect to the cluster. Currently only one discovery endpoint is supported. |
| <CopyableCode code="nodeType" /> | `string` | Optional. The type of a redis node in the cluster. NodeType determines the underlying machine-type of a redis node. |
| <CopyableCode code="persistenceConfig" /> | `object` | Configuration of the persistence functionality. |
| <CopyableCode code="preciseSizeGb" /> | `number` | Output only. Precise value of redis memory size in GB for the entire cluster. |
| <CopyableCode code="pscConfigs" /> | `array` | Required. Each PscConfig configures the consumer network where IPs will be designated to the cluster for client access through Private Service Connect Automation. Currently, only one PscConfig is supported. |
| <CopyableCode code="pscConnections" /> | `array` | Output only. PSC connections for discovery of the cluster topology and accessing the cluster. |
| <CopyableCode code="redisConfigs" /> | `object` | Optional. Key/Value pairs of customer overrides for mutable Redis Configs |
| <CopyableCode code="replicaCount" /> | `integer` | Optional. The number of replica nodes per shard. |
| <CopyableCode code="shardCount" /> | `integer` | Required. Number of shards for the Redis cluster. |
| <CopyableCode code="sizeGb" /> | `integer` | Output only. Redis memory size in GB for the entire cluster rounded up to the next integer. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of this cluster. Can be CREATING, READY, UPDATING, DELETING and SUSPENDED |
| <CopyableCode code="stateInfo" /> | `object` | Represents additional information about the state of the cluster. |
| <CopyableCode code="transitEncryptionMode" /> | `string` | Optional. The in-transit encryption for the Redis cluster. If not provided, encryption is disabled for the cluster. |
| <CopyableCode code="uid" /> | `string` | Output only. System assigned, unique identifier for the cluster. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Gets the details of a specific Redis cluster. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all Redis clusters owned by a project in either the specified location (region) or all locations. The location should have the following format: * `projects/&#123;project_id&#125;/locations/&#123;location_id&#125;` If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a Redis cluster based on the specified properties. The creation is executed asynchronously and callers may check the returned operation to track its progress. Once the operation is completed the Redis cluster will be fully functional. The completed longrunning.Operation will contain the new cluster object in the response field. The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Deletes a specific Redis cluster. Cluster stops serving and data is deleted. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Updates the metadata and configuration of a specific Redis cluster. Completed longrunning.Operation will contain the new cluster object in the response field. The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists all Redis clusters owned by a project in either the specified location (region) or all locations. The location should have the following format: * `projects/&#123;project_id&#125;/locations/&#123;location_id&#125;` If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated. |
