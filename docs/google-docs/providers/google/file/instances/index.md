---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - file
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
<tr><td><b>Id</b></td><td><code>google.file.instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `instances` | `array` | A list of instances in the project for the specified location. If the `&#123;location&#125;` value in the request is "-", the response contains a list of instances from all locations. If any location is unreachable, the response will only return instances in reachable locations and the "unreachable" field will be populated with a list of unreachable locations. |
| `nextPageToken` | `string` | The token you can use to retrieve the next page of results. Not returned if there are no more results in the list. |
| `unreachable` | `array` | Locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `instancesId, locationsId, projectsId` | Gets the details of a specific instance. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists all instances in a project for either a specified location or for all locations. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates an instance. When creating from a backup, the capacity of the new instance needs to be equal to or larger than the capacity of the backup (and also equal to or larger than the minimum capacity of the tier). |
| `delete` | `DELETE` | `instancesId, locationsId, projectsId` | Deletes an instance. |
| `patch` | `EXEC` | `instancesId, locationsId, projectsId` | Updates the settings of a specific instance. |
| `restore` | `EXEC` | `instancesId, locationsId, projectsId` | Restores an existing instance's file share from a backup. The capacity of the instance needs to be equal to or larger than the capacity of the backup (and also equal to or larger than the minimum capacity of the tier). |
| `revert` | `EXEC` | `instancesId, locationsId, projectsId` | Revert an existing instance's file system to a specified snapshot. |
