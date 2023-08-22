---
title: fleets
hide_title: false
hide_table_of_contents: false
keywords:
  - fleets
  - gkehub
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
<tr><td><b>Name</b></td><td><code>fleets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkehub.fleets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The full, unique resource name of this fleet in the format of `projects/&#123;project&#125;/locations/&#123;location&#125;/fleets/&#123;fleet&#125;`. Each Google Cloud project can have at most one fleet resource, named "default". |
| `state` | `object` | FleetLifecycleState describes the state of a Fleet resource. |
| `uid` | `string` | Output only. Google-generated UUID for this resource. This is unique across all Fleet resources. If a Fleet resource is deleted and another resource with the same name is created, it gets a different uid. |
| `updateTime` | `string` | Output only. When the Fleet was last updated. |
| `createTime` | `string` | Output only. When the Fleet was created. |
| `deleteTime` | `string` | Output only. When the Fleet was deleted. |
| `displayName` | `string` | Optional. A user-assigned display name of the Fleet. When present, it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, single-quote, double-quote, space, and exclamation point. Example: `Production Fleet` |
| `labels` | `object` | Optional. Labels for this Fleet. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_locations_fleets_list` | `SELECT` | `locationsId, organizationsId` | Returns all fleets within an organization or a project that the caller has access to. |
| `projects_locations_fleets_get` | `SELECT` | `fleetsId, locationsId, projectsId` | Returns the details of a fleet. |
| `projects_locations_fleets_list` | `SELECT` | `locationsId, projectsId` | Returns all fleets within an organization or a project that the caller has access to. |
| `projects_locations_fleets_create` | `INSERT` | `locationsId, projectsId` | Creates a fleet. |
| `projects_locations_fleets_delete` | `DELETE` | `fleetsId, locationsId, projectsId` | Removes a Fleet. There must be no memberships remaining in the Fleet. |
| `_organizations_locations_fleets_list` | `EXEC` | `locationsId, organizationsId` | Returns all fleets within an organization or a project that the caller has access to. |
| `_projects_locations_fleets_list` | `EXEC` | `locationsId, projectsId` | Returns all fleets within an organization or a project that the caller has access to. |
| `projects_locations_fleets_patch` | `EXEC` | `fleetsId, locationsId, projectsId` | Updates a fleet. |
