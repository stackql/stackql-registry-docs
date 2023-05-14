---
title: vlans
hide_title: false
hide_table_of_contents: false
keywords:
  - vlans
  - networking
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vlans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.networking.vlans</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `created` | `string` | The date this VLAN was created.<br /> |
| `label` | `string` | The name of this VLAN. |
| `linodes` | `array` | An array of Linode IDs attached to this VLAN.<br /> |
| `region` | `string` | This VLAN's data center region.<br /><br />**Note:** Currently, a VLAN can only be assigned to a Linode<br />within the same data center region.<br /> |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getVLANs` | `SELECT` |  |
| `_getVLANs` | `EXEC` |  |
