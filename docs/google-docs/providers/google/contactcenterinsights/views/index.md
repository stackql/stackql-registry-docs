---
title: views
hide_title: false
hide_table_of_contents: false
keywords:
  - views
  - contactcenterinsights
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
<tr><td><b>Name</b></td><td><code>views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.contactcenterinsights.views</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The resource name of the view. Format: projects/{project}/locations/{location}/views/{view} |
| `updateTime` | `string` | Output only. The most recent time at which the view was updated. |
| `value` | `string` | String with specific view properties. |
| `createTime` | `string` | Output only. The time at which this view was created. |
| `displayName` | `string` | The human-readable display name of the view. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_views_get` | `SELECT` | `locationsId, projectsId, viewsId` | Gets a view. |
| `projects_locations_views_list` | `SELECT` | `locationsId, projectsId` | Lists views. |
| `projects_locations_views_create` | `INSERT` | `locationsId, projectsId` | Creates a view. |
| `projects_locations_views_delete` | `DELETE` | `locationsId, projectsId, viewsId` | Deletes a view. |
| `projects_locations_views_patch` | `EXEC` | `locationsId, projectsId, viewsId` | Updates a view. |
