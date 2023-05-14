---
title: firewalls_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - firewalls_rules
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
<tr><td><b>Name</b></td><td><code>firewalls_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.networking.firewalls_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `inbound` | `array` | The inbound rules for the firewall, as a JSON array.<br /> |
| `inbound_policy` | `string` | The default behavior for inbound traffic. This setting can be overridden by [updating](/docs/api/networking/#firewall-rules-update) the `inbound.action` property of the Firewall Rule.<br /> |
| `outbound` | `array` | The outbound rules for the firewall, as a JSON array.<br /> |
| `outbound_policy` | `string` | The default behavior for outbound traffic. This setting can be overridden by [updating](/docs/api/networking/#firewall-rules-update) the `outbound.action` property of the Firewall Rule.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getFirewallRules` | `SELECT` | `firewallId` | Returns the inbound and outbound Rules for a Firewall.<br /> |
| `_getFirewallRules` | `EXEC` | `firewallId` | Returns the inbound and outbound Rules for a Firewall.<br /> |
| `updateFirewallRules` | `EXEC` | `firewallId` | Updates the inbound and outbound Rules for a Firewall.<br /><br />**Note:** This command replaces all of a Firewall's `inbound` and/or `outbound` rulesets with the values specified in your request.<br /> |
