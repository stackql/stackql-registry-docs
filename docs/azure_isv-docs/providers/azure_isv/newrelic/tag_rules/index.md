---
title: tag_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - tag_rules
  - newrelic
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
<tr><td><b>Id</b></td><td><code>azure_isv.newrelic.tag_rules</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `monitorName, resourceGroupName, ruleSetName, subscriptionId` | Get a TagRule |
| `list_by_new_relic_monitor_resource` | `SELECT` | `monitorName, resourceGroupName, subscriptionId` | List TagRule resources by NewRelicMonitorResource |
| `create_or_update` | `INSERT` | `monitorName, resourceGroupName, ruleSetName, subscriptionId, data__properties` | Create a TagRule |
| `delete` | `DELETE` | `monitorName, resourceGroupName, ruleSetName, subscriptionId` | Delete a TagRule |
| `_list_by_new_relic_monitor_resource` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` | List TagRule resources by NewRelicMonitorResource |
| `update` | `EXEC` | `monitorName, resourceGroupName, ruleSetName, subscriptionId` | Update a TagRule |
