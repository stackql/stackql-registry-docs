---
title: sub_account_tag_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - sub_account_tag_rules
  - logz
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
<tr><td><b>Name</b></td><td><code>sub_account_tag_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.logz.sub_account_tag_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The id of the rule set. |
| `name` | `string` | Name of the rule set. |
| `properties` | `object` | Definition of the properties for a TagRules resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the rule set. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `monitorName, resourceGroupName, ruleSetName, subAccountName, subscriptionId` |
| `list` | `SELECT` | `monitorName, resourceGroupName, subAccountName, subscriptionId` |
| `create_or_update` | `INSERT` | `monitorName, resourceGroupName, ruleSetName, subAccountName, subscriptionId` |
| `delete` | `DELETE` | `monitorName, resourceGroupName, ruleSetName, subAccountName, subscriptionId` |
| `_list` | `EXEC` | `monitorName, resourceGroupName, subAccountName, subscriptionId` |
