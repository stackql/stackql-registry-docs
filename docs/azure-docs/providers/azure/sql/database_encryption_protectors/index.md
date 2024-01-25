---
title: database_encryption_protectors
hide_title: false
hide_table_of_contents: false
keywords:
  - database_encryption_protectors
  - sql
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
<tr><td><b>Name</b></td><td><code>database_encryption_protectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.database_encryption_protectors</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `revalidate` | `EXEC` | `databaseName, encryptionProtectorName, resourceGroupName, serverName, subscriptionId` | Revalidates an existing encryption protector for a particular database. |
| `revert` | `EXEC` | `databaseName, encryptionProtectorName, resourceGroupName, serverName, subscriptionId` | Reverts an existing encryption protector for a particular database. |
