---
title: service_transfers
hide_title: false
hide_table_of_contents: false
keywords:
  - service_transfers
  - account
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
<tr><td><b>Name</b></td><td><code>service_transfers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.account.service_transfers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `updated` | `string` | When this transfer was last updated.<br /> |
| `created` | `string` | When this transfer was created.<br /> |
| `entities` | `object` | A collection of the services to include in this transfer request, separated by type.<br /> |
| `expiry` | `string` | When this transfer expires. Transfers will automatically expire 24 hours after creation.<br /> |
| `is_sender` | `boolean` | If the requesting account created this transfer.<br /> |
| `status` | `string` | The status of the transfer request.<br /><br />`accepted`: The transfer has been accepted by another user and is currently in progress.<br />Transfers can take up to 3 hours to complete.<br /><br />`cancelled`: The transfer has been cancelled by the sender.<br /><br />`completed`: The transfer has completed successfully.<br /><br />`failed`: The transfer has failed after initiation.<br /><br />`pending`: The transfer is ready to be accepted.<br /><br />`stale`: The transfer has exceeded its expiration date. It can no longer be accepted or<br />cancelled.<br /> |
| `token` | `string` | The token used to identify and accept or cancel this transfer.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getServiceTransfer` | `SELECT` | `token` | Returns the details of the Service Transfer for the provided token.<br /><br />While a transfer is pending, any unrestricted user *of any account* can access this command. After a<br />transfer has been accepted, it can only be viewed by unrestricted users of the accounts that created and<br />accepted the transfer. If cancelled or expired, only unrestricted users of the account that created the<br />transfer can view it.<br /> |
| `getServiceTransfers` | `SELECT` |  | Returns a collection of all created and accepted Service Transfers for this account, regardless of the user that created or accepted the transfer.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| `createServiceTransfer` | `INSERT` | `data__entities` | Creates a transfer request for the specified services. A request can contain any of the specified service types<br />and any number of each service type. At this time, only Linodes can be transferred.<br /><br />When created successfully, a confirmation email is sent to the account that created this transfer containing a<br />transfer token and instructions on completing the transfer.<br /><br />When a transfer is [accepted](/docs/api/account/#service-transfer-accept), the requested services are moved to<br />the receiving account. Linode services will not experience interruptions due to the transfer process. Backups<br />for Linodes are transferred as well.<br /><br />DNS records that are associated with requested services will not be transferred or updated. Please ensure that<br />associated DNS records have been updated or communicated to the recipient prior to the transfer.<br /><br />A transfer can take up to three hours to complete once accepted. When a transfer is<br />completed, billing for transferred services ends for the sending account and begins for the receiving account.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /><br />There are several conditions that must be met in order to successfully create a transfer request:<br /><br />1. The account creating the transfer must not have a past due balance or active Terms of Service violation.<br /><br />1. The service must be owned by the account that is creating the transfer.<br /><br />1. The service must not be assigned to another Service Transfer that is pending or that has been accepted and is<br />incomplete.<br /><br />1. Linodes must not:<br /><br />    * be assigned to a NodeBalancer, Firewall, VLAN, or Managed Service.<br /><br />    * have any attached Block Storage Volumes.<br /><br />    * have any shared IP addresses.<br /><br />    * have any assigned /56, /64, or /116 IPv6 ranges.<br /> |
| `deleteServiceTransfer` | `DELETE` | `token` | Cancels the Service Transfer for the provided token. Once cancelled, a transfer cannot be accepted or otherwise<br />acted on in any way. If cancelled in error, the transfer must be<br />[created](/docs/api/account/#service-transfer-create) again.<br /><br />When cancelled, an email notification for the cancellation is sent to the account that created<br />this transfer. Transfers can not be cancelled if they are expired or have been accepted.<br /><br />This command can only be accessed by the unrestricted users of the account that created this transfer.<br /> |
| `_getServiceTransfer` | `EXEC` | `token` | Returns the details of the Service Transfer for the provided token.<br /><br />While a transfer is pending, any unrestricted user *of any account* can access this command. After a<br />transfer has been accepted, it can only be viewed by unrestricted users of the accounts that created and<br />accepted the transfer. If cancelled or expired, only unrestricted users of the account that created the<br />transfer can view it.<br /> |
| `_getServiceTransfers` | `EXEC` |  | Returns a collection of all created and accepted Service Transfers for this account, regardless of the user that created or accepted the transfer.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| `acceptServiceTransfer` | `EXEC` | `token` | Accept a Service Transfer for the provided token to receive the services included in the transfer to your<br />account. At this time, only Linodes can be transferred.<br /><br />When accepted, email confirmations are sent to the accounts that created and accepted the transfer. A transfer<br />can take up to three hours to complete once accepted. Once a transfer is completed, billing for transferred<br />services ends for the sending account and begins for the receiving account.<br /><br />This command can only be accessed by the unrestricted users of the account that receives the transfer. Users<br />of the same account that created a transfer cannot accept the transfer.<br /><br />There are several conditions that must be met in order to accept a transfer request:<br /><br />1. Only transfers with a `pending` status can be accepted.<br /><br />1. The account accepting the transfer must have a registered payment method and must not have a past due<br />  balance or other account limitations for the services to be transferred.<br /><br />1. Both the account that created the transfer and the account that is accepting the transfer must not have any<br />active Terms of Service violations.<br /><br />1. The service must still be owned by the account that created the transfer.<br /><br />1. Linodes must not:<br /><br />    * be assigned to a NodeBalancer, Firewall, VLAN, or Managed Service.<br /><br />    * have any attached Block Storage Volumes.<br /><br />    * have any shared IP addresses.<br /><br />    * have any assigned /56, /64, or /116 IPv6 ranges.<br /><br />Any and all of the above conditions must be cured and maintained by the relevant account prior to the<br />transfer's expiration to allow the transfer to be accepted by the receiving account.<br /> |
