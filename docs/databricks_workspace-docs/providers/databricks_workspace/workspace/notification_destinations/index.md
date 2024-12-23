---
title: notification_destinations
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - notification_destinations
  - workspace
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

Operations on a <code>notification_destinations</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notification_destinations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workspace.notification_destinations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="destination_type" /> | `string` |
| <CopyableCode code="display_name" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="id, deployment_name" /> | Gets a notification destination. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Lists notification destinations. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a notification destination. Requires workspace admin permissions. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="id, deployment_name" /> | Deletes a notification destination. Requires workspace admin permissions. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="id, deployment_name" /> | Updates a notification destination. Requires workspace admin permissions. At least one field is required in the request body. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'notification_destinations (list)', value: 'list' },
        { label: 'notification_destinations (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
id,
destination_type,
display_name
FROM databricks_workspace.workspace.notification_destinations
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
id,
destination_type,
display_name
FROM databricks_workspace.workspace.notification_destinations
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>notification_destinations</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'notification_destinations', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.workspace.notification_destinations (
deployment_name,
data__config,
data__display_name
)
SELECT 
'{{ deployment_name }}',
'{{ config }}',
'{{ display_name }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: config
    value:
      generic_webhook:
        password: my-password
        url: https://my-webhook.com
        username: my-username
  - name: display_name
    value: My webhook destination

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>notification_destinations</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.workspace.notification_destinations
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>notification_destinations</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.workspace.notification_destinations
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```
