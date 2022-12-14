---
title: tag_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - tag_rules
  - logz
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
<tr><td><b>Name</b></td><td><code>tag_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.logz.tag_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The id of the rule set. |
| `name` | `string` | Name of the rule set. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the rule set. |
| `properties` | `object` | Definition of the properties for a TagRules resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `TagRules_Get` | `SELECT` | `monitorName, resourceGroupName, ruleSetName, subscriptionId` |
| `TagRules_List` | `SELECT` | `monitorName, resourceGroupName, subscriptionId` |
| `TagRules_CreateOrUpdate` | `INSERT` | `monitorName, resourceGroupName, ruleSetName, subscriptionId` |
| `TagRules_Delete` | `DELETE` | `monitorName, resourceGroupName, ruleSetName, subscriptionId` |
