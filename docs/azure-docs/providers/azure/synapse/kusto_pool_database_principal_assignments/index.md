---
title: kusto_pool_database_principal_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - kusto_pool_database_principal_assignments
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
<tr><td><b>Name</b></td><td><code>kusto_pool_database_principal_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.kusto_pool_database_principal_assignments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | A class representing database principal property. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, kustoPoolName, principalAssignmentName, resourceGroupName, subscriptionId, workspaceName" /> | Gets a Kusto pool database principalAssignment. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Lists all Kusto pool database principalAssignments. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="databaseName, kustoPoolName, principalAssignmentName, resourceGroupName, subscriptionId, workspaceName" /> | Creates a Kusto pool database principalAssignment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="databaseName, kustoPoolName, principalAssignmentName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes a Kusto pool principalAssignment. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Lists all Kusto pool database principalAssignments. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName, data__name, data__type" /> | Checks that the database principal assignment is valid and is not already in use. |
