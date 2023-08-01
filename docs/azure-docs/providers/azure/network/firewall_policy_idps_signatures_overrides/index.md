---
title: firewall_policy_idps_signatures_overrides
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_policy_idps_signatures_overrides
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
<tr><td><b>Name</b></td><td><code>firewall_policy_idps_signatures_overrides</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.firewall_policy_idps_signatures_overrides</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Will contain the resource id of the signature override resource |
| `name` | `string` | Contains the name of the resource (default) |
| `properties` | `object` | Will contain the properties of the resource (the actual signature overrides) |
| `type` | `string` | Will contain the type of the resource: Microsoft.Network/firewallPolicies/intrusionDetectionSignaturesOverrides |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `FirewallPolicyIdpsSignaturesOverrides_List` | `SELECT` | `firewallPolicyName, resourceGroupName, subscriptionId` | Returns all signatures overrides objects for a specific policy as a list containing a single value. |
| `FirewallPolicyIdpsSignaturesOverrides_Get` | `EXEC` | `firewallPolicyName, resourceGroupName, subscriptionId` | Returns all signatures overrides for a specific policy. |
| `FirewallPolicyIdpsSignaturesOverrides_Patch` | `EXEC` | `firewallPolicyName, resourceGroupName, subscriptionId` | Will update the status of policy's signature overrides for IDPS |
| `FirewallPolicyIdpsSignaturesOverrides_Put` | `EXEC` | `firewallPolicyName, resourceGroupName, subscriptionId` | Will override/create a new signature overrides for the policy's IDPS |
