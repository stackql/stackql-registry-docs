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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewalls_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.networking.firewalls_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="inbound" /> | `array` | The inbound rules for the firewall, as a JSON array.<br /> |
| <CopyableCode code="inbound_policy" /> | `string` | The default behavior for inbound traffic. This setting can be overridden by [updating](/docs/api/networking/#firewall-rules-update) the `inbound.action` property of the Firewall Rule.<br /> |
| <CopyableCode code="outbound" /> | `array` | The outbound rules for the firewall, as a JSON array.<br /> |
| <CopyableCode code="outbound_policy" /> | `string` | The default behavior for outbound traffic. This setting can be overridden by [updating](/docs/api/networking/#firewall-rules-update) the `outbound.action` property of the Firewall Rule.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getFirewallRules" /> | `SELECT` | <CopyableCode code="firewallId" /> | Returns the inbound and outbound Rules for a Firewall.<br /> |
| <CopyableCode code="_getFirewallRules" /> | `EXEC` | <CopyableCode code="firewallId" /> | Returns the inbound and outbound Rules for a Firewall.<br /> |
| <CopyableCode code="updateFirewallRules" /> | `EXEC` | <CopyableCode code="firewallId" /> | Updates the inbound and outbound Rules for a Firewall.<br /><br />**Note:** This command replaces all of a Firewall's `inbound` and/or `outbound` rulesets with the values specified in your request.<br /> |
