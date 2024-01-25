---
title: namespaces_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces_keys
  - event_hubs
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
<tr><td><b>Id</b></td><td><code>azure.event_hubs.namespaces_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `aliasPrimaryConnectionString` | `string` | Primary connection string of the alias if GEO DR is enabled |
| `aliasSecondaryConnectionString` | `string` | Secondary  connection string of the alias if GEO DR is enabled |
| `keyName` | `string` | A string that describes the AuthorizationRule. |
| `primaryConnectionString` | `string` | Primary connection string of the created namespace AuthorizationRule. |
| `primaryKey` | `string` | A base64-encoded 256-bit primary key for signing and validating the SAS token. |
| `secondaryConnectionString` | `string` | Secondary connection string of the created namespace AuthorizationRule. |
| `secondaryKey` | `string` | A base64-encoded 256-bit primary key for signing and validating the SAS token. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId` |
