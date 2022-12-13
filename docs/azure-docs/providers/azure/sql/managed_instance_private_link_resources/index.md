---
title: managed_instance_private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instance_private_link_resources
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
<tr><td><b>Name</b></td><td><code>managed_instance_private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_instance_private_link_resources</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedInstancePrivateLinkResources_Get` | `SELECT` | `groupName, managedInstanceName, resourceGroupName, subscriptionId` | Gets a private link resource for SQL server. |
| `ManagedInstancePrivateLinkResources_ListByManagedInstance` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets the private link resources for SQL server. |
