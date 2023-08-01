---
title: contentitems
hide_title: false
hide_table_of_contents: false
keywords:
  - contentitems
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
<tr><td><b>Name</b></td><td><code>contentitems</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataplex.contentitems</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `content` | `array` | Content under the given parent lake. |
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_lakes_contentitems_list` | `SELECT` | `lakesId, locationsId, projectsId` | List content. |
| `projects_locations_lakes_contentitems_create` | `INSERT` | `lakesId, locationsId, projectsId` | Create a content. |
| `projects_locations_lakes_contentitems_delete` | `DELETE` | `contentitemsId, lakesId, locationsId, projectsId` | Delete a content. |
| `projects_locations_lakes_contentitems_get` | `EXEC` | `contentitemsId, lakesId, locationsId, projectsId` | Get a content resource. |
| `projects_locations_lakes_contentitems_patch` | `EXEC` | `contentitemsId, lakesId, locationsId, projectsId` | Update a content. Only supports full resource update. |
