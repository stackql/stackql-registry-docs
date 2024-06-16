---
title: virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines
  - lab_services
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
<tr><td><b>Name</b></td><td><code>virtual_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.lab_services.virtual_machines" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Virtual machine resource properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` |  | Returns the properties for a lab virtual machine. |
| <CopyableCode code="list_by_lab" /> | `SELECT` |  | Returns a list of all virtual machines for a lab. |
| <CopyableCode code="redeploy" /> | `EXEC` |  | Action to redeploy a lab virtual machine to a different compute node. For troubleshooting connectivity. |
| <CopyableCode code="reimage" /> | `EXEC` |  | Re-image a lab virtual machine. The virtual machine will be deleted and recreated using the latest published snapshot of the reference environment of the lab. |
| <CopyableCode code="reset_password" /> | `EXEC` | <CopyableCode code="data__password, data__username" /> | Resets a lab virtual machine password. |
| <CopyableCode code="start" /> | `EXEC` |  | Action to start a lab virtual machine. |
| <CopyableCode code="stop" /> | `EXEC` |  | Action to stop a lab virtual machine. |
