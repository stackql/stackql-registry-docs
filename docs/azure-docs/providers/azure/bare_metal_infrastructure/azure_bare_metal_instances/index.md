---
title: azure_bare_metal_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_bare_metal_instances
  - bare_metal_infrastructure
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
<tr><td><b>Name</b></td><td><code>azure_bare_metal_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.bare_metal_infrastructure.azure_bare_metal_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Describes the properties of an Azure Bare Metal Instance. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="azureBareMetalInstanceName, resourceGroupName, subscriptionId" /> | Gets an Azure Bare Metal Instance for the specified subscription, resource group, and instance name. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of Azure Bare Metal Instances in the specified subscription and resource group. The operations returns various properties of each Azure Bare Metal Instance. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns a list of Azure Bare Metal Instances in the specified subscription. The operations returns various properties of each Azure Bare Metal Instance. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of Azure Bare Metal Instances in the specified subscription and resource group. The operations returns various properties of each Azure Bare Metal Instance. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Returns a list of Azure Bare Metal Instances in the specified subscription. The operations returns various properties of each Azure Bare Metal Instance. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="azureBareMetalInstanceName, resourceGroupName, subscriptionId" /> | The operation to restart an Azure Bare Metal Instance |
| <CopyableCode code="shutdown" /> | `EXEC` | <CopyableCode code="azureBareMetalInstanceName, resourceGroupName, subscriptionId" /> | The operation to shutdown an Azure Bare Metal Instance |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="azureBareMetalInstanceName, resourceGroupName, subscriptionId" /> | The operation to start an Azure Bare Metal instance |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="azureBareMetalInstanceName, resourceGroupName, subscriptionId" /> | Patches the Tags field of a Azure Bare Metal Instance for the specified subscription, resource group, and instance name. |
