---
title: sap_application_server_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - sap_application_server_instances
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
<tr><td><b>Name</b></td><td><code>sap_application_server_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.sap_workloads.sap_application_server_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Defines the SAP Application Server instance properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `applicationInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId` | Gets the SAP Application Server Instance corresponding to the Virtual Instance for SAP solutions resource. |
| `list` | `SELECT` | `resourceGroupName, sapVirtualInstanceName, subscriptionId` | Lists the SAP Application Server Instance resources for a given Virtual Instance for SAP solutions resource. |
| `create` | `INSERT` | `applicationInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId` | Puts the SAP Application Server Instance resource. &lt;br&gt;&lt;br&gt;This will be used by service only. PUT by end user will return a Bad Request error. |
| `delete` | `DELETE` | `applicationInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId` | Deletes the SAP Application Server Instance resource. &lt;br&gt;&lt;br&gt;This operation will be used by service only. Delete by end user will return a Bad Request error. |
| `_list` | `EXEC` | `resourceGroupName, sapVirtualInstanceName, subscriptionId` | Lists the SAP Application Server Instance resources for a given Virtual Instance for SAP solutions resource. |
| `start_instance` | `EXEC` | `applicationInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId` | Starts the SAP Application Server Instance. |
| `stop_instance` | `EXEC` | `applicationInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId` | Stops the SAP Application Server Instance. |
| `update` | `EXEC` | `applicationInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId` | Puts the SAP Application Server Instance resource. |
