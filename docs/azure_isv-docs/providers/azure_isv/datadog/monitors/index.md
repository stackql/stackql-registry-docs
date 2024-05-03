---
title: monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors
  - datadog
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
<tr><td><b>Name</b></td><td><code>monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.datadog.monitors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ARM id of the monitor resource. |
| <CopyableCode code="name" /> | `string` | Name of the monitor resource. |
| <CopyableCode code="identity" /> | `object` |  |
| <CopyableCode code="location" /> | `string` |  |
| <CopyableCode code="properties" /> | `object` | Properties specific to the monitor resource. |
| <CopyableCode code="sku" /> | `object` |  |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | The type of the monitor resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId, data__location" /> |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> |
| <CopyableCode code="refresh_set_password_link" /> | `EXEC` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="set_default_key" /> | `EXEC` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId, data__key" /> |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |
