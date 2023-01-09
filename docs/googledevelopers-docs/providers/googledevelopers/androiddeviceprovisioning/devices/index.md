---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
  - androiddeviceprovisioning
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androiddeviceprovisioning.devices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The API resource name in the format `partners/[PARTNER_ID]/devices/[DEVICE_ID]`. Assigned by the server. |
| `configuration` | `string` | Not available to resellers. |
| `deviceId` | `string` | Output only. The ID of the device. Assigned by the server. |
| `deviceIdentifier` | `object` | Encapsulates hardware and product IDs to identify a manufactured device. To understand requirements on identifier sets, read [Identifiers](https://developers.google.com/zero-touch/guides/identifiers). |
| `deviceMetadata` | `object` | Metadata entries that can be attached to a `Device`. To learn more, read [Device metadata](https://developers.google.com/zero-touch/guides/metadata). |
| `claims` | `array` | Output only. The provisioning claims for a device. Devices claimed for zero-touch enrollment have a claim with the type `SECTION_TYPE_ZERO_TOUCH`. Call `partners.devices.unclaim` or `partners.devices.unclaimAsync` to remove the device from zero-touch enrollment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `customers_devices_get` | `SELECT` | `customersId, devicesId` | Gets the details of a device. |
| `customers_devices_list` | `SELECT` | `customersId` | Lists a customer's devices. |
| `partners_devices_get` | `SELECT` | `devicesId, partnersId` | Gets a device. |
| `customers_devices_applyConfiguration` | `EXEC` | `customersId` | Applies a Configuration to the device to register the device for zero-touch enrollment. After applying a configuration to a device, the device automatically provisions itself on first boot, or next factory reset. |
| `customers_devices_unclaim` | `EXEC` | `customersId` | Unclaims a device from a customer and removes it from zero-touch enrollment. After removing a device, a customer must contact their reseller to register the device into zero-touch enrollment again. |
| `partners_devices_claim` | `EXEC` | `partnersId` | Claims a device for a customer and adds it to zero-touch enrollment. If the device is already claimed by another customer, the call returns an error. |
| `partners_devices_claimAsync` | `EXEC` | `partnersId` | Claims a batch of devices for a customer asynchronously. Adds the devices to zero-touch enrollment. To learn more, read [Long‑running batch operations](/zero-touch/guides/how-it-works#operations). |
| `partners_devices_findByIdentifier` | `EXEC` | `partnersId` | Finds devices by hardware identifiers, such as IMEI. |
| `partners_devices_findByOwner` | `EXEC` | `partnersId` | Finds devices claimed for customers. The results only contain devices registered to the reseller that's identified by the `partnerId` argument. The customer's devices purchased from other resellers don't appear in the results. |
| `partners_devices_metadata` | `EXEC` | `devicesId, partnersId` | Updates reseller metadata associated with the device. Android devices only. |
| `partners_devices_unclaim` | `EXEC` | `partnersId` | Unclaims a device from a customer and removes it from zero-touch enrollment. |
| `partners_devices_unclaimAsync` | `EXEC` | `partnersId` | Unclaims a batch of devices for a customer asynchronously. Removes the devices from zero-touch enrollment. To learn more, read [Long‑running batch operations](/zero-touch/guides/how-it-works#operations). |
| `partners_devices_updateMetadataAsync` | `EXEC` | `partnersId` | Updates the reseller metadata attached to a batch of devices. This method updates devices asynchronously and returns an `Operation` that can be used to track progress. Read [Long‑running batch operations](/zero-touch/guides/how-it-works#operations). Android Devices only. |
