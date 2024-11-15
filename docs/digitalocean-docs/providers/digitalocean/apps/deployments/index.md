---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - apps
  - digitalocean
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage digitalocean resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>deployments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.apps.deployments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="cause" /> | `string` |  |
| <CopyableCode code="cloned_from" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="functions" /> | `array` |  |
| <CopyableCode code="jobs" /> | `array` |  |
| <CopyableCode code="phase" /> | `string` |  |
| <CopyableCode code="phase_last_updated_at" /> | `string` |  |
| <CopyableCode code="progress" /> | `object` |  |
| <CopyableCode code="services" /> | `array` |  |
| <CopyableCode code="spec" /> | `object` | The desired configuration of an application. |
| <CopyableCode code="static_sites" /> | `array` |  |
| <CopyableCode code="tier_slug" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="workers" /> | `array` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="apps_get_deployment" /> | `SELECT` | <CopyableCode code="app_id, deployment_id" /> | Retrieve information about an app deployment. |
| <CopyableCode code="apps_list_deployments" /> | `SELECT` | <CopyableCode code="app_id" /> | List all deployments of an app. |
| <CopyableCode code="apps_create_deployment" /> | `INSERT` | <CopyableCode code="app_id" /> | Creating an app deployment will pull the latest changes from your repository and schedule a new deployment for your app. |
| <CopyableCode code="apps_cancel_deployment" /> | `EXEC` | <CopyableCode code="app_id, deployment_id" /> | Immediately cancel an in-progress deployment. |

## `SELECT` examples

List all deployments of an app.


```sql
SELECT
id,
cause,
cloned_from,
created_at,
functions,
jobs,
phase,
phase_last_updated_at,
progress,
services,
spec,
static_sites,
tier_slug,
updated_at,
workers
FROM digitalocean.apps.deployments
WHERE app_id = '{{ app_id }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>deployments</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'Required Properties', value: 'required' },
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO digitalocean.apps.deployments (
data__force_build,
app_id
)
SELECT 
'{{ force_build }}',
'{{ app_id }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO digitalocean.apps.deployments (
app_id
)
SELECT 
'{{ app_id }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: deployments
  props:
    - name: app_id
      value: string
    - name: force_build
      value: boolean

```
</TabItem>
</Tabs>
