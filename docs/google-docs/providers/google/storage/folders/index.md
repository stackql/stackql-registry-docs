---
title: folders
hide_title: false
hide_table_of_contents: false
keywords:
  - folders
  - storage
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

Creates, updates, deletes, gets or lists a <code>folders</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>folders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.storage.folders" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the folder, including the bucket name, folder name. |
| <CopyableCode code="name" /> | `string` | The name of the folder. Required if not specified by URL parameter. |
| <CopyableCode code="bucket" /> | `string` | The name of the bucket containing this folder. |
| <CopyableCode code="createTime" /> | `string` | The creation time of the folder in RFC 3339 format. |
| <CopyableCode code="kind" /> | `string` | The kind of item this is. For folders, this is always storage#folder. |
| <CopyableCode code="metageneration" /> | `string` | The version of the metadata for this folder. Used for preconditions and for detecting changes in metadata. |
| <CopyableCode code="pendingRenameInfo" /> | `object` | Only present if the folder is part of an ongoing rename folder operation. Contains information which can be used to query the operation status. |
| <CopyableCode code="selfLink" /> | `string` | The link to this folder. |
| <CopyableCode code="updateTime" /> | `string` | The modification time of the folder metadata in RFC 3339 format. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="bucket, folder" /> | Returns metadata for the specified folder. Only applicable to buckets with hierarchical namespace enabled. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="bucket" /> | Retrieves a list of folders matching the criteria. Only applicable to buckets with hierarchical namespace enabled. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="bucket" /> | Creates a new folder. Only applicable to buckets with hierarchical namespace enabled. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="bucket, folder" /> | Permanently deletes a folder. Only applicable to buckets with hierarchical namespace enabled. |
| <CopyableCode code="rename" /> | `EXEC` | <CopyableCode code="bucket, destinationFolder, sourceFolder" /> | Renames a source folder to a destination folder. Only applicable to buckets with hierarchical namespace enabled. |

## `SELECT` examples

Retrieves a list of folders matching the criteria. Only applicable to buckets with hierarchical namespace enabled.

```sql
SELECT
id,
name,
bucket,
createTime,
kind,
metageneration,
pendingRenameInfo,
selfLink,
updateTime
FROM google.storage.folders
WHERE bucket = '{{ bucket }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>folders</code> resource.

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
INSERT INTO google.storage.folders (
bucket,
bucket,
metageneration,
name,
pendingRenameInfo
)
SELECT 
'{{ bucket }}',
'{{ bucket }}',
'{{ metageneration }}',
'{{ name }}',
'{{ pendingRenameInfo }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: bucket
      value: '{{ bucket }}'
    - name: metageneration
      value: '{{ metageneration }}'
    - name: name
      value: '{{ name }}'
    - name: pendingRenameInfo
      value:
        - name: operationId
          value: '{{ operationId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>folders</code> resource.

```sql
/*+ delete */
DELETE FROM google.storage.folders
WHERE bucket = '{{ bucket }}'
AND folder = '{{ folder }}';
```
