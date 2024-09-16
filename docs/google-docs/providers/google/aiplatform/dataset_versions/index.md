---
title: dataset_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - dataset_versions
  - aiplatform
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

Creates, updates, deletes, gets or lists a <code>dataset_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dataset_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.dataset_versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Identifier. The resource name of the DatasetVersion. |
| <CopyableCode code="bigQueryDatasetName" /> | `string` | Output only. Name of the associated BigQuery dataset. |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this DatasetVersion was created. |
| <CopyableCode code="displayName" /> | `string` | The user-defined name of the DatasetVersion. The name can be up to 128 characters long and can consist of any UTF-8 characters. |
| <CopyableCode code="etag" /> | `string` | Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="metadata" /> | `any` | Required. Output only. Additional information about the DatasetVersion. |
| <CopyableCode code="modelReference" /> | `string` | Output only. Reference to the public base model last used by the dataset version. Only set for prompt dataset versions. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this DatasetVersion was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="datasetVersionsId, datasetsId" /> | Gets a Dataset version. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="datasetsId" /> | Lists DatasetVersions in a Dataset. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="datasetsId" /> | Create a version from a Dataset. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="datasetVersionsId, datasetsId" /> | Deletes a Dataset version. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="datasetVersionsId, datasetsId" /> | Updates a DatasetVersion. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="datasetVersionsId, datasetsId" /> | Restores a dataset version. |

## `SELECT` examples

Lists DatasetVersions in a Dataset.

```sql
SELECT
name,
bigQueryDatasetName,
createTime,
displayName,
etag,
metadata,
modelReference,
satisfiesPzi,
satisfiesPzs,
updateTime
FROM google.aiplatform.dataset_versions
WHERE datasetsId = '{{ datasetsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dataset_versions</code> resource.

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
INSERT INTO google.aiplatform.dataset_versions (
datasetsId,
etag,
displayName
)
SELECT 
'{{ datasetsId }}',
'{{ etag }}',
'{{ displayName }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: etag
      value: '{{ etag }}'
    - name: displayName
      value: '{{ displayName }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>dataset_versions</code> resource.

```sql
/*+ update */
UPDATE google.aiplatform.dataset_versions
SET 
etag = '{{ etag }}',
displayName = '{{ displayName }}'
WHERE 
datasetVersionsId = '{{ datasetVersionsId }}'
AND datasetsId = '{{ datasetsId }}';
```

## `DELETE` example

Deletes the specified <code>dataset_versions</code> resource.

```sql
/*+ delete */
DELETE FROM google.aiplatform.dataset_versions
WHERE datasetVersionsId = '{{ datasetVersionsId }}'
AND datasetsId = '{{ datasetsId }}';
```
