---
title: restorable_database_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - restorable_database_accounts
  - cosmos_db
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
<tr><td><b>Name</b></td><td><code>restorable_database_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.restorable_database_accounts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique resource identifier of the ARM resource. |
| <CopyableCode code="name" /> | `string` | The name of the ARM resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource group to which the resource belongs. |
| <CopyableCode code="properties" /> | `object` | The properties of a restorable database account. |
| <CopyableCode code="type" /> | `string` | The type of Azure resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the restorable Azure Cosmos DB database accounts available under the subscription. This call requires 'Microsoft.DocumentDB/locations/restorableDatabaseAccounts/read' permission. |
| <CopyableCode code="list_by_location" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Lists all the restorable Azure Cosmos DB database accounts available under the subscription and in a region.  This call requires 'Microsoft.DocumentDB/locations/restorableDatabaseAccounts/read' permission. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Lists all the restorable Azure Cosmos DB database accounts available under the subscription. This call requires 'Microsoft.DocumentDB/locations/restorableDatabaseAccounts/read' permission. |
| <CopyableCode code="_list_by_location" /> | `EXEC` | <CopyableCode code="location, subscriptionId" /> | Lists all the restorable Azure Cosmos DB database accounts available under the subscription and in a region.  This call requires 'Microsoft.DocumentDB/locations/restorableDatabaseAccounts/read' permission. |
| <CopyableCode code="get_by_location" /> | `EXEC` | <CopyableCode code="instanceId, location, subscriptionId" /> | Retrieves the properties of an existing Azure Cosmos DB restorable database account.  This call requires 'Microsoft.DocumentDB/locations/restorableDatabaseAccounts/read/*' permission. |
