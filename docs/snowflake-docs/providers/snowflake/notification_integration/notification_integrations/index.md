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
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="fetch_notification_integration" /> | `SELECT` | <CopyableCode code="name, endpoint" /> | - | Fetch a notification integration |
| <CopyableCode code="list_notification_integrations" /> | `SELECT` | <CopyableCode code="endpoint" /> | <CopyableCode code="like" /> | List notification integrations |
| <CopyableCode code="create_notification_integration" /> | `INSERT` | <CopyableCode code="data__name, data__notification_hook, endpoint" /> | <CopyableCode code="createMode" /> | Create a notification integration |
| <CopyableCode code="delete_notification_integration" /> | `DELETE` | <CopyableCode code="name, endpoint" /> | <CopyableCode code="ifExists" /> | Delete a notification integration |

<br />


<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="createMode" /> | Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. | `string` | `errorIfExists` |
| <CopyableCode code="ifExists" /> | Query parameter that specifies how to handle the request for a resource that does not exist: - `true`: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - `false`: The endpoint throws an error if the resource doesn't exist. | `boolean` | `false` |
| <CopyableCode code="like" /> | Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. | `string` | `-` |

</details>

## `SELECT` examples

<Tabs
    defaultValue="list_notification_integrations"
    values={[
        { label: 'list_notification_integrations', value: 'list_notification_integrations' },
        { label: 'fetch_notification_integration', value: 'fetch_notification_integration' }
    ]
}>
<TabItem value="list_notification_integrations">

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
</TabItem>
<TabItem value="fetch_notification_integration">

Fetch a notification integration

```sql
SELECT
name,
comment,
created_on,
enabled,
notification_hook
FROM snowflake.notification_integration.notification_integrations
WHERE name = '{{ name }}'
AND endpoint = '{{ endpoint }}';
```
</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>notification_integrations</code> resource.

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
INSERT INTO snowflake.notification_integration.notification_integrations (
data__name,
data__enabled,
data__comment,
data__notification_hook,
endpoint
)
SELECT 
'{{ name }}',
{{ enabled }},
'{{ comment }}',
'{{ notification_hook }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO snowflake.notification_integration.notification_integrations (
data__name,
data__notification_hook,
endpoint
)
SELECT 
'{{ name }}',
'{{ notification_hook }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
# Description fields below are for documentation purposes only and are not required in the manifest
- name: notification_integrations
  props:
    - name: endpoint
      value: string
      description: Required parameter for the notification_integrations resource.
    - name: name
      value: string
      description: Name of the notification.
    - name: enabled
      value: boolean
      description: Whether the notification integration is enabled.
    - name: comment
      value: string
      description: Comment for the notification integration.
    - name: notification_hook
      value:
        - name: type
          value: string
          description: >-
            Type of NotificationHook, can be QUEUE, EMAIL or WEBHOOK (valid
            values: 'EMAIL', 'WEBHOOK', 'QUEUE_AWS_SNS_OUTBOUND',
            'QUEUE_AZURE_EVENT_GRID_OUTBOUND', 'QUEUE_GCP_PUBSUB_OUTBOUND',
            'QUEUE_AZURE_EVENT_GRID_INBOUND', 'QUEUE_GCP_PUBSUB_INBOUND')
```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>notification_integrations</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.notification_integration.notification_integrations
WHERE name = '{{ name }}'
AND endpoint = '{{ endpoint }}';
```
