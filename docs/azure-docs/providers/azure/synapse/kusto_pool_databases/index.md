---
title: kusto_pool_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - kusto_pool_databases
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
<tr><td><b>Name</b></td><td><code>kusto_pool_databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.kusto_pool_databases" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Kind of the database |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Returns a database. |
| <CopyableCode code="list_by_kusto_pool" /> | `SELECT` | <CopyableCode code="kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Returns the list of databases of the given Kusto pool. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName, data__kind" /> | Creates or updates a database. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes the database with the given name. |
| <CopyableCode code="_list_by_kusto_pool" /> | `EXEC` | <CopyableCode code="kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Returns the list of databases of the given Kusto pool. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName, data__kind" /> | Updates a database. |
