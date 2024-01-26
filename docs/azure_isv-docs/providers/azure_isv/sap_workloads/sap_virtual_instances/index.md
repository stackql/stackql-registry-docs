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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sap_virtual_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.sap_workloads.sap_virtual_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | A pre-created user assigned identity with appropriate roles assigned. To learn more on identity and roles required, visit the ACSS how-to-guide. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Defines the Virtual Instance for SAP solutions resource properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, sapVirtualInstanceName, subscriptionId` | Gets a Virtual Instance for SAP solutions resource |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all Virtual Instances for SAP solutions resources in a Resource Group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Gets all Virtual Instances for SAP solutions resources in a Subscription. |
| `create` | `INSERT` | `resourceGroupName, sapVirtualInstanceName, subscriptionId, data__properties` | Creates a Virtual Instance for SAP solutions (VIS) resource |
| `delete` | `DELETE` | `resourceGroupName, sapVirtualInstanceName, subscriptionId` | Deletes a Virtual Instance for SAP solutions resource and its child resources, that is the associated Central Services Instance, Application Server Instances and Database Instance. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets all Virtual Instances for SAP solutions resources in a Resource Group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Gets all Virtual Instances for SAP solutions resources in a Subscription. |
| `start` | `EXEC` | `resourceGroupName, sapVirtualInstanceName, subscriptionId` | Starts the SAP application, that is the Central Services instance and Application server instances. |
| `stop` | `EXEC` | `resourceGroupName, sapVirtualInstanceName, subscriptionId` | Stops the SAP Application, that is the Application server instances and Central Services instance. |
| `update` | `EXEC` | `resourceGroupName, sapVirtualInstanceName, subscriptionId` | Updates a Virtual Instance for SAP solutions resource |
