---
title: api_collections
hide_title: false
hide_table_of_contents: false
keywords:
  - api_collections
  - security
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
<tr><td><b>Name</b></td><td><code>api_collections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.api_collections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Describes the properties of an API collection. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_by_azure_api_management_service` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Gets a list of Azure API Management APIs that have been onboarded to Microsoft Defender for APIs. If an Azure API Management API is onboarded to Microsoft Defender for APIs, the system will monitor the operations within the Azure API Management API for intrusive behaviors and provide alerts for attacks that have been detected. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of API collections within a resource group that have been onboarded to Microsoft Defender for APIs. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Gets a list of API collections within a subscription that have been onboarded to Microsoft Defender for APIs. |
| `_list_by_azure_api_management_service` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Gets a list of Azure API Management APIs that have been onboarded to Microsoft Defender for APIs. If an Azure API Management API is onboarded to Microsoft Defender for APIs, the system will monitor the operations within the Azure API Management API for intrusive behaviors and provide alerts for attacks that have been detected. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets a list of API collections within a resource group that have been onboarded to Microsoft Defender for APIs. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Gets a list of API collections within a subscription that have been onboarded to Microsoft Defender for APIs. |
| `get_by_azure_api_management_service` | `EXEC` | `apiId, resourceGroupName, serviceName, subscriptionId` | Gets an Azure API Management API if it has been onboarded to Microsoft Defender for APIs. If an Azure API Management API is onboarded to Microsoft Defender for APIs, the system will monitor the operations within the Azure API Management API for intrusive behaviors and provide alerts for attacks that have been detected. |
| `offboard_azure_api_management_api` | `EXEC` | `apiId, resourceGroupName, serviceName, subscriptionId` | Offboard an Azure API Management API from Microsoft Defender for APIs. The system will stop monitoring the operations within the Azure API Management API for intrusive behaviors. |
| `onboard_azure_api_management_api` | `EXEC` | `apiId, resourceGroupName, serviceName, subscriptionId` | Onboard an Azure API Management API to Microsoft Defender for APIs. The system will start monitoring the operations within the Azure Management API for intrusive behaviors and provide alerts for attacks that have been detected. |
