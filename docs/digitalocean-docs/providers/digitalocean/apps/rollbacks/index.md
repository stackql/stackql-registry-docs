---
title: rollbacks
hide_title: false
hide_table_of_contents: false
keywords:
  - rollbacks
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

Creates, updates, deletes, gets or lists a <code>rollbacks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rollbacks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.apps.rollbacks" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="apps_create_rollback" /> | `INSERT` | <CopyableCode code="app_id" /> | Rollback an app to a previous deployment. A new deployment will be created to perform the rollback. The app will be pinned to the rollback deployment preventing any new deployments from being created, either manually or through Auto Deploy on Push webhooks. To resume deployments, the rollback must be either committed or reverted. It is recommended to use the Validate App Rollback endpoint to double check if the rollback is valid and if there are any warnings. |
| <CopyableCode code="apps_commit_rollback" /> | `EXEC` | <CopyableCode code="app_id" /> | Commit an app rollback. This action permanently applies the rollback and unpins the app to resume new deployments. |
| <CopyableCode code="apps_revert_rollback" /> | `EXEC` | <CopyableCode code="app_id" /> | Revert an app rollback. This action reverts the active rollback by creating a new deployment from the latest app spec prior to the rollback and unpins the app to resume new deployments. |
| <CopyableCode code="apps_validate_rollback" /> | `EXEC` | <CopyableCode code="app_id" /> | Check whether an app can be rolled back to a specific deployment. This endpoint can also be used to check if there are any warnings or validation conditions that will cause the rollback to proceed under unideal circumstances. For example, if a component must be rebuilt as part of the rollback causing it to take longer than usual. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>rollbacks</code> resource.

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
INSERT INTO digitalocean.apps.rollbacks (
data__deployment_id,
data__skip_pin,
app_id
)
SELECT 
'{{ deployment_id }}',
'{{ skip_pin }}',
'{{ app_id }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO digitalocean.apps.rollbacks (
app_id
)
SELECT 
'{{ app_id }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: rollbacks
  props:
    - name: app_id
      value: string
    - name: deployment_id
      value: string
    - name: skip_pin
      value: boolean

```
</TabItem>
</Tabs>
