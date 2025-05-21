---
title: notification_integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_integrations
  - notification_integration
  - snowflake
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage snowflake resources using SQL
custom_edit_url: null
image: /img/providers/snowflake/stackql-snowflake-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>notification_integrations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notification_integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.notification_integration.notification_integrations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the notification. |
| <CopyableCode code="comment" /> | `string` | Comment for the notification integration. |
| <CopyableCode code="created_on" /> | `string` | Date and time when the notification was created. |
| <CopyableCode code="enabled" /> | `boolean` | Whether the notification integration is enabled. |
| <CopyableCode code="notification_hook" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_notification_integration" /> | `SELECT` | <CopyableCode code="name, endpoint" /> | Fetch a notification integration |
| <CopyableCode code="list_notification_integrations" /> | `SELECT` | <CopyableCode code="endpoint" /> | List notification integrations |
| <CopyableCode code="create_notification_integration" /> | `INSERT` | <CopyableCode code="data__name, data__notification_hook, endpoint" /> | Create a notification integration |
| <CopyableCode code="delete_notification_integration" /> | `DELETE` | <CopyableCode code="name, endpoint" /> | Delete a notification integration |

## `SELECT` examples

List notification integrations


```sql
SELECT
name,
comment,
created_on,
enabled,
notification_hook
FROM snowflake.notification_integration.notification_integrations
WHERE endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>notification_integrations</code> resource.

<Tabs     defaultValue="all"    values={[        { label: 'All Properties', value: 'all' }, { label: 'Manifest', value: 'manifest' }    ]}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO snowflake.notification_integration.notification_integrations (
data__name,
data__notification_hook,
endpoint
)
SELECT 
'{ notification_hook }',
'{ name }',
'{ endpoint }'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: notification_integrations
  props:
  - name: data__name
    value: string
  - name: data__notification_hook
    value: string
  - name: endpoint
    value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>notification_integrations</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.notification_integration.notification_integrations
WHERE name = '{ name }' AND endpoint = '{ endpoint }';
```
