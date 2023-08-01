---
title: scopes
hide_title: false
hide_table_of_contents: false
keywords:
  - scopes
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
<tr><td><b>Name</b></td><td><code>scopes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkehub.scopes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token to request the next page of resources from the `ListScopes` method. The value of an empty string means that there are no more resources to return. |
| `scopes` | `array` | The list of Scopes |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_scopes_list` | `SELECT` | `locationsId, projectsId` | Lists Scopes. |
| `projects_locations_scopes_create` | `INSERT` | `locationsId, projectsId` | Creates a Scope. |
| `projects_locations_scopes_delete` | `DELETE` | `locationsId, projectsId, scopesId` | Deletes a Scope. |
| `projects_locations_scopes_get` | `EXEC` | `locationsId, projectsId, scopesId` | Returns the details of a Scope. |
| `projects_locations_scopes_patch` | `EXEC` | `locationsId, projectsId, scopesId` | Updates a scopes. |
