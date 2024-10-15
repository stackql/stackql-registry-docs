---
title: databases_metric_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - databases_metric_definitions
  - sql
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

Creates, updates, deletes, gets or lists a <code>databases_metric_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>databases_metric_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.databases_metric_definitions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `object` | A database metric name. |
| <CopyableCode code="metricAvailabilities" /> | `array` | The list of database metric availabilities for the metric. |
| <CopyableCode code="primaryAggregationType" /> | `string` | The primary aggregation type defining how metric values are displayed. |
| <CopyableCode code="resourceUri" /> | `string` | The resource uri of the database. |
| <CopyableCode code="unit" /> | `string` | The unit of the metric. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | Returns database metric definitions. |

## `SELECT` examples

Returns database metric definitions.


```sql
SELECT
name,
metricAvailabilities,
primaryAggregationType,
resourceUri,
unit
FROM azure.sql.databases_metric_definitions
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```