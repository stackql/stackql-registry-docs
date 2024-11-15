---
title: topics
hide_title: false
hide_table_of_contents: false
keywords:
  - topics
  - databases
  - digitalocean
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage digitalocean resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>topics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.databases.topics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="databases_get_kafka_topic" /> | `SELECT` | <CopyableCode code="database_cluster_uuid, topic_name" /> | To retrieve a given topic by name from the set of a Kafka cluster's topics, send a GET request to `/v2/databases/$DATABASE_ID/topics/$TOPIC_NAME`. The result will be a JSON object with a `topic` key. |
| <CopyableCode code="databases_list_kafka_topics" /> | `SELECT` | <CopyableCode code="database_cluster_uuid" /> | To list all of a Kafka cluster's topics, send a GET request to `/v2/databases/$DATABASE_ID/topics`. The result will be a JSON object with a `topics` key. |
| <CopyableCode code="databases_create_kafka_topic" /> | `INSERT` | <CopyableCode code="database_cluster_uuid" /> | To create a topic attached to a Kafka cluster, send a POST request to `/v2/databases/$DATABASE_ID/topics`. The result will be a JSON object with a `topic` key. |
| <CopyableCode code="databases_delete_kafka_topic" /> | `DELETE` | <CopyableCode code="database_cluster_uuid, topic_name" /> | To delete a single topic within a Kafka cluster, send a DELETE request to `/v2/databases/$DATABASE_ID/topics/$TOPIC_NAME`. A status of 204 will be given. This indicates that the request was processed successfully, but that no response body is needed. |
| <CopyableCode code="databases_update_kafka_topic" /> | `EXEC` | <CopyableCode code="database_cluster_uuid, topic_name" /> | To update a topic attached to a Kafka cluster, send a PUT request to `/v2/databases/$DATABASE_ID/topics/$TOPIC_NAME`. The result will be a JSON object with a `topic` key. |

## `SELECT` examples

To list all of a Kafka cluster's topics, send a GET request to `/v2/databases/$DATABASE_ID/topics`. The result will be a JSON object with a `topics` key.


```sql
SELECT
column_anon
FROM digitalocean.databases.topics
WHERE database_cluster_uuid = '{{ database_cluster_uuid }}';
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
INSERT INTO digitalocean.databases.topics (
database_cluster_uuid
)
SELECT 
'{{ database_cluster_uuid }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: topics
  props:
    - name: database_cluster_uuid
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>topics</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.databases.topics
WHERE database_cluster_uuid = '{{ database_cluster_uuid }}'
AND topic_name = '{{ topic_name }}';
```
