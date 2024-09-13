
---
title: topics_partitions
hide_title: false
hide_table_of_contents: false
keywords:
  - topics_partitions
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

Creates, updates, deletes or gets an <code>topics_partition</code> resource or lists <code>topics_partitions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topics_partitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.pubsublite.topics_partitions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="partitionCount" /> | `string` | The number of partitions in the topic. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="admin_projects_locations_topics_get_partitions" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, topicsId" /> | Returns the partition information for the requested topic. |

## `SELECT` examples

Returns the partition information for the requested topic.

```sql
SELECT
partitionCount
FROM google.pubsublite.topics_partitions
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND topicsId = '{{ topicsId }}'; 
```
