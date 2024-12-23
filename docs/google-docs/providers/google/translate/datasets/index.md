---
title: datasets
hide_title: false
hide_table_of_contents: false
keywords:
  - datasets
  - translate
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

Creates, updates, deletes, gets or lists a <code>datasets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>datasets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.translate.datasets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the dataset, in form of `projects/{project-number-or-id}/locations/{location_id}/datasets/{dataset_id}` |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this dataset was created. |
| <CopyableCode code="displayName" /> | `string` | The name of the dataset to show in the interface. The name can be up to 32 characters long and can consist only of ASCII Latin letters A-Z and a-z, underscores (_), and ASCII digits 0-9. |
| <CopyableCode code="exampleCount" /> | `integer` | Output only. The number of examples in the dataset. |
| <CopyableCode code="sourceLanguageCode" /> | `string` | The BCP-47 language code of the source language. |
| <CopyableCode code="targetLanguageCode" /> | `string` | The BCP-47 language code of the target language. |
| <CopyableCode code="testExampleCount" /> | `integer` | Output only. Number of test examples (sentence pairs). |
| <CopyableCode code="trainExampleCount" /> | `integer` | Output only. Number of training examples (sentence pairs). |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this dataset was last updated. |
| <CopyableCode code="validateExampleCount" /> | `integer` | Output only. Number of validation examples (sentence pairs). |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_datasets_get" /> | `SELECT` | <CopyableCode code="datasetsId, locationsId, projectsId" /> | Gets a Dataset. |
| <CopyableCode code="projects_locations_datasets_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists datasets. |
| <CopyableCode code="projects_locations_datasets_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a Dataset. |
| <CopyableCode code="projects_locations_datasets_delete" /> | `DELETE` | <CopyableCode code="datasetsId, locationsId, projectsId" /> | Deletes a dataset and all of its contents. |
| <CopyableCode code="projects_locations_datasets_export_data" /> | `EXEC` | <CopyableCode code="datasetsId, locationsId, projectsId" /> | Exports dataset's data to the provided output location. |
| <CopyableCode code="projects_locations_datasets_import_data" /> | `EXEC` | <CopyableCode code="datasetsId, locationsId, projectsId" /> | Import sentence pairs into translation Dataset. |

## `SELECT` examples

Lists datasets.

```sql
SELECT
name,
createTime,
displayName,
exampleCount,
sourceLanguageCode,
targetLanguageCode,
testExampleCount,
trainExampleCount,
updateTime,
validateExampleCount
FROM google.translate.datasets
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>datasets</code> resource.

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
INSERT INTO google.translate.datasets (
locationsId,
projectsId,
name,
displayName,
sourceLanguageCode,
targetLanguageCode
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ sourceLanguageCode }}',
'{{ targetLanguageCode }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: displayName
      value: string
    - name: sourceLanguageCode
      value: string
    - name: targetLanguageCode
      value: string
    - name: exampleCount
      value: integer
    - name: trainExampleCount
      value: integer
    - name: validateExampleCount
      value: integer
    - name: testExampleCount
      value: integer
    - name: createTime
      value: string
    - name: updateTime
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>datasets</code> resource.

```sql
/*+ delete */
DELETE FROM google.translate.datasets
WHERE datasetsId = '{{ datasetsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
