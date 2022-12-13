---
title: user_identities
hide_title: false
hide_table_of_contents: false
keywords:
  - user_identities
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
<tr><td><b>Name</b></td><td><code>user_identities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.user_identities</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Identifier value within provider. |
| `provider` | `string` | Identity provider name. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `UserIdentities_List` | `SELECT` | `resourceGroupName, serviceName, subscriptionId, userId` |
