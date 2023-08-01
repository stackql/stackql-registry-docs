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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `views` | `array` | The views that match the request. |
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, viewsId` | Gets a view. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists views. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a view. |
| `delete` | `DELETE` | `locationsId, projectsId, viewsId` | Deletes a view. |
| `patch` | `EXEC` | `locationsId, projectsId, viewsId` | Updates a view. |
