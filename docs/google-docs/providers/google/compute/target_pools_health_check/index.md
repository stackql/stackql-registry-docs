
---
title: target_pools_health_check
hide_title: false
hide_table_of_contents: false
keywords:
  - target_pools_health_check
  - compute
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

Creates, updates, deletes or gets an <code>target_pools_health_check</code> resource or lists <code>target_pools_health_check</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>target_pools_health_check</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.target_pools_health_check" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="add_health_check" /> | `INSERT` | <CopyableCode code="project, region, targetPool" /> | Adds health check URLs to a target pool. |
| <CopyableCode code="remove_health_check" /> | `DELETE` | <CopyableCode code="project, region, targetPool" /> | Removes health check URL from a target pool. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>target_pools_health_check</code> resource.

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
INSERT INTO google.compute.target_pools_health_check (
project,
region,
targetPool,
healthChecks
)
SELECT 
'{{ project }}',
'{{ region }}',
'{{ targetPool }}',
'{{ healthChecks }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: healthChecks
        value: '{{ healthChecks }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified target_pools_health_check resource.

```sql
DELETE FROM google.compute.target_pools_health_check
WHERE project = '{{ project }}'
AND region = '{{ region }}'
AND targetPool = '{{ targetPool }}';
```
