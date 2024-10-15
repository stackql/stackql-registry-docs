---
title: sql_server_instances_telemetries
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_server_instances_telemetries
  - azure_arc_data
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

Creates, updates, deletes, gets or lists a <code>sql_server_instances_telemetries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_server_instances_telemetries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azure_arc_data.sql_server_instances_telemetries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="columns" /> | `array` | The columns of the result telemetry table for the SQL Server instance. |
| <CopyableCode code="nextLink" /> | `string` | The link to the next section of rows of the telemetry response for the SQL Server instance. Null if no more sections are available. |
| <CopyableCode code="rows" /> | `array` | A list of rows from the result telemetry table for the SQL Server instance. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlServerInstanceName, subscriptionId, data__datasetName" /> | Retrieves SQL Server instance telemetry |

## `SELECT` examples

Retrieves SQL Server instance telemetry


```sql
SELECT
columns,
nextLink,
rows
FROM azure.azure_arc_data.sql_server_instances_telemetries
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlServerInstanceName = '{{ sqlServerInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__datasetName = '{{ data__datasetName }}';
```