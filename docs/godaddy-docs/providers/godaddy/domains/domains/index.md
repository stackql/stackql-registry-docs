---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - domains
  - godaddy    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GoDaddy resources using SQL
custom_edit_url: null
image: /img/providers/godaddy/stackql-godaddy-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>godaddy.domains.domains</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `authCode` | `string` | Authorization code for transferring the Domain |
| `contactAdmin` | `object` |  |
| `contactBilling` | `object` |  |
| `contactRegistrant` | `object` |  |
| `contactTech` | `object` |  |
| `createdAt` | `string` | Date and time when this domain was created |
| `deletedAt` | `string` | Date and time when this domain was deleted |
| `domain` | `string` | Name of the domain |
| `domainId` | `number` | Unique identifier for this Domain |
| `expirationProtected` | `boolean` | Whether or not the domain is protected from expiration |
| `expires` | `string` | Date and time when this domain will expire |
| `holdRegistrar` | `boolean` | Whether or not the domain is on-hold by the registrar |
| `locked` | `boolean` | Whether or not the domain is locked to prevent transfers |
| `nameServers` | `array` | Fully-qualified domain names for DNS servers |
| `privacy` | `boolean` | Whether or not the domain has privacy protection |
| `renewAuto` | `boolean` | Whether or not the domain is configured to automatically renew |
| `renewDeadline` | `string` | Date the domain must renew on |
| `status` | `string` | Processing status of the domain<br />ACTIVE - All is well<br />AWAITING* - System is waiting for the end-user to complete an action<br />CANCELLED* - Domain has been cancelled, and may or may not be reclaimable<br />CONFISCATED - Domain has been confiscated, usually for abuse, chargeback, or fraud<br />DISABLED* - Domain has been disabled<br />EXCLUDED* - Domain has been excluded from Firehose registration<br />EXPIRED* - Domain has expired<br />FAILED* - Domain has failed a required action, and the system is no longer retrying<br />HELD* - Domain has been placed on hold, and likely requires intervention from Support<br />LOCKED* - Domain has been locked, and likely requires intervention from Support<br />PARKED* - Domain has been parked, and likely requires intervention from Support<br />PENDING* - Domain is working its way through an automated workflow<br />RESERVED* - Domain is reserved, and likely requires intervention from Support<br />REVERTED - Domain has been reverted, and likely requires intervention from Support<br />SUSPENDED* - Domain has been suspended, and likely requires intervention from Support<br />TRANSFERRED* - Domain has been transferred out<br />UNKNOWN - Domain is in an unknown state<br />UNLOCKED* - Domain has been unlocked, and likely requires intervention from Support<br />UNPARKED* - Domain has been unparked, and likely requires intervention from Support<br />UPDATED* - Domain ownership has been transferred to another account<br /> |
| `subaccountId` | `string` | Reseller subaccount shopperid who can manage the domain |
| `transferProtected` | `boolean` | Whether or not the domain is protected from transfer |
| `verifications` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `domain` | Retrieve details for the specified Domain |
| `list` | `SELECT` |  | Retrieve a list of Domains for the specified Shopper |
| `cancel` | `EXEC` | `domain` | Cancel a purchased domain |
| `cancel_privacy` | `EXEC` | `domain` | Submit a privacy cancellation request for the given domain |
| `contacts_validate` | `EXEC` | `data__domains` | All contacts specified in request will be validated against all domains specifed in "domains". As an alternative, you can also pass in tlds, with the exception of `uk`, which requires full domain names |
| `purchase` | `EXEC` | `data__consent, data__domain` | Purchase and register the specified Domain |
| `purchase_privacy` | `EXEC` | `domain, data__consent` | Purchase privacy for a specified domain |
| `renew` | `EXEC` | `domain` | Renew the specified Domain |
| `transfer_in` | `EXEC` | `domain, data__authCode, data__consent` | Purchase and start or restart transfer process |
| `update` | `EXEC` | `domain` | Update details for the specified Domain |
| `update_contacts` | `EXEC` | `domain, data__contactRegistrant` | Update domain |
| `validate` | `EXEC` | `data__consent, data__domain` | Validate the request body using the Domain Purchase Schema for the specified TLD |
| `verify_email` | `EXEC` | `domain` | Re-send Contact E-mail Verification for specified Domain |
