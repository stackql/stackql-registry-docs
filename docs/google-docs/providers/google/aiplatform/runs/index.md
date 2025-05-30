---
title: runs
hide_title: false
hide_table_of_contents: false
keywords:
  - runs
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

Creates, updates, deletes, gets or lists a <code>runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.runs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Name of the TensorboardRun. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}` |
| <CopyableCode code="description" /> | `string` | Description of this TensorboardRun. |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this TensorboardRun was created. |
| <CopyableCode code="displayName" /> | `string` | Required. User provided name of this TensorboardRun. This value must be unique among all TensorboardRuns belonging to the same parent TensorboardExperiment. |
| <CopyableCode code="etag" /> | `string` | Used to perform a consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="labels" /> | `object` | The labels with user-defined metadata to organize your TensorboardRuns. This field will be used to filter and visualize Runs in the Tensorboard UI. For example, a Vertex AI training job can set a label aiplatform.googleapis.com/training_job_id=xxxxx to all the runs created within that job. An end user can set a label experiment_id=xxxxx for all the runs produced in a Jupyter notebook. These runs can be grouped by a label value and visualized together in the Tensorboard UI. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one TensorboardRun (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this TensorboardRun was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="experimentsId, locationsId, projectsId, runsId, tensorboardsId" /> | Gets a TensorboardRun. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="experimentsId, locationsId, projectsId, tensorboardsId" /> | Lists TensorboardRuns in a Location. |
| <CopyableCode code="batch_create" /> | `INSERT` | <CopyableCode code="experimentsId, locationsId, projectsId, tensorboardsId" /> | Batch create TensorboardRuns. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="experimentsId, locationsId, projectsId, tensorboardsId" /> | Creates a TensorboardRun. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="experimentsId, locationsId, projectsId, runsId, tensorboardsId" /> | Deletes a TensorboardRun. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="experimentsId, locationsId, projectsId, runsId, tensorboardsId" /> | Updates a TensorboardRun. |
| <CopyableCode code="write" /> | `EXEC` | <CopyableCode code="experimentsId, locationsId, projectsId, runsId, tensorboardsId" /> | Write time series data points into multiple TensorboardTimeSeries under a TensorboardRun. If any data fail to be ingested, an error is returned. |

## `SELECT` examples

Lists TensorboardRuns in a Location.

```sql
SELECT
name,
description,
createTime,
displayName,
etag,
labels,
updateTime
FROM google.aiplatform.runs
WHERE experimentsId = '{{ experimentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND tensorboardsId = '{{ tensorboardsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>runs</code> resource.

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
INSERT INTO google.aiplatform.runs (
experimentsId,
locationsId,
projectsId,
tensorboardsId,
requests
)
SELECT 
'{{ experimentsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ tensorboardsId }}',
'{{ requests }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: requests
      value:
        - - name: tensorboardRunId
            value: string
          - name: parent
            value: string
          - name: tensorboardRun
            value:
              - name: createTime
                value: string
              - name: updateTime
                value: string
              - name: description
                value: string
              - name: labels
                value: object
              - name: name
                value: string
              - name: etag
                value: string
              - name: displayName
                value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>runs</code> resource.

```sql
/*+ update */
UPDATE google.aiplatform.runs
SET 
description = '{{ description }}',
labels = '{{ labels }}',
etag = '{{ etag }}',
displayName = '{{ displayName }}'
WHERE 
experimentsId = '{{ experimentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND runsId = '{{ runsId }}'
AND tensorboardsId = '{{ tensorboardsId }}';
```

## `DELETE` example

Deletes the specified <code>runs</code> resource.

```sql
/*+ delete */
DELETE FROM google.aiplatform.runs
WHERE experimentsId = '{{ experimentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND runsId = '{{ runsId }}'
AND tensorboardsId = '{{ tensorboardsId }}';
```
