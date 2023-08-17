---
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - pubsublite
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
<tr><td><b>Id</b></td><td><code>google.pubsublite.subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the subscription. Structured like: projects/&#123;project_number&#125;/locations/&#123;location&#125;/subscriptions/&#123;subscription_id&#125; |
| `exportConfig` | `object` | Configuration for a Pub/Sub Lite subscription that writes messages to a destination. User subscriber clients must not connect to this subscription. |
| `topic` | `string` | The name of the topic this subscription is attached to. Structured like: projects/&#123;project_number&#125;/locations/&#123;location&#125;/topics/&#123;topic_id&#125; |
| `deliveryConfig` | `object` | The settings for a subscription's message delivery. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `admin_projects_locations_subscriptions_get` | `SELECT` | `locationsId, projectsId, subscriptionsId` | Returns the subscription configuration. |
| `admin_projects_locations_subscriptions_list` | `SELECT` | `locationsId, projectsId` | Returns the list of subscriptions for the given project. |
| `admin_projects_locations_topics_subscriptions_list` | `SELECT` | `locationsId, projectsId, topicsId` | Lists the subscriptions attached to the specified topic. |
| `admin_projects_locations_subscriptions_create` | `INSERT` | `locationsId, projectsId` | Creates a new subscription. |
| `admin_projects_locations_subscriptions_delete` | `DELETE` | `locationsId, projectsId, subscriptionsId` | Deletes the specified subscription. |
| `_admin_projects_locations_subscriptions_list` | `EXEC` | `locationsId, projectsId` | Returns the list of subscriptions for the given project. |
| `_admin_projects_locations_topics_subscriptions_list` | `EXEC` | `locationsId, projectsId, topicsId` | Lists the subscriptions attached to the specified topic. |
| `admin_projects_locations_subscriptions_patch` | `EXEC` | `locationsId, projectsId, subscriptionsId` | Updates properties of the specified subscription. |
| `admin_projects_locations_subscriptions_seek` | `EXEC` | `locationsId, projectsId, subscriptionsId` | Performs an out-of-band seek for a subscription to a specified target, which may be timestamps or named positions within the message backlog. Seek translates these targets to cursors for each partition and orchestrates subscribers to start consuming messages from these seek cursors. If an operation is returned, the seek has been registered and subscribers will eventually receive messages from the seek cursors (i.e. eventual consistency), as long as they are using a minimum supported client library version and not a system that tracks cursors independently of Pub/Sub Lite (e.g. Apache Beam, Dataflow, Spark). The seek operation will fail for unsupported clients. If clients would like to know when subscribers react to the seek (or not), they can poll the operation. The seek operation will succeed and complete once subscribers are ready to receive messages from the seek cursors for all partitions of the topic. This means that the seek operation will not complete until all subscribers come online. If the previous seek operation has not yet completed, it will be aborted and the new invocation of seek will supersede it. |
| `cursor_projects_locations_subscriptions_commit_cursor` | `EXEC` | `locationsId, projectsId, subscriptionsId` | Updates the committed cursor. |
