---
title: managed_instance_dtcs
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instance_dtcs
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
<tr><td><b>Name</b></td><td><code>managed_instance_dtcs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_instance_dtcs</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedInstanceDtcs_Get` | `SELECT` | `dtcName, managedInstanceName, resourceGroupName, subscriptionId` | Gets managed instance DTC settings. |
| `ManagedInstanceDtcs_ListByManagedInstance` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets a list of managed instance DTC settings. |
| `ManagedInstanceDtcs_CreateOrUpdate` | `INSERT` | `dtcName, managedInstanceName, resourceGroupName, subscriptionId` | Updates managed instance DTC settings. |
