---
title: region_network_firewall_policies_effective_firewalls
hide_title: false
hide_table_of_contents: false
keywords:
  - region_network_firewall_policies_effective_firewalls
  - compute
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>region_network_firewall_policies_effective_firewalls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.region_network_firewall_policies_effective_firewalls</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `firewallPolicys` | `array` | Effective firewalls from firewall policy. |
| `firewalls` | `array` | Effective firewalls on the network. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `regionNetworkFirewallPolicies_getEffectiveFirewalls` | `SELECT` | `network, project, region` |
