---
title: virtual_machine_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_instances
  - azure_stack_hci
  - azure_stack    
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.virtual_machine_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="properties" /> | `object` | Properties under the virtual machine instance resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceUri" /> | Gets a virtual machine instance |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceUri" /> | Lists all of the virtual machine instances within the specified parent resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceUri" /> | The operation to create or update a virtual machine instance. Please note some properties can be set only during virtual machine instance creation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceUri" /> | The operation to delete a virtual machine instance. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="resourceUri" /> | The operation to restart a virtual machine instance. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="resourceUri" /> | The operation to start a virtual machine instance. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="resourceUri" /> | The operation to stop a virtual machine instance. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceUri" /> | The operation to update a virtual machine instance. |
