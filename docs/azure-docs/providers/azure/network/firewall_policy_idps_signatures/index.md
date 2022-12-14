---
title: firewall_policy_idps_signatures
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_policy_idps_signatures
  - network
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
<tr><td><b>Name</b></td><td><code>firewall_policy_idps_signatures</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.firewall_policy_idps_signatures</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `matchingRecordsCount` | `integer` | Number of total records matching the query. |
| `signatures` | `array` | Array containing the results of the query |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `FirewallPolicyIdpsSignatures_List` | `SELECT` | `firewallPolicyName, resourceGroupName, subscriptionId` |
