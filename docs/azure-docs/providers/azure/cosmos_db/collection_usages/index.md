---
title: collection_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - collection_usages
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

Creates, updates, deletes, gets or lists a <code>collection_usages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>collection_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.collection_usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `object` | A metric name. |
| <CopyableCode code="currentValue" /> | `integer` | Current value for this metric |
| <CopyableCode code="limit" /> | `integer` | Maximum value for this metric |
| <CopyableCode code="quotaPeriod" /> | `string` | The quota period used to summarize the usage values. |
| <CopyableCode code="unit" /> | `string` | The unit of the metric. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, collectionRid, databaseRid, resourceGroupName, subscriptionId" /> | Retrieves the usages (most recent storage data) for the given collection. |

## `SELECT` examples

Retrieves the usages (most recent storage data) for the given collection.


```sql
SELECT
name,
currentValue,
limit,
quotaPeriod,
unit
FROM azure.cosmos_db.collection_usages
WHERE accountName = '{{ accountName }}'
AND collectionRid = '{{ collectionRid }}'
AND databaseRid = '{{ databaseRid }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```