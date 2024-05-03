---
title: sub_account
hide_title: false
hide_table_of_contents: false
keywords:
  - sub_account
  - logz
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>sub_account</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.logz.sub_account" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ARM id of the monitor resource. |
| <CopyableCode code="name" /> | `string` | Name of the monitor resource. |
| <CopyableCode code="identity" /> | `object` |  |
| <CopyableCode code="location" /> | `string` |  |
| <CopyableCode code="properties" /> | `object` | Properties specific to the monitor resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | The type of the monitor resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subAccountName, subscriptionId" /> |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="monitorName, resourceGroupName, subAccountName, subscriptionId, data__location" /> |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="monitorName, resourceGroupName, subAccountName, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="monitorName, resourceGroupName, subAccountName, subscriptionId" /> |
| <CopyableCode code="vm_host_payload" /> | `EXEC` | <CopyableCode code="monitorName, resourceGroupName, subAccountName, subscriptionId" /> |
