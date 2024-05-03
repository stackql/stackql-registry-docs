---
title: configuration_profile_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_profile_assignments
  - automanage
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
<tr><td><b>Name</b></td><td><code>configuration_profile_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automanage.configuration_profile_assignments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="managedBy" /> | `string` | Azure resource id. Indicates if this resource is managed by another Azure resource. |
| <CopyableCode code="properties" /> | `object` | Automanage configuration profile assignment properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configurationProfileAssignmentName, resourceGroupName, subscriptionId, vmName" /> | Get information about a configuration profile assignment |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get list of configuration profile assignments |
| <CopyableCode code="list_by_cluster_name" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Get list of configuration profile assignments |
| <CopyableCode code="list_by_machine_name" /> | `SELECT` | <CopyableCode code="machineName, resourceGroupName, subscriptionId" /> | Get list of configuration profile assignments |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get list of configuration profile assignments under a given subscription |
| <CopyableCode code="list_by_virtual_machines" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | Get list of configuration profile assignments |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="configurationProfileAssignmentName, resourceGroupName, subscriptionId, vmName" /> | Creates an association between a VM and Automanage configuration profile |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configurationProfileAssignmentName, resourceGroupName, subscriptionId, vmName" /> | Delete a configuration profile assignment |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get list of configuration profile assignments |
| <CopyableCode code="_list_by_cluster_name" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Get list of configuration profile assignments |
| <CopyableCode code="_list_by_machine_name" /> | `EXEC` | <CopyableCode code="machineName, resourceGroupName, subscriptionId" /> | Get list of configuration profile assignments |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Get list of configuration profile assignments under a given subscription |
| <CopyableCode code="_list_by_virtual_machines" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | Get list of configuration profile assignments |
