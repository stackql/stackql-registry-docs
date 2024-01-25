---
title: data_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - data_versions
  - ml_services
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
<tr><td><b>Name</b></td><td><code>data_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ml_services.data_versions</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `name, resourceGroupName, subscriptionId, version, workspaceName` |
| `list` | `SELECT` | `name, resourceGroupName, subscriptionId, workspaceName` |
| `create_or_update` | `INSERT` | `name, resourceGroupName, subscriptionId, version, workspaceName, data__properties` |
| `delete` | `DELETE` | `name, resourceGroupName, subscriptionId, version, workspaceName` |
| `_list` | `EXEC` | `name, resourceGroupName, subscriptionId, workspaceName` |
