---
title: firewall_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_rules
  - data_lake_store
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
<tr><td><b>Name</b></td><td><code>firewall_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_lake_store.firewall_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `properties` | `object` | The firewall rule properties. |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, firewallRuleName, resourceGroupName, subscriptionId` | Gets the specified Data Lake Store firewall rule. |
| `list_by_account` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Lists the Data Lake Store firewall rules within the specified Data Lake Store account. |
| `create_or_update` | `INSERT` | `accountName, firewallRuleName, resourceGroupName, subscriptionId, data__properties` | Creates or updates the specified firewall rule. During update, the firewall rule with the specified name will be replaced with this new firewall rule. |
| `delete` | `DELETE` | `accountName, firewallRuleName, resourceGroupName, subscriptionId` | Deletes the specified firewall rule from the specified Data Lake Store account. |
| `_list_by_account` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Lists the Data Lake Store firewall rules within the specified Data Lake Store account. |
| `update` | `EXEC` | `accountName, firewallRuleName, resourceGroupName, subscriptionId` | Updates the specified firewall rule. |
