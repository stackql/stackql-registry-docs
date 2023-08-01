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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `unreachable` | `array` | Locations that could not be reached. |
| `instances` | `array` | A list of Redis instances in the project in the specified location, or across all locations. If the `location_id` in the parent field of the request is "-", all regions available to the project are queried, and the results aggregated. If in such an aggregated query a location is unavailable, a placeholder Redis entry is included in the response with the `name` field set to a value of the form `projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/instances/`- and the `status` field set to ERROR and `status_message` field set to "location not available for ListInstances". |
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `instancesId, locationsId, projectsId` | Gets the details of a specific Redis instance. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists all Redis instances owned by a project in either the specified location (region) or all locations. The location should have the following format: * `projects/&#123;project_id&#125;/locations/&#123;location_id&#125;` If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a Redis instance based on the specified tier and memory size. By default, the instance is accessible from the project's [default network](https://cloud.google.com/vpc/docs/vpc). The creation is executed asynchronously and callers may check the returned operation to track its progress. Once the operation is completed the Redis instance will be fully functional. Completed longrunning.Operation will contain the new instance object in the response field. The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation. |
| `delete` | `DELETE` | `instancesId, locationsId, projectsId` | Deletes a specific Redis instance. Instance stops serving and data is deleted. |
| `export` | `EXEC` | `instancesId, locationsId, projectsId` | Export Redis instance data into a Redis RDB format file in Cloud Storage. Redis will continue serving during this operation. The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation. |
| `failover` | `EXEC` | `instancesId, locationsId, projectsId` | Initiates a failover of the primary node to current replica node for a specific STANDARD tier Cloud Memorystore for Redis instance. |
| `import` | `EXEC` | `instancesId, locationsId, projectsId` | Import a Redis RDB snapshot file from Cloud Storage into a Redis instance. Redis may stop serving during this operation. Instance state will be IMPORTING for entire operation. When complete, the instance will contain only data from the imported file. The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation. |
| `patch` | `EXEC` | `instancesId, locationsId, projectsId` | Updates the metadata and configuration of a specific Redis instance. Completed longrunning.Operation will contain the new instance object in the response field. The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation. |
| `reschedule_maintenance` | `EXEC` | `instancesId, locationsId, projectsId` | Reschedule maintenance for a given instance in a given project and location. |
| `upgrade` | `EXEC` | `instancesId, locationsId, projectsId` | Upgrades Redis instance to the newer Redis version specified in the request. |
