---
title: configs
hide_title: false
hide_table_of_contents: false
keywords:
  - configs
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.instances.configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The ID of this Config. |
| `root_device` | `string` | The root device to boot.<br />* If no value or an invalid value is provided, root device will default to `/dev/sda`.<br />* If the device specified at the root device location is not mounted, the Linode will not boot until a device is mounted.<br /> |
| `virt_mode` | `string` | Controls the virtualization mode. Defaults to `paravirt`.<br />* `paravirt` is suitable for most cases. Linodes running in paravirt mode<br />  share some qualities with the host, ultimately making it run faster since<br />  there is less transition between it and the host.<br />* `fullvirt` affords more customization, but is slower because 100% of the VM<br />  is virtualized.<br /> |
| `comments` | `string` | Optional field for arbitrary User comments on this Config. |
| `kernel` | `string` | A Kernel ID to boot a Linode with. Defaults to "linode/latest-64bit". |
| `memory_limit` | `integer` | Defaults to the total RAM of the Linode.<br /> |
| `helpers` | `object` | Helpers enabled when booting to this Linode Config. |
| `label` | `string` | The Config's label is for display purposes only.<br /> |
| `run_level` | `string` | Defines the state of your Linode after booting. Defaults to `default`.<br /> |
| `devices` | `object` | A dictionary of device disks to use as a device map in a Linode's configuration profile.<br />* An empty device disk dictionary or a dictionary with empty values for device slots is allowed.<br />* If no devices are specified, booting from this configuration will hold until a device exists that allows the boot process to start.<br /> |
| `interfaces` | `array` | An array of Network Interfaces to add to this Linode's Configuration Profile.<br /><br />Up to three interface objects can be entered in this array. The position in the array determines the interface to which the settings apply:<br /><br />- First/0:  eth0<br />- Second/1: eth1<br />- Third/2:  eth2<br /><br />When updating a Linode's interfaces, *each interface must be redefined*. An empty interfaces array results in a default public interface configuration only.<br /><br />If no public interface is configured, public IP addresses are still assigned to the Linode but will not be usable without manual configuration.<br /><br />**Note:** Changes to Linode interface configurations can be enabled by rebooting the Linode.<br /><br />**Note:** Only Next Generation Network (NGN) data centers support VLANs. Use the Regions ([/regions](/docs/api/regions/)) endpoint to view the capabilities of data center regions.<br />If a VLAN is attached to your Linode and you attempt to migrate or clone it to a non-NGN data center,<br />the migration or cloning will not initiate. If a Linode cannot be migrated because of an incompatibility,<br />you will be prompted to select a different data center or contact support.<br /><br />**Note:** See the [VLANs Overview](/docs/products/networking/vlans/#technical-specifications) guide to view additional specifications and limitations.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getLinodeConfig` | `SELECT` | `configId, linodeId` | Returns information about a specific Configuration profile.<br /> |
| `getLinodeConfigs` | `SELECT` | `linodeId` | Lists Configuration profiles associated with a Linode.<br /> |
| `addLinodeConfig` | `INSERT` | `linodeId, data__devices, data__label` | Adds a new Configuration profile to a Linode.<br /> |
| `deleteLinodeConfig` | `DELETE` | `configId, linodeId` | Deletes the specified Configuration profile from the specified Linode.<br /> |
| `_getLinodeConfig` | `EXEC` | `configId, linodeId` | Returns information about a specific Configuration profile.<br /> |
| `_getLinodeConfigs` | `EXEC` | `linodeId` | Lists Configuration profiles associated with a Linode.<br /> |
| `updateLinodeConfig` | `EXEC` | `configId, linodeId` | Updates a Configuration profile.<br /> |
