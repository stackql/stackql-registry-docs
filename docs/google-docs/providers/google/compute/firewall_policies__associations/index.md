---
title: firewall_policies__associations
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_policies__associations
  - compute
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_policies__associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.firewall_policies__associations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `associations` | `array` | A list of associations. |
| `kind` | `string` | [Output Only] Type of firewallPolicy associations. Always compute#FirewallPoliciesListAssociations for lists of firewallPolicy associations. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `firewallPolicies_listAssociations` | `SELECT` |  |
