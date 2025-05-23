---
title: trials_trial_measurement
hide_title: false
hide_table_of_contents: false
keywords:
  - trials_trial_measurement
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

Creates, updates, deletes, gets or lists a <code>trials_trial_measurement</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trials_trial_measurement</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.trials_trial_measurement" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="add_trial_measurement" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, studiesId, trialsId" /> | Adds a measurement of the objective metrics to a Trial. This measurement is assumed to have been taken before the Trial is complete. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>trials_trial_measurement</code> resource.

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
INSERT INTO google.aiplatform.trials_trial_measurement (
locationsId,
projectsId,
studiesId,
trialsId,
measurement
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ studiesId }}',
'{{ trialsId }}',
'{{ measurement }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: measurement
      value:
        - name: stepCount
          value: string
        - name: elapsedDuration
          value: string
        - name: metrics
          value:
            - - name: value
                value: number
              - name: metricId
                value: string

```
</TabItem>
</Tabs>
