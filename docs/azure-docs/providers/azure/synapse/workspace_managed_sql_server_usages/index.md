---
title: workspace_managed_sql_server_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_managed_sql_server_usages
  - synapse
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
<tr><td><b>Name</b></td><td><code>workspace_managed_sql_server_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.workspace_managed_sql_server_usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the server usage metric. |
| <CopyableCode code="currentValue" /> | `number` | The current value of the metric. |
| <CopyableCode code="displayName" /> | `string` | The metric display name. |
| <CopyableCode code="limit" /> | `number` | The current limit of the metric. |
| <CopyableCode code="nextResetTime" /> | `string` | The next reset time for the metric (ISO8601 format). |
| <CopyableCode code="resourceName" /> | `string` | The name of the resource. |
| <CopyableCode code="unit" /> | `string` | The units of the metric. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |
