---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
  - dataplex
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
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataplex.environments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `environments` | `array` | Environments under the given parent lake. |
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_lakes_environments_list` | `SELECT` | `lakesId, locationsId, projectsId` | Lists environments under the given lake. |
| `projects_locations_lakes_environments_create` | `INSERT` | `lakesId, locationsId, projectsId` | Create an environment resource. |
| `projects_locations_lakes_environments_delete` | `DELETE` | `environmentsId, lakesId, locationsId, projectsId` | Delete the environment resource. All the child resources must have been deleted before environment deletion can be initiated. |
| `projects_locations_lakes_environments_get` | `EXEC` | `environmentsId, lakesId, locationsId, projectsId` | Get environment resource. |
| `projects_locations_lakes_environments_patch` | `EXEC` | `environmentsId, lakesId, locationsId, projectsId` | Update the environment resource. |
