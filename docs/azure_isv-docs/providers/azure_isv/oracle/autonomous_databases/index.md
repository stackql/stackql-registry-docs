---
title: autonomous_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - autonomous_databases
  - oracle
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>autonomous_databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle.autonomous_databases" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Autonomous Database base resource model. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="autonomousdatabasename, resourceGroupName, subscriptionId" /> | Get a AutonomousDatabase |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List AutonomousDatabase resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List AutonomousDatabase resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="autonomousdatabasename, resourceGroupName, subscriptionId" /> | Create a AutonomousDatabase |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="autonomousdatabasename, resourceGroupName, subscriptionId" /> | Delete a AutonomousDatabase |
| <CopyableCode code="failover" /> | `EXEC` | <CopyableCode code="autonomousdatabasename, resourceGroupName, subscriptionId" /> | Perform failover action on Autonomous Database |
| <CopyableCode code="generate_wallet" /> | `EXEC` | <CopyableCode code="autonomousdatabasename, resourceGroupName, subscriptionId, data__password" /> | Generate wallet action on Autonomous Database |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="autonomousdatabasename, resourceGroupName, subscriptionId, data__timestamp" /> | Restores an Autonomous Database based on the provided request parameters. |
| <CopyableCode code="shrink" /> | `EXEC` | <CopyableCode code="autonomousdatabasename, resourceGroupName, subscriptionId" /> | This operation shrinks the current allocated storage down to the current actual used data storage. |
| <CopyableCode code="switchover" /> | `EXEC` | <CopyableCode code="autonomousdatabasename, resourceGroupName, subscriptionId" /> | Perform switchover action on Autonomous Database |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="autonomousdatabasename, resourceGroupName, subscriptionId" /> | Update a AutonomousDatabase |
