---
title: files
hide_title: false
hide_table_of_contents: false
keywords:
  - files
  - artifactregistry
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
<tr><td><b>Name</b></td><td><code>files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.artifactregistry.files</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the file, for example: "projects/p1/locations/us-central1/repositories/repo1/files/a%2Fb%2Fc.txt". If the file ID part contains slashes, they are escaped. |
| `owner` | `string` | The name of the Package or Version that owns this file, if any. |
| `sizeBytes` | `string` | The size of the File in bytes. |
| `updateTime` | `string` | The time when the File was last updated. |
| `createTime` | `string` | The time when the File was created. |
| `hashes` | `array` | The hashes of the file content. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_repositories_files_get` | `SELECT` | `filesId, locationsId, projectsId, repositoriesId` | Gets a file. |
| `projects_locations_repositories_files_list` | `SELECT` | `locationsId, projectsId, repositoriesId` | Lists files. |
