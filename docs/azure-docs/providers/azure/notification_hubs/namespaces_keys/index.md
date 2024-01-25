---
title: namespaces_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces_keys
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
<tr><td><b>Name</b></td><td><code>namespaces_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.notification_hubs.namespaces_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `keyName` | `string` | Gets or sets keyName of the created AuthorizationRule |
| `primaryConnectionString` | `string` | Gets or sets primaryConnectionString of the AuthorizationRule. |
| `primaryKey` | `string` | Gets or sets primaryKey of the created AuthorizationRule. |
| `secondaryConnectionString` | `string` | Gets or sets secondaryConnectionString of the created<br />AuthorizationRule |
| `secondaryKey` | `string` | Gets or sets secondaryKey of the created AuthorizationRule |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId` |
