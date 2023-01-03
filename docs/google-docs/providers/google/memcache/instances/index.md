---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - memcache
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
<tr><td><b>Id</b></td><td><code>google.memcache.instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Unique name of the resource in this scope including project and location using the form: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` Note: Memcached instances are managed and addressed at the regional level so `location_id` here refers to a Google Cloud region; however, users may choose which zones Memcached nodes should be provisioned in within an instance. Refer to zones field for more details. |
| `maintenanceSchedule` | `object` | Upcoming maintenance schedule. |
| `nodeCount` | `integer` | Required. Number of nodes in the Memcached instance. |
| `nodeConfig` | `object` | Configuration for a Memcached Node. |
| `maintenancePolicy` | `object` | Maintenance policy per instance. |
| `createTime` | `string` | Output only. The time the instance was created. |
| `memcacheVersion` | `string` | The major version of Memcached software. If not provided, latest supported version will be used. Currently the latest supported major version is `MEMCACHE_1_5`. The minor version will be automatically determined by our system based on the latest supported minor version. |
| `memcacheFullVersion` | `string` | Output only. The full version of memcached server running on this instance. System automatically determines the full memcached version for an instance based on the input MemcacheVersion. The full version format will be "memcached-1.5.16". |
| `state` | `string` | Output only. The state of this Memcached instance. |
| `updateTime` | `string` | Output only. The time the instance was updated. |
| `parameters` | `object` |  |
| `displayName` | `string` | User provided name for the instance, which is only used for display purposes. Cannot be more than 80 characters. |
| `discoveryEndpoint` | `string` | Output only. Endpoint for the Discovery API. |
| `instanceMessages` | `array` | List of messages that describe the current state of the Memcached instance. |
| `zones` | `array` | Zones in which Memcached nodes should be provisioned. Memcached nodes will be equally distributed across these zones. If not provided, the service will by default create nodes in all zones in the region for the instance. |
| `labels` | `object` | Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources |
| `memcacheNodes` | `array` | Output only. List of Memcached nodes. Refer to Node message for more details. |
| `authorizedNetwork` | `string` | The full name of the Google Compute Engine [network](/compute/docs/networks-and-firewalls#networks) to which the instance is connected. If left unspecified, the `default` network will be used. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_instances_get` | `SELECT` | `instancesId, locationsId, projectsId` | Gets details of a single Instance. |
| `projects_locations_instances_list` | `SELECT` | `locationsId, projectsId` | Lists Instances in a given location. |
| `projects_locations_instances_create` | `INSERT` | `locationsId, projectsId` | Creates a new Instance in a given location. |
| `projects_locations_instances_delete` | `DELETE` | `instancesId, locationsId, projectsId` | Deletes a single Instance. |
| `projects_locations_instances_applyParameters` | `EXEC` | `instancesId, locationsId, projectsId` | `ApplyParameters` restarts the set of specified nodes in order to update them to the current set of parameters for the Memcached Instance. |
| `projects_locations_instances_patch` | `EXEC` | `instancesId, locationsId, projectsId` | Updates an existing Instance in a given project and location. |
| `projects_locations_instances_rescheduleMaintenance` | `EXEC` | `instancesId, locationsId, projectsId` | Reschedules upcoming maintenance event. |
| `projects_locations_instances_updateParameters` | `EXEC` | `instancesId, locationsId, projectsId` | Updates the defined Memcached parameters for an existing instance. This method only stages the parameters, it must be followed by `ApplyParameters` to apply the parameters to nodes of the Memcached instance. |
