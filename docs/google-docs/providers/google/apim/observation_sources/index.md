---
title: observation_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - observation_sources
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

Creates, updates, deletes, gets or lists a <code>observation_sources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>observation_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apim.observation_sources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. name of resource For MVP, each region can only have 1 source. |
| <CopyableCode code="createTime" /> | `string` | Output only. [Output only] Create time stamp |
| <CopyableCode code="gclbObservationSource" /> | `object` | The GCLB observation source. |
| <CopyableCode code="state" /> | `string` | Output only. The observation source state |
| <CopyableCode code="updateTime" /> | `string` | Output only. [Output only] Update time stamp |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, observationSourcesId, projectsId" /> | GetObservationSource retrieves a single ObservationSource by name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | ListObservationSources gets all ObservationSources for a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | CreateObservationSource creates a new ObservationSource but does not affect any deployed infrastructure. It is a configuration that can be used in an Observation Job to collect data about APIs running in user's dataplane. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, observationSourcesId, projectsId" /> | DeleteObservationSource deletes an observation source. This method will fail if the observation source is currently being used by any ObservationJob, even if not enabled. |

## `SELECT` examples

ListObservationSources gets all ObservationSources for a given project and location.

```sql
SELECT
name,
createTime,
gclbObservationSource,
state,
updateTime
FROM google.apim.observation_sources
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>observation_sources</code> resource.

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
INSERT INTO google.apim.observation_sources (
locationsId,
projectsId,
gclbObservationSource,
name,
state,
createTime,
updateTime
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ gclbObservationSource }}',
'{{ name }}',
'{{ state }}',
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
      - name: gclbObservationSource
        value: '{{ gclbObservationSource }}'
      - name: name
        value: '{{ name }}'
      - name: state
        value: '{{ state }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>observation_sources</code> resource.

```sql
/*+ delete */
DELETE FROM google.apim.observation_sources
WHERE locationsId = '{{ locationsId }}'
AND observationSourcesId = '{{ observationSourcesId }}'
AND projectsId = '{{ projectsId }}';
```
