---
title: hcrp_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - hcrp_assignments
  - guest_configuration
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
<tr><td><b>Name</b></td><td><code>hcrp_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.guest_configuration.hcrp_assignments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Guest configuration assignment properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="guestConfigurationAssignmentName, machineName, resourceGroupName, subscriptionId" /> | Get information about a guest configuration assignment |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="machineName, resourceGroupName, subscriptionId" /> | List all guest configuration assignments for an ARC machine. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="guestConfigurationAssignmentName, machineName, resourceGroupName, subscriptionId" /> | Creates an association between a ARC machine and guest configuration |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="guestConfigurationAssignmentName, machineName, resourceGroupName, subscriptionId" /> | Delete a guest configuration assignment |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="machineName, resourceGroupName, subscriptionId" /> | List all guest configuration assignments for an ARC machine. |
