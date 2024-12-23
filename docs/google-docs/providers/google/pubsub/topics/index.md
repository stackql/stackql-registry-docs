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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>topics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.pubsub.topics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The name of the topic. It must have the format `"projects/{project}/topics/{topic}"`. `{topic}` must start with a letter, and contain only letters (`[A-Za-z]`), numbers (`[0-9]`), dashes (`-`), underscores (`_`), periods (`.`), tildes (`~`), plus (`+`) or percent signs (`%`). It must be between 3 and 255 characters in length, and it must not start with `"goog"`. |
| <CopyableCode code="ingestionDataSourceSettings" /> | `object` | Settings for an ingestion data source on a topic. |
| <CopyableCode code="kmsKeyName" /> | `string` | Optional. The resource name of the Cloud KMS CryptoKey to be used to protect access to messages published on this topic. The expected format is `projects/*/locations/*/keyRings/*/cryptoKeys/*`. |
| <CopyableCode code="labels" /> | `object` | Optional. See [Creating and managing labels] (https://cloud.google.com/pubsub/docs/labels). |
| <CopyableCode code="messageRetentionDuration" /> | `string` | Optional. Indicates the minimum duration to retain a message after it is published to the topic. If this field is set, messages published to the topic in the last `message_retention_duration` are always available to subscribers. For instance, it allows any attached subscription to [seek to a timestamp](https://cloud.google.com/pubsub/docs/replay-overview#seek_to_a_time) that is up to `message_retention_duration` in the past. If this field is not set, message retention is controlled by settings on individual subscriptions. Cannot be more than 31 days or less than 10 minutes. |
| <CopyableCode code="messageStoragePolicy" /> | `object` | A policy constraining the storage of messages published to the topic. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Optional. Reserved for future use. This field is set only in responses from the server; it is ignored if it is set in any requests. |
| <CopyableCode code="schemaSettings" /> | `object` | Settings for validating messages published against a schema. |
| <CopyableCode code="state" /> | `string` | Output only. An output-only field indicating the state of the topic. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_topics_get" /> | `SELECT` | <CopyableCode code="projectsId, topicsId" /> | Gets the configuration of a topic. |
| <CopyableCode code="projects_topics_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists matching topics. |
| <CopyableCode code="projects_topics_delete" /> | `DELETE` | <CopyableCode code="projectsId, topicsId" /> | Deletes the topic with the given name. Returns `NOT_FOUND` if the topic does not exist. After a topic is deleted, a new topic may be created with the same name; this is an entirely new topic with none of the old configuration or subscriptions. Existing subscriptions to this topic are not deleted, but their `topic` field is set to `_deleted-topic_`. |
| <CopyableCode code="projects_topics_patch" /> | `UPDATE` | <CopyableCode code="projectsId, topicsId" /> | Updates an existing topic by updating the fields specified in the update mask. Note that certain properties of a topic are not modifiable. |
| <CopyableCode code="projects_topics_create" /> | `EXEC` | <CopyableCode code="projectsId, topicsId" /> | Creates the given topic with the given name. See the [resource name rules] (https://cloud.google.com/pubsub/docs/pubsub-basics#resource_names). |
| <CopyableCode code="projects_topics_publish" /> | `EXEC` | <CopyableCode code="projectsId, topicsId" /> | Adds one or more messages to the topic. Returns `NOT_FOUND` if the topic does not exist. |

## `SELECT` examples

Lists matching topics.

```sql
SELECT
name,
ingestionDataSourceSettings,
kmsKeyName,
labels,
messageRetentionDuration,
messageStoragePolicy,
satisfiesPzs,
schemaSettings,
state
FROM google.pubsub.topics
WHERE projectsId = '{{ projectsId }}';
```

## `UPDATE` example

Updates a <code>topics</code> resource.

```sql
/*+ update */
UPDATE google.pubsub.topics
SET 
topic = '{{ topic }}',
updateMask = '{{ updateMask }}'
WHERE 
projectsId = '{{ projectsId }}'
AND topicsId = '{{ topicsId }}';
```

## `DELETE` example

Deletes the specified <code>topics</code> resource.

```sql
/*+ delete */
DELETE FROM google.pubsub.topics
WHERE projectsId = '{{ projectsId }}'
AND topicsId = '{{ topicsId }}';
```
