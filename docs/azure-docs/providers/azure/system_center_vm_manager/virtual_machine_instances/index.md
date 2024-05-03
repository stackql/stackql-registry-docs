---
title: virtual_machine_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_instances
  - system_center_vm_manager
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
<tr><td><b>Name</b></td><td><code>virtual_machine_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.system_center_vm_manager.virtual_machine_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The extended location. |
| <CopyableCode code="properties" /> | `object` | Defines the resource properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceUri" /> | Retrieves information about a virtual machine instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceUri, data__extendedLocation, data__properties" /> | The operation to create or update a virtual machine instance. Please note some properties can be set only during virtual machine instance creation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceUri" /> | The operation to delete a virtual machine instance. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="resourceUri" /> | The operation to restart a virtual machine instance. |
| <CopyableCode code="restore_checkpoint" /> | `EXEC` | <CopyableCode code="resourceUri" /> | Restores to a checkpoint in virtual machine instance. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="resourceUri" /> | The operation to start a virtual machine instance. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="resourceUri" /> | The operation to power off (stop) a virtual machine instance. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceUri" /> | The operation to update a virtual machine instance. |
