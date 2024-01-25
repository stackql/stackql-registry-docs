---
title: managed_instance_encryption_protectors
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instance_encryption_protectors
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
<tr><td><b>Name</b></td><td><code>managed_instance_encryption_protectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_instance_encryption_protectors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Kind of encryption protector. This is metadata used for the Azure portal experience. |
| `properties` | `object` | Properties for an encryption protector execution. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `encryptionProtectorName, managedInstanceName, resourceGroupName, subscriptionId` | Gets a managed instance encryption protector. |
| `list_by_instance` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets a list of managed instance encryption protectors |
| `create_or_update` | `INSERT` | `encryptionProtectorName, managedInstanceName, resourceGroupName, subscriptionId` | Updates an existing encryption protector. |
| `_list_by_instance` | `EXEC` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets a list of managed instance encryption protectors |
| `revalidate` | `EXEC` | `encryptionProtectorName, managedInstanceName, resourceGroupName, subscriptionId` | Revalidates an existing encryption protector. |
