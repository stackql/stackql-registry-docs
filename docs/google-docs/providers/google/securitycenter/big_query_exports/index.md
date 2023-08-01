---
title: big_query_exports
hide_title: false
hide_table_of_contents: false
keywords:
  - big_query_exports
  - securitycenter
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
<tr><td><b>Name</b></td><td><code>big_query_exports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.securitycenter.big_query_exports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `bigQueryExports` | `array` | The BigQuery exports from the specified parent. |
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `folders_big_query_exports_get` | `SELECT` | `bigQueryExportsId, foldersId` | Gets a BigQuery export. |
| `folders_big_query_exports_list` | `SELECT` | `foldersId` | Lists BigQuery exports. Note that when requesting BigQuery exports at a given level all exports under that level are also returned e.g. if requesting BigQuery exports under a folder, then all BigQuery exports immediately under the folder plus the ones created under the projects within the folder are returned. |
| `organizations_big_query_exports_get` | `SELECT` | `bigQueryExportsId, organizationsId` | Gets a BigQuery export. |
| `organizations_big_query_exports_list` | `SELECT` | `organizationsId` | Lists BigQuery exports. Note that when requesting BigQuery exports at a given level all exports under that level are also returned e.g. if requesting BigQuery exports under a folder, then all BigQuery exports immediately under the folder plus the ones created under the projects within the folder are returned. |
| `projects_big_query_exports_get` | `SELECT` | `bigQueryExportsId, projectsId` | Gets a BigQuery export. |
| `projects_big_query_exports_list` | `SELECT` | `projectsId` | Lists BigQuery exports. Note that when requesting BigQuery exports at a given level all exports under that level are also returned e.g. if requesting BigQuery exports under a folder, then all BigQuery exports immediately under the folder plus the ones created under the projects within the folder are returned. |
| `folders_big_query_exports_create` | `INSERT` | `foldersId` | Creates a BigQuery export. |
| `organizations_big_query_exports_create` | `INSERT` | `organizationsId` | Creates a BigQuery export. |
| `projects_big_query_exports_create` | `INSERT` | `projectsId` | Creates a BigQuery export. |
| `folders_big_query_exports_delete` | `DELETE` | `bigQueryExportsId, foldersId` | Deletes an existing BigQuery export. |
| `organizations_big_query_exports_delete` | `DELETE` | `bigQueryExportsId, organizationsId` | Deletes an existing BigQuery export. |
| `projects_big_query_exports_delete` | `DELETE` | `bigQueryExportsId, projectsId` | Deletes an existing BigQuery export. |
| `folders_big_query_exports_patch` | `EXEC` | `bigQueryExportsId, foldersId` | Updates a BigQuery export. |
| `organizations_big_query_exports_patch` | `EXEC` | `bigQueryExportsId, organizationsId` | Updates a BigQuery export. |
| `projects_big_query_exports_patch` | `EXEC` | `bigQueryExportsId, projectsId` | Updates a BigQuery export. |
