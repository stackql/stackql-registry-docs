
---
title: adaptive_mt_datasets
hide_title: false
hide_table_of_contents: false
keywords:
  - adaptive_mt_datasets
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

Creates, updates, deletes or gets an <code>adaptive_mt_dataset</code> resource or lists <code>adaptive_mt_datasets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>adaptive_mt_datasets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.translate.adaptive_mt_datasets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The resource name of the dataset, in form of `projects/{project-number-or-id}/locations/{location_id}/adaptiveMtDatasets/{dataset_id}` |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this dataset was created. |
| <CopyableCode code="displayName" /> | `string` | The name of the dataset to show in the interface. The name can be up to 32 characters long and can consist only of ASCII Latin letters A-Z and a-z, underscores (_), and ASCII digits 0-9. |
| <CopyableCode code="exampleCount" /> | `integer` | The number of examples in the dataset. |
| <CopyableCode code="sourceLanguageCode" /> | `string` | The BCP-47 language code of the source language. |
| <CopyableCode code="targetLanguageCode" /> | `string` | The BCP-47 language code of the target language. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this dataset was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_adaptive_mt_datasets_get" /> | `SELECT` | <CopyableCode code="adaptiveMtDatasetsId, locationsId, projectsId" /> | Gets the Adaptive MT dataset. |
| <CopyableCode code="projects_locations_adaptive_mt_datasets_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all Adaptive MT datasets for which the caller has read permission. |
| <CopyableCode code="projects_locations_adaptive_mt_datasets_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates an Adaptive MT dataset. |
| <CopyableCode code="projects_locations_adaptive_mt_datasets_delete" /> | `DELETE` | <CopyableCode code="adaptiveMtDatasetsId, locationsId, projectsId" /> | Deletes an Adaptive MT dataset, including all its entries and associated metadata. |
| <CopyableCode code="projects_locations_adaptive_mt_datasets_import_adaptive_mt_file" /> | `EXEC` | <CopyableCode code="adaptiveMtDatasetsId, locationsId, projectsId" /> | Imports an AdaptiveMtFile and adds all of its sentences into the AdaptiveMtDataset. |

## `SELECT` examples

Lists all Adaptive MT datasets for which the caller has read permission.

```sql
SELECT
name,
createTime,
displayName,
exampleCount,
sourceLanguageCode,
targetLanguageCode,
updateTime
FROM google.translate.adaptive_mt_datasets
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>adaptive_mt_datasets</code> resource.

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
INSERT INTO google.translate.adaptive_mt_datasets (
locationsId,
projectsId,
name,
displayName,
sourceLanguageCode,
targetLanguageCode,
exampleCount,
createTime,
updateTime
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ sourceLanguageCode }}',
'{{ targetLanguageCode }}',
'{{ exampleCount }}',
'{{ createTime }}',
'{{ updateTime }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: displayName
        value: '{{ displayName }}'
      - name: sourceLanguageCode
        value: '{{ sourceLanguageCode }}'
      - name: targetLanguageCode
        value: '{{ targetLanguageCode }}'
      - name: exampleCount
        value: '{{ exampleCount }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified adaptive_mt_dataset resource.

```sql
DELETE FROM google.translate.adaptive_mt_datasets
WHERE adaptiveMtDatasetsId = '{{ adaptiveMtDatasetsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
