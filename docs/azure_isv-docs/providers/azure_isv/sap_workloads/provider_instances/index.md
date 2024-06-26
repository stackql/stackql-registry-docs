---
title: provider_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_instances
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
<tr><td><b>Name</b></td><td><code>provider_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.sap_workloads.provider_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | A pre-created user assigned identity with appropriate roles assigned. To learn more on identity and roles required, visit the ACSS how-to-guide. |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a provider instance. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="monitorName, providerInstanceName, resourceGroupName, subscriptionId" /> | Gets properties of a provider instance for the specified subscription, resource group, SAP monitor name, and resource name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> | Gets a list of provider instances in the specified SAP monitor. The operations returns various properties of each provider instances. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="monitorName, providerInstanceName, resourceGroupName, subscriptionId" /> | Creates a provider instance for the specified subscription, resource group, SAP monitor name, and resource name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="monitorName, providerInstanceName, resourceGroupName, subscriptionId" /> | Deletes a provider instance for the specified subscription, resource group, SAP monitor name, and resource name. |
