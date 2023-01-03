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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notifications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.storage.notifications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the notification. |
| `topic` | `string` | The Cloud PubSub topic to which this subscription publishes. Formatted as: '//pubsub.googleapis.com/projects/{project-identifier}/topics/{my-topic}' |
| `event_types` | `array` | If present, only send notifications about listed event types. If empty, sent notifications for all event types. |
| `payload_format` | `string` | The desired content of the Payload. |
| `selfLink` | `string` | The canonical URL of this notification. |
| `custom_attributes` | `object` | An optional list of additional attributes to attach to each Cloud PubSub message published for this notification subscription. |
| `object_name_prefix` | `string` | If present, only apply this notification configuration to object names that begin with this prefix. |
| `etag` | `string` | HTTP 1.1 Entity tag for this subscription notification. |
| `kind` | `string` | The kind of item this is. For notifications, this is always storage#notification. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `bucket, notification` | View a notification configuration. |
| `list` | `SELECT` | `bucket` | Retrieves a list of notification subscriptions for a given bucket. |
| `insert` | `INSERT` | `bucket` | Creates a notification subscription for a given bucket. |
| `delete` | `DELETE` | `bucket, notification` | Permanently deletes a notification subscription. |
