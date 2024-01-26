---
title: tag_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - tag_rules
  - dynatrace
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
<tr><td><b>Name</b></td><td><code>tag_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.dynatrace.tag_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties for the Tag rules resource of a Monitor account. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `monitorName, resourceGroupName, ruleSetName, subscriptionId` |
| `list` | `SELECT` | `monitorName, resourceGroupName, subscriptionId` |
| `create_or_update` | `INSERT` | `monitorName, resourceGroupName, ruleSetName, subscriptionId, data__properties` |
| `delete` | `DELETE` | `monitorName, resourceGroupName, ruleSetName, subscriptionId` |
| `_list` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
