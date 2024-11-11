---
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - notifications
  - confluent
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage confluent resources using SQL
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.notifications.subscriptions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="current_state" /> | `string` | Denotes the state of the subscription. When the subscription is ENABLED, the user will receive notification on the configured Integrations. If the subscription is DISABLED, the user will not recieve any notification for the configured notification type. Note that, you cannot disable a subscription for `REQUIRED` notification type. |
| <CopyableCode code="integrations" /> | `array` | Integrations to which notifications are to be sent. |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="notification_type" /> | `object` | The type of notification to subscribe to. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_notifications_v1subscription" /> | `SELECT` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to read a subscription. |
| <CopyableCode code="list_notifications_v1subscriptions" /> | `SELECT` | <CopyableCode code="" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Retrieve a sorted, filtered, paginated list of all subscriptions. |
| <CopyableCode code="create_notifications_v1subscription" /> | `INSERT` | <CopyableCode code="" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to create a subscription. |
| <CopyableCode code="delete_notifications_v1subscription" /> | `DELETE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to delete a subscription. |
| <CopyableCode code="update_notifications_v1subscription" /> | `UPDATE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to update a subscription. |

## `SELECT` examples

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Retrieve a sorted, filtered, paginated list of all subscriptions.


```sql
SELECT
id,
api_version,
current_state,
integrations,
kind,
metadata,
notification_type
FROM confluent.notifications.subscriptions
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>subscriptions</code> resource.

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
INSERT INTO confluent.notifications.subscriptions (
data__current_state,
data__notification_type,
data__integrations
)
SELECT 
'{{ current_state }}',
'{{ notification_type }}',
'{{ integrations }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO confluent.notifications.subscriptions (
data__notification_type,
data__integrations
)
SELECT 
'{{ notification_type }}',
'{{ integrations }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: subscriptions
  props:
    - name: current_state
      value: string
    - name: notification_type
      props:
        - name: id
          value: string
    - name: integrations
      value: array
      props:
        - name: id
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>subscriptions</code> resource.

```sql
/*+ update */
UPDATE confluent.notifications.subscriptions
SET 
current_state = '{{ current_state }}',
integrations = '{{ integrations }}'
WHERE 
id = '{{ id }}';
```

## `DELETE` example

Deletes the specified <code>subscriptions</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.notifications.subscriptions
WHERE id = '{{ id }}';
```
