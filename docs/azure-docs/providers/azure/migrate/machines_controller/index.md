---
title: machines_controller
hide_title: false
hide_table_of_contents: false
keywords:
  - machines_controller
  - migrate
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
<tr><td><b>Name</b></td><td><code>machines_controller</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.machines_controller" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="machineName, resourceGroupName, siteName, subscriptionId" /> | Get a MachineResource |
| <CopyableCode code="list_by_vmware_site" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | List MachineResource resources by VmwareSite |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="machineName, resourceGroupName, siteName, subscriptionId" /> | Method to start a machine. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="machineName, resourceGroupName, siteName, subscriptionId" /> | Method to stop a machine. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="machineName, resourceGroupName, siteName, subscriptionId" /> | Update a MachineResource |
