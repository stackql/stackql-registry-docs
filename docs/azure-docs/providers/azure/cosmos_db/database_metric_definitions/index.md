---
title: database_metric_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - database_metric_definitions
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

Creates, updates, deletes, gets or lists a <code>database_metric_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>database_metric_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.database_metric_definitions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `object` | A metric name. |
| <CopyableCode code="metricAvailabilities" /> | `array` | The list of metric availabilities for the account. |
| <CopyableCode code="primaryAggregationType" /> | `string` | The primary aggregation type of the metric. |
| <CopyableCode code="resourceUri" /> | `string` | The resource uri of the database. |
| <CopyableCode code="unit" /> | `string` | The unit of the metric. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, databaseRid, resourceGroupName, subscriptionId" /> | Retrieves metric definitions for the given database. |

## `SELECT` examples

Retrieves metric definitions for the given database.


```sql
SELECT
name,
metricAvailabilities,
primaryAggregationType,
resourceUri,
unit
FROM azure.cosmos_db.database_metric_definitions
WHERE accountName = '{{ accountName }}'
AND databaseRid = '{{ databaseRid }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```