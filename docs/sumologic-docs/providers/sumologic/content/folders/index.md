---
title: folders
hide_title: false
hide_table_of_contents: false
keywords:
  - folders
  - content
  - sumologic    
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
<tr><td><b>Name</b></td><td><code>folders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.content.folders</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | The description of the folder. |
| `children` | `array` | A list of the content items. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getFolder` | `SELECT` | `id` | Get a folder with the given identifier. Set the header parameter `isAdminMode` to `"true"` if fetching a folder inside "Admin Recommended" folder. |
| `createFolder` | `INSERT` | `data__name, data__parentId` | Creates a new folder under the given parent folder. Set the header parameter `isAdminMode` to `"true"` to create a folder inside "Admin Recommended" folder. |
| `updateFolder` | `EXEC` | `id, data__name` | Update an existing folder with the given identifier. Set the header parameter `isAdminMode` to `"true"` if updating a folder inside "Admin Recommended" folder. |
