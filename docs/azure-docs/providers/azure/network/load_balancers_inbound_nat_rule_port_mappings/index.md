---
title: load_balancers_inbound_nat_rule_port_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancers_inbound_nat_rule_port_mappings
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
<tr><td><b>Name</b></td><td><code>load_balancers_inbound_nat_rule_port_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.load_balancers_inbound_nat_rule_port_mappings</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `backendPoolName, groupName, loadBalancerName, subscriptionId` |
