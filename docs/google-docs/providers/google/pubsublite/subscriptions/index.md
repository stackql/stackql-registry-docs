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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.pubsublite.subscriptions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="admin_projects_locations_subscriptions_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, subscriptionsId" /> | Returns the subscription configuration. |
| <CopyableCode code="admin_projects_locations_subscriptions_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Returns the list of subscriptions for the given project. |
| <CopyableCode code="admin_projects_locations_topics_subscriptions_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, topicsId" /> | Lists the subscriptions attached to the specified topic. |
| <CopyableCode code="admin_projects_locations_subscriptions_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new subscription. |
| <CopyableCode code="admin_projects_locations_subscriptions_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, subscriptionsId" /> | Deletes the specified subscription. |
| <CopyableCode code="admin_projects_locations_subscriptions_patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, subscriptionsId" /> | Updates properties of the specified subscription. |
| <CopyableCode code="admin_projects_locations_subscriptions_seek" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, subscriptionsId" /> | Performs an out-of-band seek for a subscription to a specified target, which may be timestamps or named positions within the message backlog. Seek translates these targets to cursors for each partition and orchestrates subscribers to start consuming messages from these seek cursors. If an operation is returned, the seek has been registered and subscribers will eventually receive messages from the seek cursors (i.e. eventual consistency), as long as they are using a minimum supported client library version and not a system that tracks cursors independently of Pub/Sub Lite (e.g. Apache Beam, Dataflow, Spark). The seek operation will fail for unsupported clients. If clients would like to know when subscribers react to the seek (or not), they can poll the operation. The seek operation will succeed and complete once subscribers are ready to receive messages from the seek cursors for all partitions of the topic. This means that the seek operation will not complete until all subscribers come online. If the previous seek operation has not yet completed, it will be aborted and the new invocation of seek will supersede it. |
| <CopyableCode code="cursor_projects_locations_subscriptions_commit_cursor" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, subscriptionsId" /> | Updates the committed cursor. |

## `SELECT` examples

Returns the list of subscriptions for the given project.

```sql
SELECT
column_anon
FROM google.pubsublite.subscriptions
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>subscriptions</code> resource.

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
INSERT INTO google.pubsublite.subscriptions (
locationsId,
projectsId,
name,
topic,
deliveryConfig,
exportConfig
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ topic }}',
'{{ deliveryConfig }}',
'{{ exportConfig }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: topic
      value: string
    - name: deliveryConfig
      value:
        - name: deliveryRequirement
          value: string
    - name: exportConfig
      value:
        - name: desiredState
          value: string
        - name: currentState
          value: string
        - name: deadLetterTopic
          value: string
        - name: pubsubConfig
          value:
            - name: topic
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>subscriptions</code> resource.

```sql
/*+ update */
UPDATE google.pubsublite.subscriptions
SET 
name = '{{ name }}',
topic = '{{ topic }}',
deliveryConfig = '{{ deliveryConfig }}',
exportConfig = '{{ exportConfig }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND subscriptionsId = '{{ subscriptionsId }}';
```

## `DELETE` example

Deletes the specified <code>subscriptions</code> resource.

```sql
/*+ delete */
DELETE FROM google.pubsublite.subscriptions
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND subscriptionsId = '{{ subscriptionsId }}';
```
