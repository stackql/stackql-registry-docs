---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
  - cloudidentity
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
<tr><td><b>Name</b></td><td><code>devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudidentity.devices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `devices` | `array` | Devices meeting the list restrictions. |
| `nextPageToken` | `string` | Token to retrieve the next page of results. Empty if there are no more results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `devicesId` | Retrieves the specified device. |
| `list` | `SELECT` |  | Lists/Searches devices. |
| `create` | `INSERT` |  | Creates a device. Only company-owned device may be created. **Note**: This method is available only to customers who have one of the following SKUs: Enterprise Standard, Enterprise Plus, Enterprise for Education, and Cloud Identity Premium |
| `delete` | `DELETE` | `devicesId` | Deletes the specified device. |
| `cancel_wipe` | `EXEC` | `devicesId` | Cancels an unfinished device wipe. This operation can be used to cancel device wipe in the gap between the wipe operation returning success and the device being wiped. This operation is possible when the device is in a "pending wipe" state. The device enters the "pending wipe" state when a wipe device command is issued, but has not yet been sent to the device. The cancel wipe will fail if the wipe command has already been issued to the device. |
| `wipe` | `EXEC` | `devicesId` | Wipes all data on the specified device. |
