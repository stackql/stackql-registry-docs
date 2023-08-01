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
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
| `unreachable` | `array` | Locations that could not be reached. |
| `instances` | `array` | A list of Memcached instances in the project in the specified location, or across all locations. If the `location_id` in the parent field of the request is "-", all regions available to the project are queried, and the results aggregated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `instancesId, locationsId, projectsId` | Gets details of a single Instance. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists Instances in a given location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new Instance in a given location. |
| `delete` | `DELETE` | `instancesId, locationsId, projectsId` | Deletes a single Instance. |
| `apply_parameters` | `EXEC` | `instancesId, locationsId, projectsId` | `ApplyParameters` restarts the set of specified nodes in order to update them to the current set of parameters for the Memcached Instance. |
| `patch` | `EXEC` | `instancesId, locationsId, projectsId` | Updates an existing Instance in a given project and location. |
| `reschedule_maintenance` | `EXEC` | `instancesId, locationsId, projectsId` | Reschedules upcoming maintenance event. |
