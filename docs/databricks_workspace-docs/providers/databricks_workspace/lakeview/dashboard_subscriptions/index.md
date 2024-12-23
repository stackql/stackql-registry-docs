---
title: dashboard_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - dashboard_subscriptions
  - lakeview
  - databricks_workspace
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_workspace/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>dashboard_subscriptions</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dashboard_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.lakeview.dashboard_subscriptions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="create_time" /> | `string` |
| <CopyableCode code="created_by_user_id" /> | `string` |
| <CopyableCode code="dashboard_id" /> | `string` |
| <CopyableCode code="etag" /> | `string` |
| <CopyableCode code="schedule_id" /> | `string` |
| <CopyableCode code="subscriber" /> | `object` |
| <CopyableCode code="subscription_id" /> | `string` |
| <CopyableCode code="update_time" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getsubscription" /> | `SELECT` | <CopyableCode code="dashboard_id, schedule_id, subscription_id, deployment_name" /> |  |
| <CopyableCode code="listsubscriptions" /> | `SELECT` | <CopyableCode code="dashboard_id, schedule_id, deployment_name" /> |  |
| <CopyableCode code="createsubscription" /> | `INSERT` | <CopyableCode code="deployment_name" /> |  |
| <CopyableCode code="deletesubscription" /> | `DELETE` | <CopyableCode code="dashboard_id, schedule_id, subscription_id, deployment_name" /> |  |

## `SELECT` examples

<Tabs
    defaultValue="listsubscriptions"
    values={[
        { label: 'dashboard_subscriptions (listsubscriptions)', value: 'listsubscriptions' },
        { label: 'dashboard_subscriptions (getsubscription)', value: 'getsubscription' }
    ]
}>
<TabItem value="listsubscriptions">

```sql
SELECT
create_time,
created_by_user_id,
dashboard_id,
etag,
schedule_id,
subscriber,
subscription_id,
update_time
FROM databricks_workspace.lakeview.dashboard_subscriptions
WHERE dashboard_id = '{{ dashboard_id }}' AND
schedule_id = '{{ schedule_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="getsubscription">

```sql
SELECT
create_time,
created_by_user_id,
dashboard_id,
etag,
schedule_id,
subscriber,
subscription_id,
update_time
FROM databricks_workspace.lakeview.dashboard_subscriptions
WHERE dashboard_id = '{{ dashboard_id }}' AND
schedule_id = '{{ schedule_id }}' AND
subscription_id = '{{ subscription_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dashboard_subscriptions</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'dashboard_subscriptions', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.lakeview.dashboard_subscriptions (
deployment_name,
data__subscriber,
data__etag
)
SELECT 
'{{ deployment_name }}',
'{{ subscriber }}',
'{{ etag }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: subscriber
    value:
      user_subscriber:
        user_id: '3294322584244938'
  - name: etag
    value: '80611980'

```

</TabItem>
</Tabs>

## `DELETE` example

Deletes a <code>dashboard_subscriptions</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.lakeview.dashboard_subscriptions
WHERE dashboard_id = '{{ dashboard_id }}' AND
schedule_id = '{{ schedule_id }}' AND
subscription_id = '{{ subscription_id }}' AND
deployment_name = '{{ deployment_name }}';
```
