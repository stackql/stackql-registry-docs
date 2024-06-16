---
title: managed_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_databases
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
<tr><td><b>Name</b></td><td><code>managed_databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_databases" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The managed database's properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a managed database. |
| <CopyableCode code="list_by_instance" /> | `SELECT` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a list of managed databases. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="databaseName, managedInstanceName, resourceGroupName, subscriptionId, data__location" /> | Creates a new database or updates an existing database. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="databaseName, managedInstanceName, resourceGroupName, subscriptionId" /> | Deletes a managed database. |
| <CopyableCode code="cancel_move" /> | `EXEC` | <CopyableCode code="databaseName, managedInstanceName, resourceGroupName, subscriptionId, data__destinationManagedDatabaseId" /> | Cancels a managed database move operation. |
| <CopyableCode code="complete_move" /> | `EXEC` | <CopyableCode code="databaseName, managedInstanceName, resourceGroupName, subscriptionId, data__destinationManagedDatabaseId" /> | Completes a managed database move operation. |
| <CopyableCode code="complete_restore" /> | `EXEC` | <CopyableCode code="databaseName, managedInstanceName, resourceGroupName, subscriptionId, data__lastBackupName" /> | Completes the restore operation on a managed database. |
| <CopyableCode code="start_move" /> | `EXEC` | <CopyableCode code="databaseName, managedInstanceName, resourceGroupName, subscriptionId, data__destinationManagedDatabaseId" /> | Starts a managed database move operation. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="databaseName, managedInstanceName, resourceGroupName, subscriptionId" /> | Updates an existing database. |
