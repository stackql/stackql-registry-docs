---
title: service_endpoint_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - service_endpoint_policies
  - network
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
<tr><td><b>Name</b></td><td><code>service_endpoint_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.service_endpoint_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `kind` | `string` | Kind of service endpoint policy. This is metadata used for the Azure portal experience. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Service Endpoint Policy resource. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServiceEndpointPolicies_Get` | `SELECT` | `resourceGroupName, serviceEndpointPolicyName, subscriptionId` | Gets the specified service Endpoint Policies in a specified resource group. |
| `ServiceEndpointPolicies_List` | `SELECT` | `subscriptionId` | Gets all the service endpoint policies in a subscription. |
| `ServiceEndpointPolicies_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all service endpoint Policies in a resource group. |
| `ServiceEndpointPolicies_CreateOrUpdate` | `INSERT` | `resourceGroupName, serviceEndpointPolicyName, subscriptionId` | Creates or updates a service Endpoint Policies. |
| `ServiceEndpointPolicies_Delete` | `DELETE` | `resourceGroupName, serviceEndpointPolicyName, subscriptionId` | Deletes the specified service endpoint policy. |
| `ServiceEndpointPolicies_UpdateTags` | `EXEC` | `resourceGroupName, serviceEndpointPolicyName, subscriptionId` | Updates tags of a service endpoint policy. |
