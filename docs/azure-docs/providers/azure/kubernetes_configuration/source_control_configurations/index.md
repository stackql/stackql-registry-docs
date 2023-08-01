---
title: source_control_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - source_control_configurations
  - kubernetes_configuration
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
<tr><td><b>Name</b></td><td><code>source_control_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.kubernetes_configuration.source_control_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties to create a Source Control Configuration resource |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SourceControlConfigurations_Get` | `SELECT` | `clusterName, clusterResourceName, clusterRp, resourceGroupName, sourceControlConfigurationName, subscriptionId` | Gets details of the Source Control Configuration. |
| `SourceControlConfigurations_List` | `SELECT` | `clusterName, clusterResourceName, clusterRp, resourceGroupName, subscriptionId` | List all Source Control Configurations. |
| `SourceControlConfigurations_CreateOrUpdate` | `INSERT` | `clusterName, clusterResourceName, clusterRp, resourceGroupName, sourceControlConfigurationName, subscriptionId` | Create a new Kubernetes Source Control Configuration. |
| `SourceControlConfigurations_Delete` | `DELETE` | `clusterName, clusterResourceName, clusterRp, resourceGroupName, sourceControlConfigurationName, subscriptionId` | This will delete the YAML file used to set up the Source control configuration, thus stopping future sync from the source repo. |
