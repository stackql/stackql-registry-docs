---
title: sap_virtual_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - sap_virtual_instances
  - workloads
  - azure_extras    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sap_virtual_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.workloads.sap_virtual_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `identity` | `object` | Managed service identity (user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Defines the Virtual Instance for SAP solutions resource properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SAPVirtualInstances_Get` | `SELECT` | `resourceGroupName, sapVirtualInstanceName, subscriptionId` | Gets a Virtual Instance for SAP solutions resource |
| `SAPVirtualInstances_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all Virtual Instances for SAP solutions resources in a Resource Group. |
| `SAPVirtualInstances_ListBySubscription` | `SELECT` | `subscriptionId` | Gets all Virtual Instances for SAP solutions resources in a Subscription. |
| `SAPVirtualInstances_Create` | `INSERT` | `resourceGroupName, sapVirtualInstanceName, subscriptionId, data__properties` | Creates a Virtual Instance for SAP solutions (VIS) resource |
| `SAPVirtualInstances_Delete` | `DELETE` | `resourceGroupName, sapVirtualInstanceName, subscriptionId` | Deletes a Virtual Instance for SAP solutions resource and its child resources, that is the associated Central Services Instance, Application Server Instances and Database Instance. |
| `SAPVirtualInstances_Start` | `EXEC` | `resourceGroupName, sapVirtualInstanceName, subscriptionId` | Starts the SAP application, that is the Central Services instance and Application server instances. |
| `SAPVirtualInstances_Stop` | `EXEC` | `resourceGroupName, sapVirtualInstanceName, subscriptionId` | Stops the SAP Application, that is the Application server instances and Central Services instance. |
| `SAPVirtualInstances_Update` | `EXEC` | `resourceGroupName, sapVirtualInstanceName, subscriptionId` | Updates a Virtual Instance for SAP solutions resource |
