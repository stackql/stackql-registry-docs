---
title: kube_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - kube_environments
  - web_apps
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
<tr><td><b>Name</b></td><td><code>kube_environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.web_apps.kube_environments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `kind` | `string` | Kind of resource. |
| `location` | `string` | Resource Location. |
| `properties` | `object` | KubeEnvironment resource specific properties |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `extendedLocation` | `object` | Extended Location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `KubeEnvironments_Get` | `SELECT` | `name, resourceGroupName, subscriptionId` | Description for Get the properties of a Kubernetes Environment. |
| `KubeEnvironments_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Description for Get all the Kubernetes Environments in a resource group. |
| `KubeEnvironments_ListBySubscription` | `SELECT` | `subscriptionId` | Description for Get all Kubernetes Environments for a subscription. |
| `KubeEnvironments_CreateOrUpdate` | `INSERT` | `name, resourceGroupName, subscriptionId` | Description for Creates or updates a Kubernetes Environment. |
| `KubeEnvironments_Delete` | `DELETE` | `name, resourceGroupName, subscriptionId` | Description for Delete a Kubernetes Environment. |
| `KubeEnvironments_Update` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Creates or updates a Kubernetes Environment. |
