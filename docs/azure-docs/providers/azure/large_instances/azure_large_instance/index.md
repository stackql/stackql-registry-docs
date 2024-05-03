---
title: azure_large_instance
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_large_instance
  - large_instances
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
<tr><td><b>Name</b></td><td><code>azure_large_instance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.large_instances.azure_large_instance" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Describes the properties of an Azure Large Instance. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="azureLargeInstanceName, resourceGroupName, subscriptionId" /> | Gets an Azure Large Instance for the specified subscription, resource group,<br />and instance name. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of Azure Large Instances in the specified subscription and resource<br />group. The operations returns various properties of each Azure Large Instance. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of Azure Large Instances in the specified subscription. The<br />operations returns various properties of each Azure Large Instance. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of Azure Large Instances in the specified subscription and resource<br />group. The operations returns various properties of each Azure Large Instance. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Gets a list of Azure Large Instances in the specified subscription. The<br />operations returns various properties of each Azure Large Instance. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="azureLargeInstanceName, resourceGroupName, subscriptionId" /> | The operation to restart an Azure Large Instance (only for compute instances) |
| <CopyableCode code="shutdown" /> | `EXEC` | <CopyableCode code="azureLargeInstanceName, resourceGroupName, subscriptionId" /> | The operation to shutdown an Azure Large Instance (only for compute instances) |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="azureLargeInstanceName, resourceGroupName, subscriptionId" /> | The operation to start an Azure Large Instance (only for compute instances) |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="azureLargeInstanceName, resourceGroupName, subscriptionId" /> | Patches the Tags field of an Azure Large Instance for the specified<br />subscription, resource group, and instance name. |
