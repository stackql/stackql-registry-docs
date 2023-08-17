---
title: import_data_files
hide_title: false
hide_table_of_contents: false
keywords:
  - import_data_files
  - migrationcenter
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
<tr><td><b>Name</b></td><td><code>import_data_files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.migrationcenter.import_data_files</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The name of the file. |
| `format` | `string` | Required. The payload format. |
| `state` | `string` | Output only. The state of the import data file. |
| `uploadFileInfo` | `object` | A resource that contains a URI to which a data file can be uploaded. |
| `createTime` | `string` | Output only. The timestamp when the file was created. |
| `displayName` | `string` | User-friendly display name. Maximum length is 63 characters. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `importDataFilesId, importJobsId, locationsId, projectsId` | Gets an import data file. |
| `list` | `SELECT` | `importJobsId, locationsId, projectsId` | List import data files. |
| `create` | `INSERT` | `importJobsId, locationsId, projectsId` | Creates an import data file. |
| `delete` | `DELETE` | `importDataFilesId, importJobsId, locationsId, projectsId` | Delete an import data file. |
| `_list` | `EXEC` | `importJobsId, locationsId, projectsId` | List import data files. |
