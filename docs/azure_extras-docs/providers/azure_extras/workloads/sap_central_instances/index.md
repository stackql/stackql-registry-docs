---
title: sap_central_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - sap_central_instances
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
<tr><td><b>Name</b></td><td><code>sap_central_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.workloads.sap_central_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Defines the SAP Central Services Instance properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SAPCentralInstances_Get` | `SELECT` | `centralInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId` | Gets the SAP Central Services Instance resource. |
| `SAPCentralInstances_List` | `SELECT` | `resourceGroupName, sapVirtualInstanceName, subscriptionId` | Lists the SAP Central Services Instance resource for the given Virtual Instance for SAP solutions resource. |
| `SAPCentralInstances_Create` | `INSERT` | `centralInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId` | Creates the SAP Central Services Instance resource. &lt;br&gt;&lt;br&gt;This will be used by service only. PUT operation on this resource by end user will return a Bad Request error. |
| `SAPCentralInstances_Delete` | `DELETE` | `centralInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId` | Deletes the SAP Central Services Instance resource. &lt;br&gt;&lt;br&gt;This will be used by service only. Delete operation on this resource by end user will return a Bad Request error. You can delete the parent resource, which is the Virtual Instance for SAP solutions resource, using the delete operation on it. |
| `SAPCentralInstances_Update` | `EXEC` | `centralInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId` | Updates the SAP Central Services Instance resource. &lt;br&gt;&lt;br&gt;This can be used to update tags on the resource. |
