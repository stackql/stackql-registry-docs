---
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - pubsub
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.pubsub.subscriptions</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_subscriptions_get` | `SELECT` | `projectsId, subscriptionsId` | Gets the configuration details of a subscription. |
| `projects_subscriptions_list` | `SELECT` | `projectsId` | Lists matching subscriptions. |
| `projects_topics_subscriptions_list` | `SELECT` | `projectsId, topicsId` | Lists the names of the attached subscriptions on this topic. |
| `projects_subscriptions_delete` | `DELETE` | `projectsId, subscriptionsId` | Deletes an existing subscription. All messages retained in the subscription are immediately dropped. Calls to `Pull` after deletion will return `NOT_FOUND`. After a subscription is deleted, a new one may be created with the same name, but the new one has no association with the old subscription or its topic unless the same topic is specified. |
| `_projects_subscriptions_list` | `EXEC` | `projectsId` | Lists matching subscriptions. |
| `_projects_topics_subscriptions_list` | `EXEC` | `projectsId, topicsId` | Lists the names of the attached subscriptions on this topic. |
| `projects_subscriptions_acknowledge` | `EXEC` | `projectsId, subscriptionsId` | Acknowledges the messages associated with the `ack_ids` in the `AcknowledgeRequest`. The Pub/Sub system can remove the relevant messages from the subscription. Acknowledging a message whose ack deadline has expired may succeed, but such a message may be redelivered later. Acknowledging a message more than once will not result in an error. |
| `projects_subscriptions_create` | `EXEC` | `projectsId, subscriptionsId` | Creates a subscription to a given topic. See the [resource name rules] (https://cloud.google.com/pubsub/docs/admin#resource_names). If the subscription already exists, returns `ALREADY_EXISTS`. If the corresponding topic doesn't exist, returns `NOT_FOUND`. If the name is not provided in the request, the server will assign a random name for this subscription on the same project as the topic, conforming to the [resource name format] (https://cloud.google.com/pubsub/docs/admin#resource_names). The generated name is populated in the returned Subscription object. Note that for REST API requests, you must specify a name in the request. |
| `projects_subscriptions_detach` | `EXEC` | `projectsId, subscriptionsId` | Detaches a subscription from this topic. All messages retained in the subscription are dropped. Subsequent `Pull` and `StreamingPull` requests will return FAILED_PRECONDITION. If the subscription is a push subscription, pushes to the endpoint will stop. |
| `projects_subscriptions_modify_ack_deadline` | `EXEC` | `projectsId, subscriptionsId` | Modifies the ack deadline for a specific message. This method is useful to indicate that more time is needed to process a message by the subscriber, or to make the message available for redelivery if the processing was interrupted. Note that this does not modify the subscription-level `ackDeadlineSeconds` used for subsequent messages. |
| `projects_subscriptions_modify_push_config` | `EXEC` | `projectsId, subscriptionsId` | Modifies the `PushConfig` for a specified subscription. This may be used to change a push subscription to a pull one (signified by an empty `PushConfig`) or vice versa, or change the endpoint URL and other attributes of a push subscription. Messages will accumulate for delivery continuously through the call regardless of changes to the `PushConfig`. |
| `projects_subscriptions_patch` | `EXEC` | `projectsId, subscriptionsId` | Updates an existing subscription. Note that certain properties of a subscription, such as its topic, are not modifiable. |
| `projects_subscriptions_pull` | `EXEC` | `projectsId, subscriptionsId` | Pulls messages from the server. |
| `projects_subscriptions_seek` | `EXEC` | `projectsId, subscriptionsId` | Seeks an existing subscription to a point in time or to a given snapshot, whichever is provided in the request. Snapshots are used in [Seek] (https://cloud.google.com/pubsub/docs/replay-overview) operations, which allow you to manage message acknowledgments in bulk. That is, you can set the acknowledgment state of messages in an existing subscription to the state captured by a snapshot. Note that both the subscription and the snapshot must be on the same topic. |
