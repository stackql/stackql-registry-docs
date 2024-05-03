---
title: sql_pool_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_schemas
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
<tr><td><b>Name</b></td><td><code>sql_pool_schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pool_schemas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="nextLink" /> | `string` | Link to retrieve next page of results. |
| <CopyableCode code="value" /> | `array` | Array of results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Gets schemas of a given SQL pool. |
| <CopyableCode code="exec_get" /> | `EXEC` | <CopyableCode code="resourceGroupName, schemaName, sqlPoolName, subscriptionId, workspaceName" /> | Get Sql Pool schema |
