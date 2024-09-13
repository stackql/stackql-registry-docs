
---
title: trials_measurement
hide_title: false
hide_table_of_contents: false
keywords:
  - trials_measurement
  - ml
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

Creates, updates, deletes or gets an <code>trials_measurement</code> resource or lists <code>trials_measurement</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trials_measurement</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.ml.trials_measurement" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_studies_trials_add_measurement" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, studiesId, trialsId" /> | Adds a measurement of the objective metrics to a trial. This measurement is assumed to have been taken before the trial is complete. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>trials_measurement</code> resource.

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
INSERT INTO google.ml.trials_measurement (
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
resources:
  - name: instance
    props:
      - name: measurement
        value: '{{ measurement }}'

```
</TabItem>
</Tabs>
