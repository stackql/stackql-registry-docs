---
title: global_rulestack
hide_title: false
hide_table_of_contents: false
keywords:
  - global_rulestack
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
<tr><td><b>Name</b></td><td><code>global_rulestack</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.paloaltonetworks.global_rulestack</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | The properties of the managed service identities assigned to this resource. |
| `location` | `string` | Global Location |
| `properties` | `object` | PAN Rulestack Describe Object |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `globalRulestackName` | Get a GlobalRulestackResource |
| `list` | `SELECT` |  | List GlobalRulestackResource resources by Tenant |
| `create_or_update` | `INSERT` | `globalRulestackName, data__location, data__properties` | Create a GlobalRulestackResource |
| `delete` | `DELETE` | `globalRulestackName` | Delete a GlobalRulestackResource |
| `_list` | `EXEC` |  | List GlobalRulestackResource resources by Tenant |
| `commit` | `EXEC` | `globalRulestackName` | Commit rulestack configuration |
| `revert` | `EXEC` | `globalRulestackName` | Revert rulestack configuration |
| `update` | `EXEC` | `globalRulestackName` | Update a GlobalRulestackResource |
