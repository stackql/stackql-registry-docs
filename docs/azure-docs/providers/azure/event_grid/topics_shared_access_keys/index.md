---
title: topics_shared_access_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - topics_shared_access_keys
  - event_grid
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

Creates, updates, deletes, gets or lists a <code>topics_shared_access_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topics_shared_access_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.topics_shared_access_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="key1" /> | `string` | Shared access key1 for the topic. |
| <CopyableCode code="key2" /> | `string` | Shared access key2 for the topic. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, topicName" /> | List the two keys used to publish to a topic. |

## `SELECT` examples

List the two keys used to publish to a topic.


```sql
SELECT
key1,
key2
FROM azure.event_grid.topics_shared_access_keys
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND topicName = '{{ topicName }}';
```