---
title: files
hide_title: false
hide_table_of_contents: false
keywords:
  - files
  - dfareporting
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.files</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique ID of this report file. |
| `lastModifiedTime` | `string` | The timestamp in milliseconds since epoch when this file was last modified. |
| `urls` | `object` | The URLs where the completed report file can be downloaded. |
| `dateRange` | `object` | Represents a date range. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#file". |
| `format` | `string` | The output format of the report. Only available once the file is available. |
| `etag` | `string` | Etag of this resource. |
| `status` | `string` | The status of the report file. |
| `fileName` | `string` | The filename of the file. |
| `reportId` | `string` | The ID of the report this file was generated from. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `fileId, reportId` | Retrieves a report file by its report ID and file ID. This method supports media download. |
| `list` | `SELECT` | `profileId` | Lists files for a user profile. |
| `reports_files_get` | `SELECT` | `fileId, profileId, reportId` | Retrieves a report file by its report ID and file ID. This method supports media download. |
| `reports_files_list` | `SELECT` | `profileId, reportId` | Lists files for a report. |
