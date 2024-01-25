---
title: managed_instances_outbound_network_dependencies_by_managed_instance
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instances_outbound_network_dependencies_by_managed_instance
  - sql
  - azure    
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
<tr><td><b>Name</b></td><td><code>managed_instances_outbound_network_dependencies_by_managed_instance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_instances_outbound_network_dependencies_by_managed_instance</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `category` | `string` | The type of service accessed by the managed instance service, e.g., Azure Storage, Azure Active Directory, etc. |
| `endpoints` | `array` | The endpoints that the managed instance service communicates with in order to function correctly. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `managedInstanceName, resourceGroupName, subscriptionId` |
