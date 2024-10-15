---
title: sql_container_partition_merges
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_container_partition_merges
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

Creates, updates, deletes, gets or lists a <code>sql_container_partition_merges</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_container_partition_merges</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.sql_container_partition_merges" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="physicalPartitionStorageInfoCollection" /> | `array` | List of physical partitions and their properties. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, containerName, databaseName, resourceGroupName, subscriptionId" /> | Merges the partitions of a SQL Container |

## `SELECT` examples

Merges the partitions of a SQL Container


```sql
SELECT
physicalPartitionStorageInfoCollection
FROM azure.cosmos_db.sql_container_partition_merges
WHERE accountName = '{{ accountName }}'
AND containerName = '{{ containerName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```