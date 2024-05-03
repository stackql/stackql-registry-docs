---
title: firewalls_devices
hide_title: false
hide_table_of_contents: false
keywords:
  - firewalls_devices
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
<tr><td><b>Name</b></td><td><code>firewalls_devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.networking.firewalls_devices" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | The Device's unique ID<br /> |
| <CopyableCode code="created" /> | `string` | When this Device was created.<br /> |
| <CopyableCode code="entity" /> | `object` | The Linode service that this Firewall has been applied to.<br /> |
| <CopyableCode code="updated" /> | `string` | When this Device was last updated.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getFirewallDevice" /> | `SELECT` | <CopyableCode code="deviceId, firewallId" /> | Returns information for a Firewall Device, which assigns a Firewall<br />to a Linode service (referred to as the Device's `entity`). Currently,<br />only Devices with an entity of type `linode` are accepted.<br /> |
| <CopyableCode code="getFirewallDevices" /> | `SELECT` | <CopyableCode code="firewallId" /> | Returns a paginated list of a Firewall's Devices. A Firewall Device assigns a<br />Firewall to a Linode service (referred to as the Device's `entity`). Currently,<br />only Devices with an entity of type `linode` are accepted.<br /> |
| <CopyableCode code="createFirewallDevice" /> | `INSERT` | <CopyableCode code="firewallId, data__id, data__type" /> | Creates a Firewall Device, which assigns a Firewall to a service (referred to<br />as the Device's `entity`) and applies the Firewall's Rules to the device.<br /><br />* Currently, only Devices with an entity of type `linode` are accepted.<br /><br />* A Firewall can be assigned to multiple Linode instances at a time.<br /><br />* A Linode instance can have one active, assigned Firewall at a time.<br />Additional disabled Firewalls can be assigned to a service, but they cannot be enabled if another active Firewall is already assigned to the same service.<br /><br />* A `firewall_device_add` Event is generated when the Firewall Device is added successfully.<br /> |
| <CopyableCode code="deleteFirewallDevice" /> | `DELETE` | <CopyableCode code="deviceId, firewallId" /> | Removes a Firewall Device, which removes a Firewall from the Linode service it was<br />assigned to by the Device. This will remove all of the Firewall's Rules from the Linode<br />service. If any other Firewalls have been assigned to the Linode service, then those Rules<br />will remain in effect.<br /><br />A `firewall_device_remove` Event is generated when the Firewall Device is removed successfully.<br /> |
| <CopyableCode code="_getFirewallDevice" /> | `EXEC` | <CopyableCode code="deviceId, firewallId" /> | Returns information for a Firewall Device, which assigns a Firewall<br />to a Linode service (referred to as the Device's `entity`). Currently,<br />only Devices with an entity of type `linode` are accepted.<br /> |
| <CopyableCode code="_getFirewallDevices" /> | `EXEC` | <CopyableCode code="firewallId" /> | Returns a paginated list of a Firewall's Devices. A Firewall Device assigns a<br />Firewall to a Linode service (referred to as the Device's `entity`). Currently,<br />only Devices with an entity of type `linode` are accepted.<br /> |
