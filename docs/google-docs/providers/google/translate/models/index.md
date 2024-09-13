---
title: models
hide_title: false
hide_table_of_contents: false
keywords:
  - models
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

Creates, updates, deletes or gets an <code>model</code> resource or lists <code>models</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.translate.models" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the model, in form of `projects/{project-number-or-id}/locations/{location_id}/models/{model_id}` |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when the model resource was created, which is also when the training started. |
| <CopyableCode code="dataset" /> | `string` | The dataset from which the model is trained, in form of `projects/{project-number-or-id}/locations/{location_id}/datasets/{dataset_id}` |
| <CopyableCode code="displayName" /> | `string` | The name of the model to show in the interface. The name can be up to 32 characters long and can consist only of ASCII Latin letters A-Z and a-z, underscores (_), and ASCII digits 0-9. |
| <CopyableCode code="sourceLanguageCode" /> | `string` | Output only. The BCP-47 language code of the source language. |
| <CopyableCode code="targetLanguageCode" /> | `string` | Output only. The BCP-47 language code of the target language. |
| <CopyableCode code="testExampleCount" /> | `integer` | Output only. Number of examples (sentence pairs) used to test the model. |
| <CopyableCode code="trainExampleCount" /> | `integer` | Output only. Number of examples (sentence pairs) used to train the model. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this model was last updated. |
| <CopyableCode code="validateExampleCount" /> | `integer` | Output only. Number of examples (sentence pairs) used to validate the model. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_models_get" /> | `SELECT` | <CopyableCode code="locationsId, modelsId, projectsId" /> | Gets a model. |
| <CopyableCode code="projects_locations_models_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists models. |
| <CopyableCode code="projects_locations_models_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a Model. |
| <CopyableCode code="projects_locations_models_delete" /> | `DELETE` | <CopyableCode code="locationsId, modelsId, projectsId" /> | Deletes a model. |

## `SELECT` examples

Lists models.

```sql
SELECT
name,
createTime,
dataset,
displayName,
sourceLanguageCode,
targetLanguageCode,
testExampleCount,
trainExampleCount,
updateTime,
validateExampleCount
FROM google.translate.models
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>models</code> resource.

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
INSERT INTO google.translate.models (
locationsId,
projectsId,
name,
displayName,
dataset,
sourceLanguageCode,
targetLanguageCode,
trainExampleCount,
validateExampleCount,
testExampleCount,
createTime,
updateTime
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ dataset }}',
'{{ sourceLanguageCode }}',
'{{ targetLanguageCode }}',
'{{ trainExampleCount }}',
'{{ validateExampleCount }}',
'{{ testExampleCount }}',
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
      - name: dataset
        value: '{{ dataset }}'
      - name: sourceLanguageCode
        value: '{{ sourceLanguageCode }}'
      - name: targetLanguageCode
        value: '{{ targetLanguageCode }}'
      - name: trainExampleCount
        value: '{{ trainExampleCount }}'
      - name: validateExampleCount
        value: '{{ validateExampleCount }}'
      - name: testExampleCount
        value: '{{ testExampleCount }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified model resource.

```sql
DELETE FROM google.translate.models
WHERE locationsId = '{{ locationsId }}'
AND modelsId = '{{ modelsId }}'
AND projectsId = '{{ projectsId }}';
```
