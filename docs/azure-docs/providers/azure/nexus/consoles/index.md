---
title: consoles
hide_title: false
hide_table_of_contents: false
keywords:
  - consoles
  - nexus
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
<tr><td><b>Name</b></td><td><code>consoles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.nexus.consoles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` |  |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="consoleName, resourceGroupName, subscriptionId, virtualMachineName" /> | Get properties of the provided virtual machine console. |
| <CopyableCode code="list_by_virtual_machine" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineName" /> | Get a list of consoles for the provided virtual machine. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="consoleName, resourceGroupName, subscriptionId, virtualMachineName, data__extendedLocation, data__properties" /> | Create a new virtual machine console or update the properties of the existing virtual machine console. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="consoleName, resourceGroupName, subscriptionId, virtualMachineName" /> | Delete the provided virtual machine console. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="consoleName, resourceGroupName, subscriptionId, virtualMachineName" /> | Patch the properties of the provided virtual machine console, or update the tags associated with the virtual machine console. Properties and tag updates can be done independently. |
