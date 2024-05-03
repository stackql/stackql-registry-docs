---
title: machine_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - machine_extensions
  - hybrid_compute
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
<tr><td><b>Name</b></td><td><code>machine_extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_compute.machine_extensions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a Machine Extension. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="extensionName, machineName, resourceGroupName, subscriptionId" /> | The operation to get the extension. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="machineName, resourceGroupName, subscriptionId" /> | The operation to get all extensions of a non-Azure machine |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="extensionName, machineName, resourceGroupName, subscriptionId" /> | The operation to create or update the extension. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="extensionName, machineName, resourceGroupName, subscriptionId" /> | The operation to delete the extension. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="machineName, resourceGroupName, subscriptionId" /> | The operation to get all extensions of a non-Azure machine |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="extensionName, machineName, resourceGroupName, subscriptionId" /> | The operation to create or update the extension. |
