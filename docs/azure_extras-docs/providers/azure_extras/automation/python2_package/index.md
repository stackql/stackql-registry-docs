---
title: python2_package
hide_title: false
hide_table_of_contents: false
keywords:
  - python2_package
  - automation
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
<tr><td><b>Name</b></td><td><code>python2_package</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automation.python2_package</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Definition of the module property type. |
| `tags` | `object` | Resource tags. |
| `etag` | `string` | Gets or sets the etag of the resource. |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Python2Package_Get` | `SELECT` | `automationAccountName, packageName, resourceGroupName, subscriptionId` | Retrieve the python 2 package identified by package name. |
| `Python2Package_ListByAutomationAccount` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of python 2 packages. |
| `Python2Package_CreateOrUpdate` | `INSERT` | `automationAccountName, packageName, resourceGroupName, subscriptionId, data__properties` | Create or Update the python 2 package identified by package name. |
| `Python2Package_Delete` | `DELETE` | `automationAccountName, packageName, resourceGroupName, subscriptionId` | Delete the python 2 package by name. |
| `Python2Package_Update` | `EXEC` | `automationAccountName, packageName, resourceGroupName, subscriptionId` | Update the python 2 package identified by package name. |
