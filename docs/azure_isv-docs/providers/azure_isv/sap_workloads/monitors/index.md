---
title: monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors
  - sap_workloads
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.sap_workloads.monitors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | A pre-created user assigned identity with appropriate roles assigned. To learn more on identity and roles required, visit the ACSS how-to-guide. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a SAP monitor. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> | Gets properties of a SAP monitor for the specified subscription, resource group, and resource name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of SAP monitors in the specified subscription. The operations returns various properties of each SAP monitor. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of SAP monitors in the specified resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> | Creates a SAP monitor for the specified subscription, resource group, and resource name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> | Deletes a SAP monitor with the specified subscription, resource group, and SAP monitor name. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Gets a list of SAP monitors in the specified subscription. The operations returns various properties of each SAP monitor. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of SAP monitors in the specified resource group. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> | Patches the Tags field of a SAP monitor for the specified subscription, resource group, and SAP monitor name. |
