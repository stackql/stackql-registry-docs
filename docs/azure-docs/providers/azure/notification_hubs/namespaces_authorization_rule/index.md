---
title: namespaces_authorization_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces_authorization_rule
  - notification_hubs
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
<tr><td><b>Name</b></td><td><code>namespaces_authorization_rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.notification_hubs.namespaces_authorization_rule</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | Deprecated - only for compatibility. |
| `properties` | `object` | SharedAccessAuthorizationRule properties. |
| `tags` | `object` | Deprecated - only for compatibility. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId` |
| `create_or_update` | `INSERT` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId` |
| `delete` | `DELETE` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId` |
