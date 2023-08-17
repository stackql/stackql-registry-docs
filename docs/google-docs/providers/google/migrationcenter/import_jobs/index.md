---
title: import_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - import_jobs
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
<tr><td><b>Name</b></td><td><code>import_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.migrationcenter.import_jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The full name of the import job. |
| `labels` | `object` | Labels as key value pairs. |
| `completeTime` | `string` | Output only. The timestamp when the import job was completed. |
| `createTime` | `string` | Output only. The timestamp when the import job was created. |
| `updateTime` | `string` | Output only. The timestamp when the import job was last updated. |
| `assetSource` | `string` | Required. Reference to a source. |
| `displayName` | `string` | User-friendly display name. Maximum length is 63 characters. |
| `validationReport` | `object` | A resource that aggregates errors across import job files. |
| `state` | `string` | Output only. The state of the import job. |
| `executionReport` | `object` | A resource that reports result of the import job execution. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `importJobsId, locationsId, projectsId` | Gets the details of an import job. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists all import jobs. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates an import job. |
| `delete` | `DELETE` | `importJobsId, locationsId, projectsId` | Deletes an import job. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists all import jobs. |
| `patch` | `EXEC` | `importJobsId, locationsId, projectsId` | Updates an import job. |
| `run` | `EXEC` | `importJobsId, locationsId, projectsId` | Runs an import job. |
| `validate` | `EXEC` | `importJobsId, locationsId, projectsId` | Validates an import job. |
