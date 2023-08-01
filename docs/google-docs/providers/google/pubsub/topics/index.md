---
title: topics
hide_title: false
hide_table_of_contents: false
keywords:
  - topics
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
<tr><td><b>Name</b></td><td><code>topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.pubsub.topics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `topics` | `array` | Optional. The resulting topics. |
| `nextPageToken` | `string` | Optional. If not empty, indicates that there may be more topics that match the request; this value should be passed in a new `ListTopicsRequest`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_topics_list` | `SELECT` | `projectsId` | Lists matching topics. |
| `projects_topics_delete` | `DELETE` | `projectsId, topicsId` | Deletes the topic with the given name. Returns `NOT_FOUND` if the topic does not exist. After a topic is deleted, a new topic may be created with the same name; this is an entirely new topic with none of the old configuration or subscriptions. Existing subscriptions to this topic are not deleted, but their `topic` field is set to `_deleted-topic_`. |
| `projects_topics_create` | `EXEC` | `projectsId, topicsId` | Creates the given topic with the given name. See the [resource name rules] (https://cloud.google.com/pubsub/docs/admin#resource_names). |
| `projects_topics_get` | `EXEC` | `projectsId, topicsId` | Gets the configuration of a topic. |
| `projects_topics_patch` | `EXEC` | `projectsId, topicsId` | Updates an existing topic. Note that certain properties of a topic are not modifiable. |
| `projects_topics_publish` | `EXEC` | `projectsId, topicsId` | Adds one or more messages to the topic. Returns `NOT_FOUND` if the topic does not exist. |
