---
title: gateway_certificate_authority
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway_certificate_authority
  - api_management
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
<tr><td><b>Name</b></td><td><code>gateway_certificate_authority</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.gateway_certificate_authority</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Gateway certificate authority details. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `GatewayCertificateAuthority_Get` | `SELECT` | `certificateId, gatewayId, resourceGroupName, serviceName, subscriptionId` | Get assigned Gateway Certificate Authority details. |
| `GatewayCertificateAuthority_ListByService` | `SELECT` | `gatewayId, resourceGroupName, serviceName, subscriptionId` | Lists the collection of Certificate Authorities for the specified Gateway entity. |
| `GatewayCertificateAuthority_CreateOrUpdate` | `INSERT` | `certificateId, gatewayId, resourceGroupName, serviceName, subscriptionId` | Assign Certificate entity to Gateway entity as Certificate Authority. |
| `GatewayCertificateAuthority_Delete` | `DELETE` | `If-Match, certificateId, gatewayId, resourceGroupName, serviceName, subscriptionId` | Remove relationship between Certificate Authority and Gateway entity. |
| `GatewayCertificateAuthority_GetEntityTag` | `EXEC` | `certificateId, gatewayId, resourceGroupName, serviceName, subscriptionId` | Checks if Certificate entity is assigned to Gateway entity as Certificate Authority. |
