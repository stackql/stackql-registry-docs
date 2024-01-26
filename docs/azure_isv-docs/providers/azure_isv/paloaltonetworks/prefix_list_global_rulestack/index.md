---
title: prefix_list_global_rulestack
hide_title: false
hide_table_of_contents: false
keywords:
  - prefix_list_global_rulestack
  - paloaltonetworks
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>prefix_list_global_rulestack</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.paloaltonetworks.prefix_list_global_rulestack</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | prefix entry |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `globalRulestackName, name` | Get a PrefixListGlobalRulestackResource |
| `list` | `SELECT` | `globalRulestackName` | List PrefixListGlobalRulestackResource resources by Tenant |
| `create_or_update` | `INSERT` | `globalRulestackName, name, data__properties` | Create a PrefixListGlobalRulestackResource |
| `delete` | `DELETE` | `globalRulestackName, name` | Delete a PrefixListGlobalRulestackResource |
| `_list` | `EXEC` | `globalRulestackName` | List PrefixListGlobalRulestackResource resources by Tenant |
