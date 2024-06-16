---
title: long_term_retention_managed_instance_backups
hide_title: false
hide_table_of_contents: false
keywords:
  - long_term_retention_managed_instance_backups
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
<tr><td><b>Name</b></td><td><code>long_term_retention_managed_instance_backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.long_term_retention_managed_instance_backups" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupName, databaseName, locationName, managedInstanceName, subscriptionId" /> | Gets a long term retention backup for a managed database. |
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="databaseName, locationName, managedInstanceName, subscriptionId" /> | Lists all long term retention backups for a managed database. |
| <CopyableCode code="list_by_instance" /> | `SELECT` | <CopyableCode code="locationName, managedInstanceName, subscriptionId" /> | Lists the long term retention backups for a given managed instance. |
| <CopyableCode code="list_by_location" /> | `SELECT` | <CopyableCode code="locationName, subscriptionId" /> | Lists the long term retention backups for managed databases in a given location. |
| <CopyableCode code="list_by_resource_group_database" /> | `SELECT` | <CopyableCode code="databaseName, locationName, managedInstanceName, resourceGroupName, subscriptionId" /> | Lists all long term retention backups for a managed database. |
| <CopyableCode code="list_by_resource_group_instance" /> | `SELECT` | <CopyableCode code="locationName, managedInstanceName, resourceGroupName, subscriptionId" /> | Lists the long term retention backups for a given managed instance. |
| <CopyableCode code="list_by_resource_group_location" /> | `SELECT` | <CopyableCode code="locationName, resourceGroupName, subscriptionId" /> | Lists the long term retention backups for managed databases in a given location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backupName, databaseName, locationName, managedInstanceName, subscriptionId" /> | Deletes a long term retention backup. |
| <CopyableCode code="delete_by_resource_group" /> | `DELETE` | <CopyableCode code="backupName, databaseName, locationName, managedInstanceName, resourceGroupName, subscriptionId" /> | Deletes a long term retention backup. |
| <CopyableCode code="get_by_resource_group" /> | `EXEC` | <CopyableCode code="backupName, databaseName, locationName, managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a long term retention backup for a managed database. |
