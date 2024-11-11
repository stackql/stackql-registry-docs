---
title: integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - integrations
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

Creates, updates, deletes, gets or lists a <code>integrations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.notifications.integrations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="description" /> | `string` | A human readable description for the particular integration |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="display_name" /> | `string` | A human readable name for the particular integration |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="target" /> | `` | Integration-specific details (integration targets) |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_notifications_v1integration" /> | `SELECT` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to read an integration. |
| <CopyableCode code="list_notifications_v1integrations" /> | `SELECT` | <CopyableCode code="" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Retrieve a sorted, filtered, paginated list of all integrations. |
| <CopyableCode code="create_notifications_v1integration" /> | `INSERT` | <CopyableCode code="" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to create an integration. |
| <CopyableCode code="delete_notifications_v1integration" /> | `DELETE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to delete an integration. |
| <CopyableCode code="update_notifications_v1integration" /> | `UPDATE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to update an integration. |
| <CopyableCode code="test_notifications_v1integration" /> | `EXEC` | <CopyableCode code="" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Sends a test notification to validate the integration. This is supported only for Webhook, Slack and MsTeams targets |

## `SELECT` examples

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Retrieve a sorted, filtered, paginated list of all integrations.


```sql
SELECT
id,
description,
api_version,
display_name,
kind,
metadata,
target
FROM confluent.notifications.integrations
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>integrations</code> resource.

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
INSERT INTO confluent.notifications.integrations (
data__display_name,
data__description,
data__target
)
SELECT 
'{{ display_name }}',
'{{ description }}',
'{{ target }}'
;
```
</TabItem>

    <TabItem value="required">

    ```sql
    /*+ create */
    INSERT INTO confluent.notifications.integrations (
    data__display_name,
data__target
    )
    SELECT 
    '{{ display_name }}',
'{{ target }}'
    ;
    ```
    </TabItem>
    
<TabItem value="manifest">

```yaml
- name: integrations
  props:
    - name: display_name
      value: string
    - name: description
      value: string
    - name: target
      props:
        - name: kind
          value: string
        - name: webhook_url
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>integrations</code> resource.

```sql
/*+ update */
UPDATE confluent.notifications.integrations
SET 
display_name = '{{ display_name }}',
description = '{{ description }}',
target = '{{ target }}'
WHERE 
id = '{{ id }}';
```

## `DELETE` example

Deletes the specified <code>integrations</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.notifications.integrations
WHERE id = '{{ id }}';
```
