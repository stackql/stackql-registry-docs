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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `name` | `string` | Required. Unique name of the resource in this scope including project and location using the form: `projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/instances/&#123;instance_id&#125;` Note: Memcached instances are managed and addressed at the regional level so `location_id` here refers to a Google Cloud region; however, users may choose which zones Memcached nodes should be provisioned in within an instance. Refer to zones field for more details. |
| `state` | `string` | Output only. The state of this Memcached instance. |
| `authorizedNetwork` | `string` | The full name of the Google Compute Engine [network](/compute/docs/networks-and-firewalls#networks) to which the instance is connected. If left unspecified, the `default` network will be used. |
| `nodeCount` | `integer` | Required. Number of nodes in the Memcached instance. |
| `zones` | `array` | Zones in which Memcached nodes should be provisioned. Memcached nodes will be equally distributed across these zones. If not provided, the service will by default create nodes in all zones in the region for the instance. |
| `parameters` | `object` |  |
| `reservedIpRangeId` | `array` | Optional. Contains the id of allocated IP address ranges associated with the private service access connection for example, "test-default" associated with IP range 10.0.0.0/29. |
| `createTime` | `string` | Output only. The time the instance was created. |
| `memcacheVersion` | `string` | The major version of Memcached software. If not provided, latest supported version will be used. Currently the latest supported major version is `MEMCACHE_1_5`. The minor version will be automatically determined by our system based on the latest supported minor version. |
| `memcacheFullVersion` | `string` | Output only. The full version of memcached server running on this instance. System automatically determines the full memcached version for an instance based on the input MemcacheVersion. The full version format will be "memcached-1.5.16". |
| `maintenanceSchedule` | `object` | Upcoming maintenance schedule. |
| `nodeConfig` | `object` | Configuration for a Memcached Node. |
| `labels` | `object` | Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources |
| `instanceMessages` | `array` | List of messages that describe the current state of the Memcached instance. |
| `displayName` | `string` | User provided name for the instance, which is only used for display purposes. Cannot be more than 80 characters. |
| `memcacheNodes` | `array` | Output only. List of Memcached nodes. Refer to Node message for more details. |
| `updateTime` | `string` | Output only. The time the instance was updated. |
| `maintenancePolicy` | `object` | Maintenance policy per instance. |
| `discoveryEndpoint` | `string` | Output only. Endpoint for the Discovery API. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `instancesId, locationsId, projectsId` | Gets details of a single Instance. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists Instances in a given location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new Instance in a given location. |
| `delete` | `DELETE` | `instancesId, locationsId, projectsId` | Deletes a single Instance. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists Instances in a given location. |
| `apply_parameters` | `EXEC` | `instancesId, locationsId, projectsId` | `ApplyParameters` restarts the set of specified nodes in order to update them to the current set of parameters for the Memcached Instance. |
| `patch` | `EXEC` | `instancesId, locationsId, projectsId` | Updates an existing Instance in a given project and location. |
| `reschedule_maintenance` | `EXEC` | `instancesId, locationsId, projectsId` | Reschedules upcoming maintenance event. |
