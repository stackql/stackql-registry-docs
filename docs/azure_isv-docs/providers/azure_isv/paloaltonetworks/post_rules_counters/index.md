---
title: post_rules_counters
hide_title: false
hide_table_of_contents: false
keywords:
  - post_rules_counters
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
<tr><td><b>Name</b></td><td><code>post_rules_counters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.paloaltonetworks.post_rules_counters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `appSeen` | `object` | Data Type for App Seen |
| `firewallName` | `string` | firewall name |
| `hitCount` | `integer` | hit count |
| `lastUpdatedTimestamp` | `string` | last updated timestamp |
| `priority` | `string` | priority number |
| `requestTimestamp` | `string` | timestamp of request |
| `ruleListName` | `string` | rule list name |
| `ruleName` | `string` | rule name |
| `ruleStackName` | `string` | rule Stack Name |
| `timestamp` | `string` | timestamp of response |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `globalRulestackName, priority` |
