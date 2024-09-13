---
title: experiments
hide_title: false
hide_table_of_contents: false
keywords:
  - experiments
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

Creates, updates, deletes, gets or lists a <code>experiments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>experiments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.experiments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Name of the TensorboardExperiment. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}` |
| <CopyableCode code="description" /> | `string` | Description of this TensorboardExperiment. |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this TensorboardExperiment was created. |
| <CopyableCode code="displayName" /> | `string` | User provided name of this TensorboardExperiment. |
| <CopyableCode code="etag" /> | `string` | Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="labels" /> | `object` | The labels with user-defined metadata to organize your TensorboardExperiment. Label keys and values cannot be longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Dataset (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with `aiplatform.googleapis.com/` and are immutable. The following system labels exist for each Dataset: * `aiplatform.googleapis.com/dataset_metadata_schema`: output only. Its value is the metadata_schema's title. |
| <CopyableCode code="source" /> | `string` | Immutable. Source of the TensorboardExperiment. Example: a custom training job. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this TensorboardExperiment was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="experimentsId, locationsId, projectsId, tensorboardsId" /> | Gets a TensorboardExperiment. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, tensorboardsId" /> | Lists TensorboardExperiments in a Location. |
| <CopyableCode code="batch_create" /> | `INSERT` | <CopyableCode code="experimentsId, locationsId, projectsId, tensorboardsId" /> | Batch create TensorboardTimeSeries that belong to a TensorboardExperiment. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, tensorboardsId" /> | Creates a TensorboardExperiment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="experimentsId, locationsId, projectsId, tensorboardsId" /> | Deletes a TensorboardExperiment. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="experimentsId, locationsId, projectsId, tensorboardsId" /> | Updates a TensorboardExperiment. |
| <CopyableCode code="write" /> | `EXEC` | <CopyableCode code="experimentsId, locationsId, projectsId, tensorboardsId" /> | Write time series data points of multiple TensorboardTimeSeries in multiple TensorboardRun's. If any data fail to be ingested, an error is returned. |

## `SELECT` examples

Lists TensorboardExperiments in a Location.

```sql
SELECT
name,
description,
createTime,
displayName,
etag,
labels,
source,
updateTime
FROM google.aiplatform.experiments
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND tensorboardsId = '{{ tensorboardsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>experiments</code> resource.

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
INSERT INTO google.aiplatform.experiments (
locationsId,
projectsId,
tensorboardsId,
labels,
displayName,
updateTime,
source,
createTime,
etag,
name,
description
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ tensorboardsId }}',
'{{ labels }}',
'{{ displayName }}',
'{{ updateTime }}',
'{{ source }}',
'{{ createTime }}',
'{{ etag }}',
'{{ name }}',
'{{ description }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: labels
        value: '{{ labels }}'
      - name: displayName
        value: '{{ displayName }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: source
        value: '{{ source }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: etag
        value: '{{ etag }}'
      - name: name
        value: '{{ name }}'
      - name: description
        value: '{{ description }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>experiments</code> resource.

```sql
/*+ update */
UPDATE google.aiplatform.experiments
SET 
labels = '{{ labels }}',
displayName = '{{ displayName }}',
updateTime = '{{ updateTime }}',
source = '{{ source }}',
createTime = '{{ createTime }}',
etag = '{{ etag }}',
name = '{{ name }}',
description = '{{ description }}'
WHERE 
experimentsId = '{{ experimentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND tensorboardsId = '{{ tensorboardsId }}';
```

## `DELETE` example

Deletes the specified <code>experiments</code> resource.

```sql
/*+ delete */
DELETE FROM google.aiplatform.experiments
WHERE experimentsId = '{{ experimentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND tensorboardsId = '{{ tensorboardsId }}';
```
