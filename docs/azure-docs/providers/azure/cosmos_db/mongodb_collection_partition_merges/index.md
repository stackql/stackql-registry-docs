---
title: mongodb_collection_partition_merges
hide_title: false
hide_table_of_contents: false
keywords:
  - mongodb_collection_partition_merges
  - cosmos_db
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

Creates, updates, deletes, gets or lists a <code>mongodb_collection_partition_merges</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mongodb_collection_partition_merges</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.mongodb_collection_partition_merges" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="physicalPartitionStorageInfoCollection" /> | `array` | List of physical partitions and their properties. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, collectionName, databaseName, resourceGroupName, subscriptionId" /> | Merges the partitions of a MongoDB Collection |

## `SELECT` examples

Merges the partitions of a MongoDB Collection


```sql
SELECT
physicalPartitionStorageInfoCollection
FROM azure.cosmos_db.mongodb_collection_partition_merges
WHERE accountName = '{{ accountName }}'
AND collectionName = '{{ collectionName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```