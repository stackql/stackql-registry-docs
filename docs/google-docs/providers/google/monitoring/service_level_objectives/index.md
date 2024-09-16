---
title: service_level_objectives
hide_title: false
hide_table_of_contents: false
keywords:
  - service_level_objectives
  - monitoring
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

Creates, updates, deletes, gets or lists a <code>service_level_objectives</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_level_objectives</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.monitoring.service_level_objectives" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Resource name for this ServiceLevelObjective. The format is: projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID]/serviceLevelObjectives/[SLO_NAME]  |
| <CopyableCode code="calendarPeriod" /> | `string` | A calendar period, semantically "since the start of the current ". At this time, only DAY, WEEK, FORTNIGHT, and MONTH are supported. |
| <CopyableCode code="displayName" /> | `string` | Name used for UI elements listing this SLO. |
| <CopyableCode code="goal" /> | `number` | The fraction of service that must be good in order for this objective to be met. 0 < goal <= 0.9999. |
| <CopyableCode code="rollingPeriod" /> | `string` | A rolling time period, semantically "in the past ". Must be an integer multiple of 1 day no larger than 30 days. |
| <CopyableCode code="serviceLevelIndicator" /> | `object` | A Service-Level Indicator (SLI) describes the "performance" of a service. For some services, the SLI is well-defined. In such cases, the SLI can be described easily by referencing the well-known SLI and providing the needed parameters. Alternatively, a "custom" SLI can be defined with a query to the underlying metric store. An SLI is defined to be good_service / total_service over any queried time interval. The value of performance always falls into the range 0 <= performance <= 1. A custom SLI describes how to compute this ratio, whether this is by dividing values from a pair of time series, cutting a Distribution into good and bad counts, or counting time windows in which the service complies with a criterion. For separation of concerns, a single Service-Level Indicator measures performance for only one aspect of service quality, such as fraction of successful queries or fast-enough queries. |
| <CopyableCode code="userLabels" /> | `object` | Labels which have been used to annotate the service-level objective. Label keys must start with a letter. Label keys and values may contain lowercase letters, numbers, underscores, and dashes. Label keys and values have a maximum length of 63 characters, and must be less than 128 bytes in size. Up to 64 label entries may be stored. For labels which do not have a semantic value, the empty string may be supplied for the label value. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="services_service_level_objectives_get" /> | `SELECT` | <CopyableCode code="name" /> | Get a ServiceLevelObjective by name. |
| <CopyableCode code="services_service_level_objectives_list" /> | `SELECT` | <CopyableCode code="parent, parentType" /> | List the ServiceLevelObjectives for the given Service. |
| <CopyableCode code="services_service_level_objectives_create" /> | `INSERT` | <CopyableCode code="parent, parentType" /> | Create a ServiceLevelObjective for the given Service. |
| <CopyableCode code="services_service_level_objectives_delete" /> | `DELETE` | <CopyableCode code="name" /> | Delete the given ServiceLevelObjective. |
| <CopyableCode code="services_service_level_objectives_patch" /> | `UPDATE` | <CopyableCode code="name" /> | Update the given ServiceLevelObjective. |

## `SELECT` examples

Get a ServiceLevelObjective by name.

```sql
SELECT
name,
calendarPeriod,
displayName,
goal,
rollingPeriod,
serviceLevelIndicator,
userLabels
FROM google.monitoring.service_level_objectives
WHERE name = '{{ name }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>service_level_objectives</code> resource.

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
INSERT INTO google.monitoring.service_level_objectives (
parent,
parentType,
name,
displayName,
serviceLevelIndicator,
goal,
rollingPeriod,
calendarPeriod,
userLabels
)
SELECT 
'{{ parent }}',
'{{ parentType }}',
'{{ name }}',
'{{ displayName }}',
'{{ serviceLevelIndicator }}',
number,
'{{ rollingPeriod }}',
'{{ calendarPeriod }}',
'{{ userLabels }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: displayName
      value: '{{ displayName }}'
    - name: serviceLevelIndicator
      value: '{{ serviceLevelIndicator }}'
    - name: goal
      value: '{{ goal }}'
    - name: rollingPeriod
      value: '{{ rollingPeriod }}'
    - name: calendarPeriod
      value: '{{ calendarPeriod }}'
    - name: userLabels
      value: '{{ userLabels }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>service_level_objectives</code> resource.

```sql
/*+ update */
UPDATE google.monitoring.service_level_objectives
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
serviceLevelIndicator = '{{ serviceLevelIndicator }}',
goal = number,
rollingPeriod = '{{ rollingPeriod }}',
calendarPeriod = '{{ calendarPeriod }}',
userLabels = '{{ userLabels }}'
WHERE 
name = '{{ name }}';
```

## `DELETE` example

Deletes the specified <code>service_level_objectives</code> resource.

```sql
/*+ delete */
DELETE FROM google.monitoring.service_level_objectives
WHERE name = '{{ name }}';
```
