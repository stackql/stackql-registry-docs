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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `name` | `string` | The relative resource name of this export. See: https://cloud.google.com/apis/design/resource_names#relative_resource_name. Example format: "organizations/{organization_id}/bigQueryExports/{export_id}" Example format: "folders/{folder_id}/bigQueryExports/{export_id}" Example format: "projects/{project_id}/bigQueryExports/{export_id}" This field is provided in responses, and is ignored when provided in create requests. |
| `description` | `string` | The description of the export (max of 1024 characters). |
| `createTime` | `string` | Output only. The time at which the big query export was created. This field is set by the server and will be ignored if provided on export on creation. |
| `dataset` | `string` | The dataset to write findings' updates to. Its format is "projects/[project_id]/datasets/[bigquery_dataset_id]". BigQuery Dataset unique ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_). |
| `filter` | `string` | Expression that defines the filter to apply across create/update events of findings. The expression is a list of zero or more restrictions combined via logical operators `AND` and `OR`. Parentheses are supported, and `OR` has higher precedence than `AND`. Restrictions have the form ` ` and may have a `-` character in front of them to indicate negation. The fields map to those defined in the corresponding resource. The supported operators are: * `=` for all value types. * `&gt;`, `&lt;`, `&gt;=`, `&lt;=` for integer values. * `:`, meaning substring matching, for strings. The supported value types are: * string literals in quotes. * integer literals without quotes. * boolean literals `true` and `false` without quotes. |
| `mostRecentEditor` | `string` | Output only. Email address of the user who last edited the big query export. This field is set by the server and will be ignored if provided on export creation or update. |
| `principal` | `string` | Output only. The service account that needs permission to create table, upload data to the big query dataset. |
| `updateTime` | `string` | Output only. The most recent time at which the big export was updated. This field is set by the server and will be ignored if provided on export creation or update. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `folders_bigQueryExports_get` | `SELECT` | `bigQueryExportsId, foldersId` | Gets a big query export. |
| `folders_bigQueryExports_list` | `SELECT` | `foldersId` | Lists BigQuery exports. Note that when requesting BigQuery exports at a given level all exports under that level are also returned e.g. if requesting BigQuery exports under a folder, then all BigQuery exports immediately under the folder plus the ones created under the projects within the folder are returned. |
| `organizations_bigQueryExports_get` | `SELECT` | `bigQueryExportsId, organizationsId` | Gets a big query export. |
| `organizations_bigQueryExports_list` | `SELECT` | `organizationsId` | Lists BigQuery exports. Note that when requesting BigQuery exports at a given level all exports under that level are also returned e.g. if requesting BigQuery exports under a folder, then all BigQuery exports immediately under the folder plus the ones created under the projects within the folder are returned. |
| `projects_bigQueryExports_get` | `SELECT` | `bigQueryExportsId, projectsId` | Gets a big query export. |
| `projects_bigQueryExports_list` | `SELECT` | `projectsId` | Lists BigQuery exports. Note that when requesting BigQuery exports at a given level all exports under that level are also returned e.g. if requesting BigQuery exports under a folder, then all BigQuery exports immediately under the folder plus the ones created under the projects within the folder are returned. |
| `folders_bigQueryExports_create` | `INSERT` | `foldersId` | Creates a big query export. |
| `organizations_bigQueryExports_create` | `INSERT` | `organizationsId` | Creates a big query export. |
| `projects_bigQueryExports_create` | `INSERT` | `projectsId` | Creates a big query export. |
| `folders_bigQueryExports_delete` | `DELETE` | `bigQueryExportsId, foldersId` | Deletes an existing big query export. |
| `organizations_bigQueryExports_delete` | `DELETE` | `bigQueryExportsId, organizationsId` | Deletes an existing big query export. |
| `projects_bigQueryExports_delete` | `DELETE` | `bigQueryExportsId, projectsId` | Deletes an existing big query export. |
| `folders_bigQueryExports_patch` | `EXEC` | `bigQueryExportsId, foldersId` | Updates a BigQuery export. |
| `organizations_bigQueryExports_patch` | `EXEC` | `bigQueryExportsId, organizationsId` | Updates a BigQuery export. |
| `projects_bigQueryExports_patch` | `EXEC` | `bigQueryExportsId, projectsId` | Updates a BigQuery export. |
