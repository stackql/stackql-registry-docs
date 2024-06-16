---
title: managed_database_columns
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_database_columns
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
<tr><td><b>Name</b></td><td><code>managed_database_columns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_database_columns" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="columnName, databaseName, managedInstanceName, resourceGroupName, schemaName, subscriptionId, tableName" /> | Get managed database column |
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="databaseName, managedInstanceName, resourceGroupName, subscriptionId" /> | List managed database columns |
| <CopyableCode code="list_by_table" /> | `SELECT` | <CopyableCode code="databaseName, managedInstanceName, resourceGroupName, schemaName, subscriptionId, tableName" /> | List managed database columns |
