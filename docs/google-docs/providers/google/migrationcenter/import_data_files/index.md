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
| `unreachable` | `array` | Locations that could not be reached. |
| `importDataFiles` | `array` | The list of import data files. |
| `nextPageToken` | `string` | A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `importDataFilesId, importJobsId, locationsId, projectsId` | Gets an import data file. |
| `list` | `SELECT` | `importJobsId, locationsId, projectsId` | List import data files. |
| `create` | `INSERT` | `importJobsId, locationsId, projectsId` | Creates an import data file. |
| `delete` | `DELETE` | `importDataFilesId, importJobsId, locationsId, projectsId` | Delete an import data file. |
