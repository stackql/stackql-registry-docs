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
| `fleets` | `array` | The list of matching fleets. |
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. The token is only valid for 1h. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_locations_fleets_list` | `SELECT` | `locationsId, organizationsId` | Returns all fleets within an organization or a project that the caller has access to. |
| `projects_locations_fleets_list` | `SELECT` | `locationsId, projectsId` | Returns all fleets within an organization or a project that the caller has access to. |
| `projects_locations_fleets_create` | `INSERT` | `locationsId, projectsId` | Creates a fleet. |
| `projects_locations_fleets_delete` | `DELETE` | `fleetsId, locationsId, projectsId` | Removes a Fleet. There must be no memberships remaining in the Fleet. |
| `projects_locations_fleets_get` | `EXEC` | `fleetsId, locationsId, projectsId` | Returns the details of a fleet. |
| `projects_locations_fleets_patch` | `EXEC` | `fleetsId, locationsId, projectsId` | Updates a fleet. |
