---
title: managed_restorable_dropped_database_backup_short_term_retention_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_restorable_dropped_database_backup_short_term_retention_policies
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
<tr><td><b>Name</b></td><td><code>managed_restorable_dropped_database_backup_short_term_retention_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_restorable_dropped_database_backup_short_term_retention_policies" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managedInstanceName, policyName, resourceGroupName, restorableDroppedDatabaseId, subscriptionId" /> | Gets a dropped database's short term retention policy. |
| <CopyableCode code="list_by_restorable_dropped_database" /> | `SELECT` | <CopyableCode code="managedInstanceName, resourceGroupName, restorableDroppedDatabaseId, subscriptionId" /> | Gets a dropped database's short term retention policy list. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="managedInstanceName, policyName, resourceGroupName, restorableDroppedDatabaseId, subscriptionId" /> | Sets a database's short term retention policy. |
| <CopyableCode code="_list_by_restorable_dropped_database" /> | `EXEC` | <CopyableCode code="managedInstanceName, resourceGroupName, restorableDroppedDatabaseId, subscriptionId" /> | Gets a dropped database's short term retention policy list. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="managedInstanceName, policyName, resourceGroupName, restorableDroppedDatabaseId, subscriptionId" /> | Sets a database's short term retention policy. |
