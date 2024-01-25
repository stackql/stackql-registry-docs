---
title: python2_package
hide_title: false
hide_table_of_contents: false
keywords:
  - python2_package
  - automation
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
<tr><td><b>Name</b></td><td><code>python2_package</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.automation.python2_package</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Gets the etag of the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Definition of the module property type. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `automationAccountName, packageName, resourceGroupName, subscriptionId` | Retrieve the python 2 package identified by package name. |
| `list_by_automation_account` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of python 2 packages. |
| `create_or_update` | `INSERT` | `automationAccountName, packageName, resourceGroupName, subscriptionId, data__properties` | Create or Update the python 2 package identified by package name. |
| `delete` | `DELETE` | `automationAccountName, packageName, resourceGroupName, subscriptionId` | Delete the python 2 package by name. |
| `_list_by_automation_account` | `EXEC` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of python 2 packages. |
| `update` | `EXEC` | `automationAccountName, packageName, resourceGroupName, subscriptionId` | Update the python 2 package identified by package name. |
