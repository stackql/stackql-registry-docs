---
title: long_term_retention_backups
hide_title: false
hide_table_of_contents: false
keywords:
  - long_term_retention_backups
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
<tr><td><b>Name</b></td><td><code>long_term_retention_backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.long_term_retention_backups" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, subscriptionId" /> | Gets a long term retention backup. |
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="locationName, longTermRetentionDatabaseName, longTermRetentionServerName, subscriptionId" /> | Lists all long term retention backups for a database. |
| <CopyableCode code="list_by_location" /> | `SELECT` | <CopyableCode code="locationName, subscriptionId" /> | Lists the long term retention backups for a given location. |
| <CopyableCode code="list_by_resource_group_database" /> | `SELECT` | <CopyableCode code="locationName, longTermRetentionDatabaseName, longTermRetentionServerName, resourceGroupName, subscriptionId" /> | Lists all long term retention backups for a database based on a particular resource group. |
| <CopyableCode code="list_by_resource_group_location" /> | `SELECT` | <CopyableCode code="locationName, resourceGroupName, subscriptionId" /> | Lists the long term retention backups for a given location based on resource group. |
| <CopyableCode code="list_by_resource_group_server" /> | `SELECT` | <CopyableCode code="locationName, longTermRetentionServerName, resourceGroupName, subscriptionId" /> | Lists the long term retention backups for a given server based on resource groups. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="locationName, longTermRetentionServerName, subscriptionId" /> | Lists the long term retention backups for a given server. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, subscriptionId" /> | Deletes a long term retention backup. |
| <CopyableCode code="delete_by_resource_group" /> | `DELETE` | <CopyableCode code="backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, resourceGroupName, subscriptionId" /> | Deletes a long term retention backup. |
| <CopyableCode code="change_access_tier" /> | `EXEC` | <CopyableCode code="backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, subscriptionId, data__backupStorageAccessTier, data__operationMode" /> | Change a long term retention backup access tier. |
| <CopyableCode code="change_access_tier_by_resource_group" /> | `EXEC` | <CopyableCode code="backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, resourceGroupName, subscriptionId, data__backupStorageAccessTier, data__operationMode" /> | Change a long term retention backup access tier. |
| <CopyableCode code="copy" /> | `EXEC` | <CopyableCode code="backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, subscriptionId" /> | Copy an existing long term retention backup. |
| <CopyableCode code="copy_by_resource_group" /> | `EXEC` | <CopyableCode code="backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, resourceGroupName, subscriptionId" /> | Copy an existing long term retention backup to a different server. |
| <CopyableCode code="get_by_resource_group" /> | `EXEC` | <CopyableCode code="backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, resourceGroupName, subscriptionId" /> | Gets a long term retention backup. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, subscriptionId" /> | Updates an existing long term retention backup. |
| <CopyableCode code="update_by_resource_group" /> | `EXEC` | <CopyableCode code="backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, resourceGroupName, subscriptionId" /> | Updates an existing long term retention backup. |
