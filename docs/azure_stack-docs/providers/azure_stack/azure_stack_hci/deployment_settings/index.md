---
title: deployment_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment_settings
  - azure_stack_hci
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>deployment_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.azure_stack_hci.deployment_settings</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterName, deploymentSettingsName, resourceGroupName, subscriptionId` | Get a DeploymentSetting |
| `list_by_clusters` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | List DeploymentSetting resources by Clusters |
| `create_or_update` | `INSERT` | `clusterName, deploymentSettingsName, resourceGroupName, subscriptionId` | Create a DeploymentSetting |
| `delete` | `DELETE` | `clusterName, deploymentSettingsName, resourceGroupName, subscriptionId` | Delete a DeploymentSetting |
| `_list_by_clusters` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | List DeploymentSetting resources by Clusters |
