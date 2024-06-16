---
title: managed_database_queries
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_database_queries
  - sql
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
<tr><td><b>Name</b></td><td><code>managed_database_queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_database_queries" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_query" /> | `SELECT` | <CopyableCode code="databaseName, managedInstanceName, queryId, resourceGroupName, subscriptionId" /> | Get query execution statistics by query id. |
| <CopyableCode code="exec_get" /> | `EXEC` | <CopyableCode code="databaseName, managedInstanceName, queryId, resourceGroupName, subscriptionId" /> | Get query by query id. |
