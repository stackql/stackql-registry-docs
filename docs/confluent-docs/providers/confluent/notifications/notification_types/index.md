---
title: notification_types
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_types
  - notifications
  - confluent    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Confluent Cloud resources using SQL.
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notification_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.notifications.notification_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="description" /> | `string` | Human readable description of the notification type<br /> |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="category" /> | `string` | Represents the group with which the notification is associated.<br />Notifications are grouped under certain categories for better organization.<br />- BILLING_LICENSING: All billing, payments or licensing related notifications are grouped here.<br />- SECURITY: All Confluent Cloud and Platform security related notifications are grouped here.<br />- SERVICE: All Confluent services (eg. Kafka, Schema Registry, Connect etc.) related notifications are<br />  grouped here.<br />- ACCOUNT: All Confluent account related notifications are grouped here.<br />For example: Billing, payment or license related notifications are grouped in BILLING_LICENSING category.<br /> |
| <CopyableCode code="display_name" /> | `string` | Human readable display name of the notification type<br /> |
| <CopyableCode code="is_included_in_plan" /> | `boolean` | Whether this notification is available to subscribe or not<br />as per the user's current billing plan.<br /> |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="severity" /> | `string` | Severity indicates the impact of this notification.<br />- CRITICAL: a high impact notification which needs immediate attention.<br />- WARN: a warning notification which can be addressed now or later.<br />- INFO: an informational notification.<br /> |
| <CopyableCode code="subscription_priority" /> | `string` | Indicates whether the notification is auto-subscribed and if the user can opt-out.<br />- REQUIRED: the user is auto-subscribed to this notification and can't opt-out.<br />- RECOMMENDED: the user is auto-subscribed to this notification and can opt-out.<br />- OPTIONAL: the user is not auto-subscribed to this notification but can explicitly subscribe to it.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_notifications_v1notification_type" /> | `SELECT` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to read a notification type. |
| <CopyableCode code="list_notifications_v1notification_types" /> | `SELECT` |  | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Retrieve a sorted, filtered, paginated list of all notification types. |
