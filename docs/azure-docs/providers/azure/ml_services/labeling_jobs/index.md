---
title: labeling_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - labeling_jobs
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
<tr><td><b>Name</b></td><td><code>labeling_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ml_services.labeling_jobs</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `id, resourceGroupName, subscriptionId, workspaceName` |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` |
| `create_or_update` | `INSERT` | `id, resourceGroupName, subscriptionId, workspaceName, data__properties` |
| `delete` | `DELETE` | `id, resourceGroupName, subscriptionId, workspaceName` |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` |
| `export_labels` | `EXEC` | `id, resourceGroupName, subscriptionId, workspaceName, data__format` |
| `pause` | `EXEC` | `id, resourceGroupName, subscriptionId, workspaceName` |
| `resume` | `EXEC` | `id, resourceGroupName, subscriptionId, workspaceName` |
