---
title: dsc_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - dsc_configuration
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
<tr><td><b>Name</b></td><td><code>dsc_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.automation.dsc_configuration</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Gets or sets the etag of the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Definition of the configuration property type. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `automationAccountName, configurationName, resourceGroupName, subscriptionId` | Retrieve the configuration identified by configuration name. |
| `list_by_automation_account` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of configurations. |
| `create_or_update` | `INSERT` | `automationAccountName, configurationName, resourceGroupName, subscriptionId, data__properties` | Create the configuration identified by configuration name. |
| `delete` | `DELETE` | `automationAccountName, configurationName, resourceGroupName, subscriptionId` | Delete the dsc configuration identified by configuration name. |
| `_list_by_automation_account` | `EXEC` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of configurations. |
| `update` | `EXEC` | `automationAccountName, configurationName, resourceGroupName, subscriptionId` | Create the configuration identified by configuration name. |
