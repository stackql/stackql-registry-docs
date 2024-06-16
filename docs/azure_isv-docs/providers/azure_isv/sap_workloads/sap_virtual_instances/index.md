---
title: sap_virtual_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - sap_virtual_instances
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
<tr><td><b>Name</b></td><td><code>sap_virtual_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.sap_workloads.sap_virtual_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | A pre-created user assigned identity with appropriate roles assigned. To learn more on identity and roles required, visit the ACSS how-to-guide. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Defines the Virtual Instance for SAP solutions resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Gets a Virtual Instance for SAP solutions resource |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all Virtual Instances for SAP solutions resources in a Resource Group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all Virtual Instances for SAP solutions resources in a Subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, sapVirtualInstanceName, subscriptionId, data__properties" /> | Creates a Virtual Instance for SAP solutions (VIS) resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Deletes a Virtual Instance for SAP solutions resource and its child resources, that is the associated Central Services Instance, Application Server Instances and Database Instance. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Starts the SAP application, that is the Central Services instance and Application server instances. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Stops the SAP Application, that is the Application server instances and Central Services instance. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Updates a Virtual Instance for SAP solutions resource |
