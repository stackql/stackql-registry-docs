---
title: topics
hide_title: false
hide_table_of_contents: false
keywords:
  - topics
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
<tr><td><b>Name</b></td><td><code>topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.pubsublite.topics</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `admin_projects_locations_reservations_topics_list` | `SELECT` | `locationsId, projectsId, reservationsId` | Lists the topics attached to the specified reservation. |
| `admin_projects_locations_topics_get` | `SELECT` | `locationsId, projectsId, topicsId` | Returns the topic configuration. |
| `admin_projects_locations_topics_list` | `SELECT` | `locationsId, projectsId` | Returns the list of topics for the given project. |
| `admin_projects_locations_topics_create` | `INSERT` | `locationsId, projectsId` | Creates a new topic. |
| `admin_projects_locations_topics_delete` | `DELETE` | `locationsId, projectsId, topicsId` | Deletes the specified topic. |
| `_admin_projects_locations_reservations_topics_list` | `EXEC` | `locationsId, projectsId, reservationsId` | Lists the topics attached to the specified reservation. |
| `_admin_projects_locations_topics_list` | `EXEC` | `locationsId, projectsId` | Returns the list of topics for the given project. |
| `admin_projects_locations_topics_patch` | `EXEC` | `locationsId, projectsId, topicsId` | Updates properties of the specified topic. |
| `topic_stats_projects_locations_topics_compute_head_cursor` | `EXEC` | `locationsId, projectsId, topicsId` | Compute the head cursor for the partition. The head cursor's offset is guaranteed to be less than or equal to all messages which have not yet been acknowledged as published, and greater than the offset of any message whose publish has already been acknowledged. It is zero if there have never been messages in the partition. |
| `topic_stats_projects_locations_topics_compute_message_stats` | `EXEC` | `locationsId, projectsId, topicsId` | Compute statistics about a range of messages in a given topic and partition. |
| `topic_stats_projects_locations_topics_compute_time_cursor` | `EXEC` | `locationsId, projectsId, topicsId` | Compute the corresponding cursor for a publish or event time in a topic partition. |
