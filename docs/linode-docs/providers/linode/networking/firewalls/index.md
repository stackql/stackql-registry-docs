---
title: firewalls
hide_title: false
hide_table_of_contents: false
keywords:
  - firewalls
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
<tr><td><b>Name</b></td><td><code>firewalls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.networking.firewalls" /></td></tr>
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
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getFirewall" /> | `SELECT` | <CopyableCode code="firewallId" /> | Get a specific Firewall resource by its ID. The Firewall's Devices will not be<br />returned in the response. Instead, use the<br />[List Firewall Devices](/docs/api/networking/#firewall-devices-list)<br />endpoint to review them.<br /> |
| <CopyableCode code="getFirewalls" /> | `SELECT` |  | Returns a paginated list of accessible Firewalls.<br /> |
| <CopyableCode code="createFirewalls" /> | `INSERT` | <CopyableCode code="data__rules" /> | Creates a Firewall to filter network traffic.<br /><br />* Use the `rules` property to create inbound and outbound access rules.<br /><br />* Use the `devices` property to assign the Firewall to a service and apply its Rules to the device. Requires `read_write` [User's Grants](/docs/api/account/#users-grants-view) to the device.<br />Currently, Firewalls can only be assigned to Linode instances.<br /><br />* A Firewall can be assigned to multiple Linode instances at a time.<br /><br />* A Linode instance can have one active, assigned Firewall at a time.<br />Additional disabled Firewalls can be assigned to a service, but they cannot be enabled if another active Firewall is already assigned to the same service.<br /><br />* A `firewall_create` Event is generated when this endpoint returns successfully.<br /> |
| <CopyableCode code="deleteFirewall" /> | `DELETE` | <CopyableCode code="firewallId" /> | Delete a Firewall resource by its ID. This will remove all of the Firewall's Rules<br />from any Linode services that the Firewall was assigned to.<br /><br />A `firewall_delete` Event is generated when this endpoint returns successfully.<br /> |
| <CopyableCode code="_getFirewall" /> | `EXEC` | <CopyableCode code="firewallId" /> | Get a specific Firewall resource by its ID. The Firewall's Devices will not be<br />returned in the response. Instead, use the<br />[List Firewall Devices](/docs/api/networking/#firewall-devices-list)<br />endpoint to review them.<br /> |
| <CopyableCode code="_getFirewalls" /> | `EXEC` |  | Returns a paginated list of accessible Firewalls.<br /> |
| <CopyableCode code="updateFirewall" /> | `EXEC` | <CopyableCode code="firewallId" /> | Updates information for a Firewall. Some parts of a Firewall's configuration cannot<br />be manipulated by this endpoint:<br /><br />- A Firewall's Devices cannot be set with this endpoint. Instead, use the<br />[Create Firewall Device](/docs/api/networking/#firewall-device-create)<br />and [Delete Firewall Device](/docs/api/networking/#firewall-device-delete)<br />endpoints to assign and remove this Firewall from Linode services.<br /><br />- A Firewall's Rules cannot be changed with this endpoint. Instead, use the<br />[Update Firewall Rules](/docs/api/networking/#firewall-rules-update)<br />endpoint to update your Rules.<br /><br />- A Firewall's status can be set to `enabled` or `disabled` by this endpoint, but it cannot be<br />set to `deleted`. Instead, use the<br />[Delete Firewall](/docs/api/networking/#firewall-delete)<br />endpoint to delete a Firewall.<br /><br />If a Firewall's status is changed with this endpoint, a corresponding `firewall_enable` or<br />`firewall_disable` Event will be generated.<br /> |
