---
title: cluster_principal_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_principal_assignments
  - data_explorer
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
<tr><td><b>Name</b></td><td><code>cluster_principal_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_explorer.cluster_principal_assignments" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, principalAssignmentName, resourceGroupName, subscriptionId" /> | Gets a Kusto cluster principalAssignment. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Lists all Kusto cluster principalAssignments. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, principalAssignmentName, resourceGroupName, subscriptionId" /> | Create a Kusto cluster principalAssignment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, principalAssignmentName, resourceGroupName, subscriptionId" /> | Deletes a Kusto cluster principalAssignment. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, data__name, data__type" /> | Checks that the principal assignment name is valid and is not already in use. |
