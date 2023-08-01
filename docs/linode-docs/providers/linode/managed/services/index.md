---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - managed
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.managed.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | This Service's unique ID.<br /> |
| `address` | `string` | The URL at which this Service is monitored.<br /><br />URL parameters such as `?no-cache=1` are preserved.<br /><br />URL fragments/anchors such as `#monitor` are **not** preserved.<br /> |
| `consultation_group` | `string` | The group of ManagedContacts who should be notified or consulted with when an Issue is detected.<br /> |
| `status` | `string` | The current status of this Service.<br /> |
| `label` | `string` | The label for this Service. This is for display purposes only.<br /> |
| `notes` | `string` | Any information relevant to the Service that Linode special forces should know when attempting to resolve Issues.<br /> |
| `service_type` | `string` | How this Service is monitored.<br /> |
| `created` | `string` | When this Managed Service was created. |
| `credentials` | `array` | An array of ManagedCredential IDs that should be used when attempting to resolve issues with this Service.<br /> |
| `region` | `string` | The Region in which this Service is located. This is required if address is a private IP, and may not be set otherwise.<br /> |
| `timeout` | `integer` | How long to wait, in seconds, for a response before considering the Service to be down.<br /> |
| `updated` | `string` | When this Managed Service was last updated. |
| `body` | `string` | What to expect to find in the response body for the Service to be considered up.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getManagedService` | `SELECT` | `serviceId` | Returns information about a single Managed Service on your Account.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| `getManagedServices` | `SELECT` |  | Returns a paginated list of Managed Services on your Account. These<br />are the services Linode Managed is monitoring and will report and attempt<br />to resolve issues with.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| `createManagedService` | `INSERT` | `data__address, data__label, data__service_type, data__timeout` | Creates a Managed Service. Linode Managed will begin monitoring this<br />service and reporting and attempting to resolve any Issues.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| `deleteManagedService` | `DELETE` | `serviceId` | Deletes a Managed Service.  This service will no longer be monitored by<br />Linode Managed.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| `_getManagedService` | `EXEC` | `serviceId` | Returns information about a single Managed Service on your Account.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| `_getManagedServices` | `EXEC` |  | Returns a paginated list of Managed Services on your Account. These<br />are the services Linode Managed is monitoring and will report and attempt<br />to resolve issues with.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| `disableManagedService` | `EXEC` | `serviceId` | Temporarily disables monitoring of a Managed Service.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| `enableManagedService` | `EXEC` | `serviceId` | Enables monitoring of a Managed Service.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| `updateManagedService` | `EXEC` | `serviceId` | Updates information about a Managed Service.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
