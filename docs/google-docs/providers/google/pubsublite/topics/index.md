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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>topics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.pubsublite.topics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the topic. Structured like: projects/{project_number}/locations/{location}/topics/{topic_id} |
| <CopyableCode code="partitionConfig" /> | `object` | The settings for a topic's partitions. |
| <CopyableCode code="reservationConfig" /> | `object` | The settings for this topic's Reservation usage. |
| <CopyableCode code="retentionConfig" /> | `object` | The settings for a topic's message retention. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="admin_projects_locations_reservations_topics_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, reservationsId" /> | Lists the topics attached to the specified reservation. |
| <CopyableCode code="admin_projects_locations_topics_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, topicsId" /> | Returns the topic configuration. |
| <CopyableCode code="admin_projects_locations_topics_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Returns the list of topics for the given project. |
| <CopyableCode code="admin_projects_locations_topics_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new topic. |
| <CopyableCode code="admin_projects_locations_topics_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, topicsId" /> | Deletes the specified topic. |
| <CopyableCode code="admin_projects_locations_topics_patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, topicsId" /> | Updates properties of the specified topic. |
| <CopyableCode code="topic_stats_projects_locations_topics_compute_head_cursor" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, topicsId" /> | Compute the head cursor for the partition. The head cursor's offset is guaranteed to be less than or equal to all messages which have not yet been acknowledged as published, and greater than the offset of any message whose publish has already been acknowledged. It is zero if there have never been messages in the partition. |
| <CopyableCode code="topic_stats_projects_locations_topics_compute_message_stats" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, topicsId" /> | Compute statistics about a range of messages in a given topic and partition. |
| <CopyableCode code="topic_stats_projects_locations_topics_compute_time_cursor" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, topicsId" /> | Compute the corresponding cursor for a publish or event time in a topic partition. |

## `SELECT` examples

Returns the list of topics for the given project.

```sql
SELECT
name,
partitionConfig,
reservationConfig,
retentionConfig
FROM google.pubsublite.topics
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>topics</code> resource.

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
INSERT INTO google.pubsublite.topics (
locationsId,
projectsId,
name,
partitionConfig,
retentionConfig,
reservationConfig
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ partitionConfig }}',
'{{ retentionConfig }}',
'{{ reservationConfig }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
partitionConfig:
  count: string
  scale: integer
  capacity:
    publishMibPerSec: integer
    subscribeMibPerSec: integer
retentionConfig:
  perPartitionBytes: string
  period: string
reservationConfig:
  throughputReservation: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>topics</code> resource.

```sql
/*+ update */
UPDATE google.pubsublite.topics
SET 
name = '{{ name }}',
partitionConfig = '{{ partitionConfig }}',
retentionConfig = '{{ retentionConfig }}',
reservationConfig = '{{ reservationConfig }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND topicsId = '{{ topicsId }}';
```

## `DELETE` example

Deletes the specified <code>topics</code> resource.

```sql
/*+ delete */
DELETE FROM google.pubsublite.topics
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND topicsId = '{{ topicsId }}';
```
