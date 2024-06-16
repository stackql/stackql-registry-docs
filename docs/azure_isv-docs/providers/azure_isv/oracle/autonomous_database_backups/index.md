---
title: autonomous_database_backups
hide_title: false
hide_table_of_contents: false
keywords:
  - autonomous_database_backups
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
<tr><td><b>Name</b></td><td><code>autonomous_database_backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle.autonomous_database_backups" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="adbbackupid, autonomousdatabasename, resourceGroupName, subscriptionId" /> | Get a AutonomousDatabaseBackup |
| <CopyableCode code="list_by_autonomous_database" /> | `SELECT` | <CopyableCode code="autonomousdatabasename, resourceGroupName, subscriptionId" /> | List AutonomousDatabaseBackup resources by AutonomousDatabase |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="adbbackupid, autonomousdatabasename, resourceGroupName, subscriptionId" /> | Create a AutonomousDatabaseBackup |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="adbbackupid, autonomousdatabasename, resourceGroupName, subscriptionId" /> | Delete a AutonomousDatabaseBackup |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="adbbackupid, autonomousdatabasename, resourceGroupName, subscriptionId" /> | Update a AutonomousDatabaseBackup |
