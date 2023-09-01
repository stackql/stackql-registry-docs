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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `updateTime` | `string` | Output only. The time when the File was last updated. |
| `createTime` | `string` | Output only. The time when the File was created. |
| `fetchTime` | `string` | Output only. The time when the last attempt to refresh the file's data was made. Only set when the repository is remote. |
| `hashes` | `array` | The hashes of the file content. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `filesId, locationsId, projectsId, repositoriesId` | Gets a file. |
| `list` | `SELECT` | `locationsId, projectsId, repositoriesId` | Lists files. |
| `_list` | `EXEC` | `locationsId, projectsId, repositoriesId` | Lists files. |
