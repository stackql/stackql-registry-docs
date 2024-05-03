---
title: firewalls
hide_title: false
hide_table_of_contents: false
keywords:
  - firewalls
  - instances
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
<tr><td><b>Name</b></td><td><code>firewalls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.instances.firewalls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | The Firewall's unique ID.<br /> |
| <CopyableCode code="created" /> | `string` | When this Firewall was created.<br /> |
| <CopyableCode code="label" /> | `string` | The Firewall's label, for display purposes only.<br /><br />Firewall labels have the following constraints:<br /><br />  * Must begin and end with an alphanumeric character.<br />  * May only consist of alphanumeric characters, dashes (`-`), underscores (`_`) or periods (`.`).<br />  * Cannot have two dashes (`--`), underscores (`__`) or periods (`..`) in a row.<br />  * Must be between 3 and 32 characters.<br />  * Must be unique.<br /> |
| <CopyableCode code="rules" /> | `object` | The inbound and outbound access rules to apply to the Firewall.<br /><br />A Firewall may have up to 25 rules across its inbound and outbound rulesets.<br /> |
| <CopyableCode code="status" /> | `string` | The status of this Firewall.<br /><br />  * When a Firewall is first created its status is `enabled`.<br />  * Use the [Update Firewall](/docs/api/networking/#firewall-update) endpoint to set a Firewall's status to `enabled` or `disabled`.<br />  * Use the [Delete Firewall](/docs/api/networking/#firewall-delete) endpoint to delete a Firewall.<br /> |
| <CopyableCode code="tags" /> | `array` | An array of tags applied to this object. Tags are for organizational purposes only.<br /> |
| <CopyableCode code="updated" /> | `string` | When this Firewall was last updated.<br /> |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="getLinodeFirewalls" /> | `SELECT` | <CopyableCode code="linodeId" /> |
| <CopyableCode code="_getLinodeFirewalls" /> | `EXEC` | <CopyableCode code="linodeId" /> |
