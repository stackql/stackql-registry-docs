---
title: namespaces_authorization_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces_authorization_rule
  - relay
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
<tr><td><b>Id</b></td><td><code>azure.relay.namespaces_authorization_rule</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `` | Properties supplied to create or update AuthorizationRule |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId` | Authorization rule for a namespace by name. |
| `create_or_update` | `INSERT` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId` | Creates or updates an authorization rule for a namespace. |
| `delete` | `DELETE` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId` | Deletes a namespace authorization rule. |
