---
title: apms
hide_title: false
hide_table_of_contents: false
keywords:
  - apms
  - spring_apps
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
<tr><td><b>Name</b></td><td><code>apms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.spring_apps.apms</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `apmName, resourceGroupName, serviceName, subscriptionId` | Get the APM by name. |
| `list` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Get collection of APMs. |
| `create_or_update` | `INSERT` | `apmName, resourceGroupName, serviceName, subscriptionId` | Create or update an APM. |
| `delete` | `DELETE` | `apmName, resourceGroupName, serviceName, subscriptionId` | Operation to delete an APM |
| `_list` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Get collection of APMs. |
