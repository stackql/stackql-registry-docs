---
title: notifications
hide_title: false
hide_table_of_contents: false
keywords:
  - notifications
  - storage
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

Creates, updates, deletes, gets or lists a <code>notifications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notifications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.storage.notifications" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the notification. |
| <CopyableCode code="custom_attributes" /> | `object` | An optional list of additional attributes to attach to each Cloud PubSub message published for this notification subscription. |
| <CopyableCode code="etag" /> | `string` | HTTP 1.1 Entity tag for this subscription notification. |
| <CopyableCode code="event_types" /> | `array` | If present, only send notifications about listed event types. If empty, sent notifications for all event types. |
| <CopyableCode code="kind" /> | `string` | The kind of item this is. For notifications, this is always storage#notification. |
| <CopyableCode code="object_name_prefix" /> | `string` | If present, only apply this notification configuration to object names that begin with this prefix. |
| <CopyableCode code="payload_format" /> | `string` | The desired content of the Payload. |
| <CopyableCode code="selfLink" /> | `string` | The canonical URL of this notification. |
| <CopyableCode code="topic" /> | `string` | The Cloud PubSub topic to which this subscription publishes. Formatted as: '//pubsub.googleapis.com/projects/{project-identifier}/topics/{my-topic}' |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="bucket, notification" /> | View a notification configuration. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="bucket" /> | Retrieves a list of notification subscriptions for a given bucket. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="bucket" /> | Creates a notification subscription for a given bucket. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="bucket, notification" /> | Permanently deletes a notification subscription. |

## `SELECT` examples

Retrieves a list of notification subscriptions for a given bucket.

```sql
SELECT
id,
custom_attributes,
etag,
event_types,
kind,
object_name_prefix,
payload_format,
selfLink,
topic
FROM google.storage.notifications
WHERE bucket = '{{ bucket }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>notifications</code> resource.

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
INSERT INTO google.storage.notifications (
bucket,
custom_attributes,
etag,
event_types,
id,
kind,
object_name_prefix,
payload_format,
selfLink,
topic
)
SELECT 
'{{ bucket }}',
'{{ custom_attributes }}',
'{{ etag }}',
'{{ event_types }}',
'{{ id }}',
'{{ kind }}',
'{{ object_name_prefix }}',
'{{ payload_format }}',
'{{ selfLink }}',
'{{ topic }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: custom_attributes
      value: '{{ custom_attributes }}'
    - name: etag
      value: '{{ etag }}'
    - name: event_types
      value: '{{ event_types }}'
    - name: id
      value: '{{ id }}'
    - name: kind
      value: '{{ kind }}'
    - name: object_name_prefix
      value: '{{ object_name_prefix }}'
    - name: payload_format
      value: '{{ payload_format }}'
    - name: selfLink
      value: '{{ selfLink }}'
    - name: topic
      value: '{{ topic }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>notifications</code> resource.

```sql
/*+ delete */
DELETE FROM google.storage.notifications
WHERE bucket = '{{ bucket }}'
AND notification = '{{ notification }}';
```
