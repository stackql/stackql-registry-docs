---
title: flux_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - flux_configurations
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
<tr><td><b>Name</b></td><td><code>flux_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.kubernetes_configuration.flux_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties to create a Flux Configuration resource |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `FluxConfigurations_Get` | `SELECT` | `clusterName, clusterResourceName, clusterRp, fluxConfigurationName, resourceGroupName, subscriptionId` | Gets details of the Flux Configuration. |
| `FluxConfigurations_List` | `SELECT` | `clusterName, clusterResourceName, clusterRp, resourceGroupName, subscriptionId` | List all Flux Configurations. |
| `FluxConfigurations_CreateOrUpdate` | `INSERT` | `clusterName, clusterResourceName, clusterRp, fluxConfigurationName, resourceGroupName, subscriptionId` | Create a new Kubernetes Flux Configuration. |
| `FluxConfigurations_Delete` | `DELETE` | `clusterName, clusterResourceName, clusterRp, fluxConfigurationName, resourceGroupName, subscriptionId` | This will delete the YAML file used to set up the Flux Configuration, thus stopping future sync from the source repo. |
| `FluxConfigurations_Update` | `EXEC` | `clusterName, clusterResourceName, clusterRp, fluxConfigurationName, resourceGroupName, subscriptionId` | Update an existing Kubernetes Flux Configuration. |
