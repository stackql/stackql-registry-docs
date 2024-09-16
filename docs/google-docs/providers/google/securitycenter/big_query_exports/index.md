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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>big_query_exports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>big_query_exports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.securitycenter.big_query_exports" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The relative resource name of this export. See: https://cloud.google.com/apis/design/resource_names#relative_resource_name. Example format: "organizations/{organization_id}/bigQueryExports/{export_id}" Example format: "folders/{folder_id}/bigQueryExports/{export_id}" Example format: "projects/{project_id}/bigQueryExports/{export_id}" This field is provided in responses, and is ignored when provided in create requests. |
| <CopyableCode code="description" /> | `string` | The description of the export (max of 1024 characters). |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which the BigQuery export was created. This field is set by the server and will be ignored if provided on export on creation. |
| <CopyableCode code="dataset" /> | `string` | The dataset to write findings' updates to. Its format is "projects/[project_id]/datasets/[bigquery_dataset_id]". BigQuery Dataset unique ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_). |
| <CopyableCode code="filter" /> | `string` | Expression that defines the filter to apply across create/update events of findings. The expression is a list of zero or more restrictions combined via logical operators `AND` and `OR`. Parentheses are supported, and `OR` has higher precedence than `AND`. Restrictions have the form ` ` and may have a `-` character in front of them to indicate negation. The fields map to those defined in the corresponding resource. The supported operators are: * `=` for all value types. * `>`, `<`, `>=`, `<=` for integer values. * `:`, meaning substring matching, for strings. The supported value types are: * string literals in quotes. * integer literals without quotes. * boolean literals `true` and `false` without quotes. |
| <CopyableCode code="mostRecentEditor" /> | `string` | Output only. Email address of the user who last edited the BigQuery export. This field is set by the server and will be ignored if provided on export creation or update. |
| <CopyableCode code="principal" /> | `string` | Output only. The service account that needs permission to create table and upload data to the BigQuery dataset. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The most recent time at which the BigQuery export was updated. This field is set by the server and will be ignored if provided on export creation or update. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="folders_big_query_exports_get" /> | `SELECT` | <CopyableCode code="bigQueryExportsId, foldersId" /> | Gets a BigQuery export. |
| <CopyableCode code="folders_big_query_exports_list" /> | `SELECT` | <CopyableCode code="foldersId" /> | Lists BigQuery exports. Note that when requesting BigQuery exports at a given level all exports under that level are also returned e.g. if requesting BigQuery exports under a folder, then all BigQuery exports immediately under the folder plus the ones created under the projects within the folder are returned. |
| <CopyableCode code="organizations_big_query_exports_get" /> | `SELECT` | <CopyableCode code="bigQueryExportsId, organizationsId" /> | Gets a BigQuery export. |
| <CopyableCode code="organizations_big_query_exports_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists BigQuery exports. Note that when requesting BigQuery exports at a given level all exports under that level are also returned e.g. if requesting BigQuery exports under a folder, then all BigQuery exports immediately under the folder plus the ones created under the projects within the folder are returned. |
| <CopyableCode code="projects_big_query_exports_get" /> | `SELECT` | <CopyableCode code="bigQueryExportsId, projectsId" /> | Gets a BigQuery export. |
| <CopyableCode code="projects_big_query_exports_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists BigQuery exports. Note that when requesting BigQuery exports at a given level all exports under that level are also returned e.g. if requesting BigQuery exports under a folder, then all BigQuery exports immediately under the folder plus the ones created under the projects within the folder are returned. |
| <CopyableCode code="folders_big_query_exports_create" /> | `INSERT` | <CopyableCode code="foldersId" /> | Creates a BigQuery export. |
| <CopyableCode code="organizations_big_query_exports_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates a BigQuery export. |
| <CopyableCode code="projects_big_query_exports_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a BigQuery export. |
| <CopyableCode code="folders_big_query_exports_delete" /> | `DELETE` | <CopyableCode code="bigQueryExportsId, foldersId" /> | Deletes an existing BigQuery export. |
| <CopyableCode code="organizations_big_query_exports_delete" /> | `DELETE` | <CopyableCode code="bigQueryExportsId, organizationsId" /> | Deletes an existing BigQuery export. |
| <CopyableCode code="projects_big_query_exports_delete" /> | `DELETE` | <CopyableCode code="bigQueryExportsId, projectsId" /> | Deletes an existing BigQuery export. |
| <CopyableCode code="folders_big_query_exports_patch" /> | `UPDATE` | <CopyableCode code="bigQueryExportsId, foldersId" /> | Updates a BigQuery export. |
| <CopyableCode code="organizations_big_query_exports_patch" /> | `UPDATE` | <CopyableCode code="bigQueryExportsId, organizationsId" /> | Updates a BigQuery export. |
| <CopyableCode code="projects_big_query_exports_patch" /> | `UPDATE` | <CopyableCode code="bigQueryExportsId, projectsId" /> | Updates a BigQuery export. |

## `SELECT` examples

Lists BigQuery exports. Note that when requesting BigQuery exports at a given level all exports under that level are also returned e.g. if requesting BigQuery exports under a folder, then all BigQuery exports immediately under the folder plus the ones created under the projects within the folder are returned.

```sql
SELECT
name,
description,
createTime,
dataset,
filter,
mostRecentEditor,
principal,
updateTime
FROM google.securitycenter.big_query_exports
WHERE foldersId = '{{ foldersId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>big_query_exports</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.securitycenter.big_query_exports (
foldersId,
name,
description,
filter,
dataset
)
SELECT 
'{{ foldersId }}',
'{{ name }}',
'{{ description }}',
'{{ filter }}',
'{{ dataset }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: description
      value: '{{ description }}'
    - name: filter
      value: '{{ filter }}'
    - name: dataset
      value: '{{ dataset }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>big_query_exports</code> resource.

```sql
/*+ update */
UPDATE google.securitycenter.big_query_exports
SET 
name = '{{ name }}',
description = '{{ description }}',
filter = '{{ filter }}',
dataset = '{{ dataset }}'
WHERE 
bigQueryExportsId = '{{ bigQueryExportsId }}'
AND foldersId = '{{ foldersId }}';
```

## `DELETE` example

Deletes the specified <code>big_query_exports</code> resource.

```sql
/*+ delete */
DELETE FROM google.securitycenter.big_query_exports
WHERE bigQueryExportsId = '{{ bigQueryExportsId }}'
AND foldersId = '{{ foldersId }}';
```
