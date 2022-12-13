---
title: information_protection_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - information_protection_policies
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
<tr><td><b>Name</b></td><td><code>information_protection_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.information_protection_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | describes properties of an information protection policy. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `InformationProtectionPolicies_Get` | `SELECT` | `api-version, informationProtectionPolicyName, scope` | Details of the information protection policy. |
| `InformationProtectionPolicies_List` | `SELECT` | `api-version, scope` | Information protection policies of a specific management group. |
| `InformationProtectionPolicies_CreateOrUpdate` | `INSERT` | `api-version, informationProtectionPolicyName, scope` | Details of the information protection policy. |
