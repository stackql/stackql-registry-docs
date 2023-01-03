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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.pubsub.subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The name of the subscription. It must have the format `"projects/{project}/subscriptions/{subscription}"`. `{subscription}` must start with a letter, and contain only letters (`[A-Za-z]`), numbers (`[0-9]`), dashes (`-`), underscores (`_`), periods (`.`), tildes (`~`), plus (`+`) or percent signs (`%`). It must be between 3 and 255 characters in length, and it must not start with `"goog"`. |
| `ackDeadlineSeconds` | `integer` | The approximate amount of time (on a best-effort basis) Pub/Sub waits for the subscriber to acknowledge receipt before resending the message. In the interval after the message is delivered and before it is acknowledged, it is considered to be *outstanding*. During that time period, the message will not be redelivered (on a best-effort basis). For pull subscriptions, this value is used as the initial value for the ack deadline. To override this value for a given message, call `ModifyAckDeadline` with the corresponding `ack_id` if using non-streaming pull or send the `ack_id` in a `StreamingModifyAckDeadlineRequest` if using streaming pull. The minimum custom deadline you can specify is 10 seconds. The maximum custom deadline you can specify is 600 seconds (10 minutes). If this parameter is 0, a default value of 10 seconds is used. For push delivery, this value is also used to set the request timeout for the call to the push endpoint. If the subscriber never acknowledges the message, the Pub/Sub system will eventually redeliver the message. |
| `detached` | `boolean` | Indicates whether the subscription is detached from its topic. Detached subscriptions don't receive messages from their topic and don't retain any backlog. `Pull` and `StreamingPull` requests will return FAILED_PRECONDITION. If the subscription is a push subscription, pushes to the endpoint will not be made. |
| `messageRetentionDuration` | `string` | How long to retain unacknowledged messages in the subscription's backlog, from the moment a message is published. If `retain_acked_messages` is true, then this also configures the retention of acknowledged messages, and thus configures how far back in time a `Seek` can be done. Defaults to 7 days. Cannot be more than 7 days or less than 10 minutes. |
| `retryPolicy` | `object` | A policy that specifies how Cloud Pub/Sub retries message delivery. Retry delay will be exponential based on provided minimum and maximum backoffs. https://en.wikipedia.org/wiki/Exponential_backoff. RetryPolicy will be triggered on NACKs or acknowledgement deadline exceeded events for a given message. Retry Policy is implemented on a best effort basis. At times, the delay between consecutive deliveries may not match the configuration. That is, delay can be more or less than configured backoff. |
| `retainAckedMessages` | `boolean` | Indicates whether to retain acknowledged messages. If true, then messages are not expunged from the subscription's backlog, even if they are acknowledged, until they fall out of the `message_retention_duration` window. This must be true if you would like to [`Seek` to a timestamp] (https://cloud.google.com/pubsub/docs/replay-overview#seek_to_a_time) in the past to replay previously-acknowledged messages. |
| `labels` | `object` | See Creating and managing labels. |
| `topic` | `string` | Required. The name of the topic from which this subscription is receiving messages. Format is `projects/{project}/topics/{topic}`. The value of this field will be `_deleted-topic_` if the topic has been deleted. |
| `state` | `string` | Output only. An output-only field indicating whether or not the subscription can receive messages. |
| `enableMessageOrdering` | `boolean` | If true, messages published with the same `ordering_key` in `PubsubMessage` will be delivered to the subscribers in the order in which they are received by the Pub/Sub system. Otherwise, they may be delivered in any order. |
| `bigqueryConfig` | `object` | Configuration for a BigQuery subscription. |
| `filter` | `string` | An expression written in the Pub/Sub [filter language](https://cloud.google.com/pubsub/docs/filtering). If non-empty, then only `PubsubMessage`s whose `attributes` field matches the filter are delivered on this subscription. If empty, then no messages are filtered out. |
| `expirationPolicy` | `object` | A policy that specifies the conditions for resource expiration (i.e., automatic resource deletion). |
| `deadLetterPolicy` | `object` | Dead lettering is done on a best effort basis. The same message might be dead lettered multiple times. If validation on any of the fields fails at subscription creation/updation, the create/update subscription request will fail. |
| `pushConfig` | `object` | Configuration for a push delivery endpoint. |
| `topicMessageRetentionDuration` | `string` | Output only. Indicates the minimum duration for which a message is retained after it is published to the subscription's topic. If this field is set, messages published to the subscription's topic in the last `topic_message_retention_duration` are always available to subscribers. See the `message_retention_duration` field in `Topic`. This field is set only in responses from the server; it is ignored if it is set in any requests. |
| `enableExactlyOnceDelivery` | `boolean` | If true, Pub/Sub provides the following guarantees for the delivery of a message with a given value of `message_id` on this subscription: * The message sent to a subscriber is guaranteed not to be resent before the message's acknowledgement deadline expires. * An acknowledged message will not be resent to a subscriber. Note that subscribers may still receive multiple copies of a message when `enable_exactly_once_delivery` is true if the message was published multiple times by a publisher client. These copies are considered distinct by Pub/Sub and have distinct `message_id` values. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_subscriptions_get` | `SELECT` | `projectsId, subscriptionsId` | Gets the configuration details of a subscription. |
| `projects_subscriptions_list` | `SELECT` | `projectsId` | Lists matching subscriptions. |
| `projects_topics_subscriptions_list` | `SELECT` | `projectsId, topicsId` | Lists the names of the attached subscriptions on this topic. |
| `projects_subscriptions_create` | `INSERT` | `projectsId, subscriptionsId` | Creates a subscription to a given topic. See the [resource name rules] (https://cloud.google.com/pubsub/docs/admin#resource_names). If the subscription already exists, returns `ALREADY_EXISTS`. If the corresponding topic doesn't exist, returns `NOT_FOUND`. If the name is not provided in the request, the server will assign a random name for this subscription on the same project as the topic, conforming to the [resource name format] (https://cloud.google.com/pubsub/docs/admin#resource_names). The generated name is populated in the returned Subscription object. Note that for REST API requests, you must specify a name in the request. |
| `projects_subscriptions_delete` | `DELETE` | `projectsId, subscriptionsId` | Deletes an existing subscription. All messages retained in the subscription are immediately dropped. Calls to `Pull` after deletion will return `NOT_FOUND`. After a subscription is deleted, a new one may be created with the same name, but the new one has no association with the old subscription or its topic unless the same topic is specified. |
| `projects_subscriptions_acknowledge` | `EXEC` | `projectsId, subscriptionsId` | Acknowledges the messages associated with the `ack_ids` in the `AcknowledgeRequest`. The Pub/Sub system can remove the relevant messages from the subscription. Acknowledging a message whose ack deadline has expired may succeed, but such a message may be redelivered later. Acknowledging a message more than once will not result in an error. |
| `projects_subscriptions_detach` | `EXEC` | `projectsId, subscriptionsId` | Detaches a subscription from this topic. All messages retained in the subscription are dropped. Subsequent `Pull` and `StreamingPull` requests will return FAILED_PRECONDITION. If the subscription is a push subscription, pushes to the endpoint will stop. |
| `projects_subscriptions_modifyAckDeadline` | `EXEC` | `projectsId, subscriptionsId` | Modifies the ack deadline for a specific message. This method is useful to indicate that more time is needed to process a message by the subscriber, or to make the message available for redelivery if the processing was interrupted. Note that this does not modify the subscription-level `ackDeadlineSeconds` used for subsequent messages. |
| `projects_subscriptions_modifyPushConfig` | `EXEC` | `projectsId, subscriptionsId` | Modifies the `PushConfig` for a specified subscription. This may be used to change a push subscription to a pull one (signified by an empty `PushConfig`) or vice versa, or change the endpoint URL and other attributes of a push subscription. Messages will accumulate for delivery continuously through the call regardless of changes to the `PushConfig`. |
| `projects_subscriptions_patch` | `EXEC` | `projectsId, subscriptionsId` | Updates an existing subscription. Note that certain properties of a subscription, such as its topic, are not modifiable. |
| `projects_subscriptions_pull` | `EXEC` | `projectsId, subscriptionsId` | Pulls messages from the server. The server may return `UNAVAILABLE` if there are too many concurrent pull requests pending for the given subscription. |
| `projects_subscriptions_seek` | `EXEC` | `projectsId, subscriptionsId` | Seeks an existing subscription to a point in time or to a given snapshot, whichever is provided in the request. Snapshots are used in [Seek] (https://cloud.google.com/pubsub/docs/replay-overview) operations, which allow you to manage message acknowledgments in bulk. That is, you can set the acknowledgment state of messages in an existing subscription to the state captured by a snapshot. Note that both the subscription and the snapshot must be on the same topic. |
