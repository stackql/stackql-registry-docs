---
title: content
hide_title: false
hide_table_of_contents: false
keywords:
  - content
  - dataplex
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
<tr><td><b>Name</b></td><td><code>content</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataplex.content</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The relative resource name of the content, of the form: projects/{project_id}/locations/{location_id}/lakes/{lake_id}/content/{content_id} |
| `description` | `string` | Optional. Description of the content. |
| `path` | `string` | Required. The path for the Content file, represented as directory structure. Unique within a lake. Limited to alphanumerics, hyphens, underscores, dots and slashes. |
| `sqlScript` | `object` | Configuration for the Sql Script content. |
| `updateTime` | `string` | Output only. The time when the content was last updated. |
| `uid` | `string` | Output only. System generated globally unique ID for the content. This ID will be different if the content is deleted and re-created with the same name. |
| `createTime` | `string` | Output only. Content creation time. |
| `notebook` | `object` | Configuration for Notebook content. |
| `dataText` | `string` | Required. Content data in string format. |
| `labels` | `object` | Optional. User defined labels for the content. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_lakes_content_get` | `SELECT` | `contentId, lakesId, locationsId, projectsId` | Get a content resource. |
| `projects_locations_lakes_content_list` | `SELECT` | `lakesId, locationsId, projectsId` | List content. |
| `projects_locations_lakes_content_create` | `INSERT` | `lakesId, locationsId, projectsId` | Create a content. |
| `projects_locations_lakes_content_delete` | `DELETE` | `contentId, lakesId, locationsId, projectsId` | Delete a content. |
| `projects_locations_lakes_content_patch` | `EXEC` | `contentId, lakesId, locationsId, projectsId` | Update a content. Only supports full resource update. |
