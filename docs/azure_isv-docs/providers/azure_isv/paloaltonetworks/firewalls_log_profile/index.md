---
title: firewalls_log_profile
hide_title: false
hide_table_of_contents: false
keywords:
  - firewalls_log_profile
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
<tr><td><b>Name</b></td><td><code>firewalls_log_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.paloaltonetworks.firewalls_log_profile</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `applicationInsights` | `object` | Application Insights key |
| `commonDestination` | `object` | Log Destination |
| `decryptLogDestination` | `object` | Log Destination |
| `logOption` | `string` | Log options possible |
| `logType` | `string` | Possible log types |
| `threatLogDestination` | `object` | Log Destination |
| `trafficLogDestination` | `object` | Log Destination |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `firewallName, resourceGroupName, subscriptionId` |
