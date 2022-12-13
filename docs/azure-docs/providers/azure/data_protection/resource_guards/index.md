---
title: resource_guards
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_guards
  - data_protection
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
<tr><td><b>Name</b></td><td><code>resource_guards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_protection.resource_guards</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id represents the complete path to the resource. |
| `name` | `string` | Resource name associated with the resource. |
| `eTag` | `string` | Optional ETag. |
| `identity` | `object` | Identity details |
| `location` | `string` | Resource location. |
| `properties` | `object` |  |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ResourceGuards_Get` | `SELECT` | `api-version, resourceGroupName, resourceGuardsName, subscriptionId` |
| `ResourceGuards_Delete` | `DELETE` | `api-version, resourceGroupName, resourceGuardsName, subscriptionId` |
| `ResourceGuards_GetBackupSecurityPINRequestsObjects` | `EXEC` | `api-version, resourceGroupName, resourceGuardsName, subscriptionId` |
| `ResourceGuards_GetDefaultBackupSecurityPINRequestsObject` | `EXEC` | `api-version, requestName, resourceGroupName, resourceGuardsName, subscriptionId` |
| `ResourceGuards_GetDefaultDeleteProtectedItemRequestsObject` | `EXEC` | `api-version, requestName, resourceGroupName, resourceGuardsName, subscriptionId` |
| `ResourceGuards_GetDefaultDeleteResourceGuardProxyRequestsObject` | `EXEC` | `api-version, requestName, resourceGroupName, resourceGuardsName, subscriptionId` |
| `ResourceGuards_GetDefaultDisableSoftDeleteRequestsObject` | `EXEC` | `api-version, requestName, resourceGroupName, resourceGuardsName, subscriptionId` |
| `ResourceGuards_GetDefaultUpdateProtectedItemRequestsObject` | `EXEC` | `api-version, requestName, resourceGroupName, resourceGuardsName, subscriptionId` |
| `ResourceGuards_GetDefaultUpdateProtectionPolicyRequestsObject` | `EXEC` | `api-version, requestName, resourceGroupName, resourceGuardsName, subscriptionId` |
| `ResourceGuards_GetDeleteProtectedItemRequestsObjects` | `EXEC` | `api-version, resourceGroupName, resourceGuardsName, subscriptionId` |
| `ResourceGuards_GetDeleteResourceGuardProxyRequestsObjects` | `EXEC` | `api-version, resourceGroupName, resourceGuardsName, subscriptionId` |
| `ResourceGuards_GetDisableSoftDeleteRequestsObjects` | `EXEC` | `api-version, resourceGroupName, resourceGuardsName, subscriptionId` |
| `ResourceGuards_GetResourcesInResourceGroup` | `EXEC` | `api-version, resourceGroupName, subscriptionId` |
| `ResourceGuards_GetResourcesInSubscription` | `EXEC` | `api-version, subscriptionId` |
| `ResourceGuards_GetUpdateProtectedItemRequestsObjects` | `EXEC` | `api-version, resourceGroupName, resourceGuardsName, subscriptionId` |
| `ResourceGuards_GetUpdateProtectionPolicyRequestsObjects` | `EXEC` | `api-version, resourceGroupName, resourceGuardsName, subscriptionId` |
| `ResourceGuards_Patch` | `EXEC` | `api-version, resourceGroupName, resourceGuardsName, subscriptionId` |
| `ResourceGuards_Put` | `EXEC` | `api-version, resourceGroupName, resourceGuardsName, subscriptionId` |
