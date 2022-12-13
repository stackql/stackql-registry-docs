---
title: private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_resources
  - azure_active_directory
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
<tr><td><b>Name</b></td><td><code>private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.azure_active_directory.private_link_resources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique resource identifier of the Azure AD PrivateLink Policy. |
| `name` | `string` | The name of the Azure AD PrivateLink Policy. |
| `type` | `string` | The type of Azure resource. |
| `properties` | `object` | Properties of a private link resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `PrivateLinkResources_Get` | `SELECT` | `groupName, policyName, resourceGroupName, subscriptionId` |
| `PrivateLinkResources_ListByPrivateLinkPolicy` | `SELECT` | `policyName, resourceGroupName, subscriptionId` |
