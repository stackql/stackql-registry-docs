---
title: observation_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - observation_jobs
  - apim
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

Creates, updates, deletes, gets or lists a <code>observation_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>observation_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apim.observation_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. name of resource Format: projects/{project}/locations/{location}/observationJobs/{observation_job} |
| <CopyableCode code="createTime" /> | `string` | Output only. [Output only] Create time stamp |
| <CopyableCode code="sources" /> | `array` | Optional. These should be of the same kind of source. |
| <CopyableCode code="state" /> | `string` | Output only. The observation job state |
| <CopyableCode code="updateTime" /> | `string` | Output only. [Output only] Update time stamp |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, observationJobsId, projectsId" /> | GetObservationJob retrieves a single ObservationJob by name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | ListObservationJobs gets all ObservationJobs for a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | CreateObservationJob creates a new ObservationJob but does not have any effecton its own. It is a configuration that can be used in an Observation Job to collect data about existing APIs. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, observationJobsId, projectsId" /> | DeleteObservationJob deletes an ObservationJob. This method will fail if the observation job is currently being used by any ObservationSource, even if not enabled. |
| <CopyableCode code="disable" /> | `EXEC` | <CopyableCode code="locationsId, observationJobsId, projectsId" /> | Disables the given ObservationJob. |
| <CopyableCode code="enable" /> | `EXEC` | <CopyableCode code="locationsId, observationJobsId, projectsId" /> | Enables the given ObservationJob. |

## `SELECT` examples

ListObservationJobs gets all ObservationJobs for a given project and location.

```sql
SELECT
name,
createTime,
sources,
state,
updateTime
FROM google.apim.observation_jobs
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>observation_jobs</code> resource.

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
INSERT INTO google.apim.observation_jobs (
locationsId,
projectsId,
name,
sources
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ sources }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: state
      value: string
    - name: sources
      value:
        - string
    - name: createTime
      value: string
    - name: updateTime
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>observation_jobs</code> resource.

```sql
/*+ delete */
DELETE FROM google.apim.observation_jobs
WHERE locationsId = '{{ locationsId }}'
AND observationJobsId = '{{ observationJobsId }}'
AND projectsId = '{{ projectsId }}';
```
