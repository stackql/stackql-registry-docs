---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - redis
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
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.redis.instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Unique name of the resource in this scope including project and location using the form: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` Note: Redis instances are managed and addressed at regional level so location_id here refers to a GCP region; however, users may choose which specific zone (or collection of zones for cross-zone instances) an instance should be provisioned in. Refer to location_id and alternative_location_id fields for more details. |
| `maintenancePolicy` | `object` | Maintenance policy for an instance. |
| `host` | `string` | Output only. Hostname or IP address of the exposed Redis endpoint used by clients to connect to the service. |
| `tier` | `string` | Required. The service tier of the instance. |
| `secondaryIpRange` | `string` | Optional. Additional IP range for node placement. Required when enabling read replicas on an existing instance. For DIRECT_PEERING mode value must be a CIDR range of size /28, or "auto". For PRIVATE_SERVICE_ACCESS mode value must be the name of an allocated address range associated with the private service access connection, or "auto". |
| `serverCaCerts` | `array` | Output only. List of server CA certificates for the instance. |
| `createTime` | `string` | Output only. The time the instance was created. |
| `authEnabled` | `boolean` | Optional. Indicates whether OSS Redis AUTH is enabled for the instance. If set to "true" AUTH is enabled on the instance. Default value is "false" meaning AUTH is disabled. |
| `readEndpointPort` | `integer` | Output only. The port number of the exposed readonly redis endpoint. Standard tier only. Write requests should target 'port'. |
| `connectMode` | `string` | Optional. The network connect mode of the Redis instance. If not provided, the connect mode defaults to DIRECT_PEERING. |
| `state` | `string` | Output only. The current state of this instance. |
| `authorizedNetwork` | `string` | Optional. The full name of the Google Compute Engine [network](https://cloud.google.com/vpc/docs/vpc) to which the instance is connected. If left unspecified, the `default` network will be used. |
| `memorySizeGb` | `integer` | Required. Redis memory size in GiB. |
| `locationId` | `string` | Optional. The zone where the instance will be provisioned. If not provided, the service will choose a zone from the specified region for the instance. For standard tier, additional nodes will be added across multiple zones for protection against zonal failures. If specified, at least one node will be provisioned in this zone. |
| `replicaCount` | `integer` | Optional. The number of replica nodes. The valid range for the Standard Tier with read replicas enabled is [1-5] and defaults to 2. If read replicas are not enabled for a Standard Tier instance, the only valid value is 1 and the default is 1. The valid value for basic tier is 0 and the default is also 0. |
| `currentLocationId` | `string` | Output only. The current zone where the Redis primary node is located. In basic tier, this will always be the same as [location_id]. In standard tier, this can be the zone of any node in the instance. |
| `alternativeLocationId` | `string` | Optional. If specified, at least one node will be provisioned in this zone in addition to the zone specified in location_id. Only applicable to standard tier. If provided, it must be a different zone from the one provided in [location_id]. Additional nodes beyond the first 2 will be placed in zones selected by the service. |
| `persistenceConfig` | `object` | Configuration of the persistence functionality. |
| `redisVersion` | `string` | Optional. The version of Redis software. If not provided, latest supported version will be used. Currently, the supported values are: * `REDIS_3_2` for Redis 3.2 compatibility * `REDIS_4_0` for Redis 4.0 compatibility (default) * `REDIS_5_0` for Redis 5.0 compatibility * `REDIS_6_X` for Redis 6.x compatibility |
| `persistenceIamIdentity` | `string` | Output only. Cloud IAM identity used by import / export operations to transfer data to/from Cloud Storage. Format is "serviceAccount:". The value may change over time for a given instance so should be checked before each import/export operation. |
| `reservedIpRange` | `string` | Optional. For DIRECT_PEERING mode, the CIDR range of internal addresses that are reserved for this instance. Range must be unique and non-overlapping with existing subnets in an authorized network. For PRIVATE_SERVICE_ACCESS mode, the name of one allocated IP address ranges associated with this private service access connection. If not provided, the service will choose an unused /29 block, for example, 10.0.0.0/29 or 192.168.0.0/29. For READ_REPLICAS_ENABLED the default block size is /28. |
| `readEndpoint` | `string` | Output only. Hostname or IP address of the exposed readonly Redis endpoint. Standard tier only. Targets all healthy replica nodes in instance. Replication is asynchronous and replica nodes will exhibit some lag behind the primary. Write requests must target 'host'. |
| `readReplicasMode` | `string` | Optional. Read replicas mode for the instance. Defaults to READ_REPLICAS_DISABLED. |
| `displayName` | `string` | An arbitrary and optional user-provided name for the instance. |
| `redisConfigs` | `object` | Optional. Redis configuration parameters, according to http://redis.io/topics/config. Currently, the only supported parameters are: Redis version 3.2 and newer: * maxmemory-policy * notify-keyspace-events Redis version 4.0 and newer: * activedefrag * lfu-decay-time * lfu-log-factor * maxmemory-gb Redis version 5.0 and newer: * stream-node-max-bytes * stream-node-max-entries |
| `labels` | `object` | Resource labels to represent user provided metadata |
| `port` | `integer` | Output only. The port number of the exposed Redis endpoint. |
| `transitEncryptionMode` | `string` | Optional. The TLS mode of the Redis instance. If not provided, TLS is disabled for the instance. |
| `maintenanceSchedule` | `object` | Upcoming maintenance schedule. If no maintenance is scheduled, fields are not populated. |
| `suspensionReasons` | `array` | Optional. reasons that causes instance in "SUSPENDED" state. |
| `customerManagedKey` | `string` | Optional. The KMS key reference that the customer provides when trying to create the instance. |
| `statusMessage` | `string` | Output only. Additional information about the current status of this instance, if available. |
| `nodes` | `array` | Output only. Info per node. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_instances_get` | `SELECT` | `instancesId, locationsId, projectsId` | Gets the details of a specific Redis instance. |
| `projects_locations_instances_list` | `SELECT` | `locationsId, projectsId` | Lists all Redis instances owned by a project in either the specified location (region) or all locations. The location should have the following format: * `projects/{project_id}/locations/{location_id}` If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated. |
| `projects_locations_instances_create` | `INSERT` | `locationsId, projectsId` | Creates a Redis instance based on the specified tier and memory size. By default, the instance is accessible from the project's [default network](https://cloud.google.com/vpc/docs/vpc). The creation is executed asynchronously and callers may check the returned operation to track its progress. Once the operation is completed the Redis instance will be fully functional. Completed longrunning.Operation will contain the new instance object in the response field. The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation. |
| `projects_locations_instances_delete` | `DELETE` | `instancesId, locationsId, projectsId` | Deletes a specific Redis instance. Instance stops serving and data is deleted. |
| `projects_locations_instances_export` | `EXEC` | `instancesId, locationsId, projectsId` | Export Redis instance data into a Redis RDB format file in Cloud Storage. Redis will continue serving during this operation. The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation. |
| `projects_locations_instances_failover` | `EXEC` | `instancesId, locationsId, projectsId` | Initiates a failover of the primary node to current replica node for a specific STANDARD tier Cloud Memorystore for Redis instance. |
| `projects_locations_instances_import` | `EXEC` | `instancesId, locationsId, projectsId` | Import a Redis RDB snapshot file from Cloud Storage into a Redis instance. Redis may stop serving during this operation. Instance state will be IMPORTING for entire operation. When complete, the instance will contain only data from the imported file. The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation. |
| `projects_locations_instances_patch` | `EXEC` | `instancesId, locationsId, projectsId` | Updates the metadata and configuration of a specific Redis instance. Completed longrunning.Operation will contain the new instance object in the response field. The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation. |
| `projects_locations_instances_rescheduleMaintenance` | `EXEC` | `instancesId, locationsId, projectsId` | Reschedule maintenance for a given instance in a given project and location. |
| `projects_locations_instances_upgrade` | `EXEC` | `instancesId, locationsId, projectsId` | Upgrades Redis instance to the newer Redis version specified in the request. |
