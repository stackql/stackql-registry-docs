---
title: azure_dev_ops_project
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_dev_ops_project
  - security_devops
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
<tr><td><b>Name</b></td><td><code>azure_dev_ops_project</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_devops.azure_dev_ops_project</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `azureDevOpsConnectorName, azureDevOpsOrgName, azureDevOpsProjectName, resourceGroupName, subscriptionId` |
| `list` | `SELECT` | `azureDevOpsConnectorName, azureDevOpsOrgName, resourceGroupName, subscriptionId` |
| `create_or_update` | `INSERT` | `azureDevOpsConnectorName, azureDevOpsOrgName, azureDevOpsProjectName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `azureDevOpsConnectorName, azureDevOpsOrgName, resourceGroupName, subscriptionId` |
| `update` | `EXEC` | `azureDevOpsConnectorName, azureDevOpsOrgName, azureDevOpsProjectName, resourceGroupName, subscriptionId` |
