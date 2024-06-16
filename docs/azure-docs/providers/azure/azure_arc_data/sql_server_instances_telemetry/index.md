---
title: sql_server_instances_telemetry
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_server_instances_telemetry
  - azure_arc_data
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_server_instances_telemetry</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azure_arc_data.sql_server_instances_telemetry" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="columns" /> | `array` | The columns of the result telemetry table for the SQL Server instance. |
| <CopyableCode code="nextLink" /> | `string` | The link to the next section of rows of the telemetry response for the SQL Server instance. Null if no more sections are available. |
| <CopyableCode code="rows" /> | `array` | A list of rows from the result telemetry table for the SQL Server instance. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, sqlServerInstanceName, subscriptionId, data__datasetName" /> |
