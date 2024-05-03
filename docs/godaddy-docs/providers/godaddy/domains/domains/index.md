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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="godaddy.domains.domains" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="authCode" /> | `string` | Authorization code for transferring the Domain |
| <CopyableCode code="contactAdmin" /> | `object` |  |
| <CopyableCode code="contactBilling" /> | `object` |  |
| <CopyableCode code="contactRegistrant" /> | `object` |  |
| <CopyableCode code="contactTech" /> | `object` |  |
| <CopyableCode code="createdAt" /> | `string` | Date and time when this domain was created |
| <CopyableCode code="deletedAt" /> | `string` | Date and time when this domain was deleted |
| <CopyableCode code="domain" /> | `string` | Name of the domain |
| <CopyableCode code="domainId" /> | `number` | Unique identifier for this Domain |
| <CopyableCode code="expirationProtected" /> | `boolean` | Whether or not the domain is protected from expiration |
| <CopyableCode code="expires" /> | `string` | Date and time when this domain will expire |
| <CopyableCode code="holdRegistrar" /> | `boolean` | Whether or not the domain is on-hold by the registrar |
| <CopyableCode code="locked" /> | `boolean` | Whether or not the domain is locked to prevent transfers |
| <CopyableCode code="nameServers" /> | `array` | Fully-qualified domain names for DNS servers |
| <CopyableCode code="privacy" /> | `boolean` | Whether or not the domain has privacy protection |
| <CopyableCode code="renewAuto" /> | `boolean` | Whether or not the domain is configured to automatically renew |
| <CopyableCode code="renewDeadline" /> | `string` | Date the domain must renew on |
| <CopyableCode code="status" /> | `string` | Processing status of the domain<br />ACTIVE - All is well<br />AWAITING* - System is waiting for the end-user to complete an action<br />CANCELLED* - Domain has been cancelled, and may or may not be reclaimable<br />CONFISCATED - Domain has been confiscated, usually for abuse, chargeback, or fraud<br />DISABLED* - Domain has been disabled<br />EXCLUDED* - Domain has been excluded from Firehose registration<br />EXPIRED* - Domain has expired<br />FAILED* - Domain has failed a required action, and the system is no longer retrying<br />HELD* - Domain has been placed on hold, and likely requires intervention from Support<br />LOCKED* - Domain has been locked, and likely requires intervention from Support<br />PARKED* - Domain has been parked, and likely requires intervention from Support<br />PENDING* - Domain is working its way through an automated workflow<br />RESERVED* - Domain is reserved, and likely requires intervention from Support<br />REVERTED - Domain has been reverted, and likely requires intervention from Support<br />SUSPENDED* - Domain has been suspended, and likely requires intervention from Support<br />TRANSFERRED* - Domain has been transferred out<br />UNKNOWN - Domain is in an unknown state<br />UNLOCKED* - Domain has been unlocked, and likely requires intervention from Support<br />UNPARKED* - Domain has been unparked, and likely requires intervention from Support<br />UPDATED* - Domain ownership has been transferred to another account<br /> |
| <CopyableCode code="subaccountId" /> | `string` | Reseller subaccount shopperid who can manage the domain |
| <CopyableCode code="transferProtected" /> | `boolean` | Whether or not the domain is protected from transfer |
| <CopyableCode code="verifications" /> | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="domain" /> | Retrieve details for the specified Domain |
| <CopyableCode code="list" /> | `SELECT` |  | Retrieve a list of Domains for the specified Shopper |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="domain" /> | Cancel a purchased domain |
| <CopyableCode code="cancel_privacy" /> | `EXEC` | <CopyableCode code="domain" /> | Submit a privacy cancellation request for the given domain |
| <CopyableCode code="contacts_validate" /> | `EXEC` | <CopyableCode code="data__domains" /> | All contacts specified in request will be validated against all domains specifed in "domains". As an alternative, you can also pass in tlds, with the exception of `uk`, which requires full domain names |
| <CopyableCode code="purchase" /> | `EXEC` | <CopyableCode code="data__consent, data__domain" /> | Purchase and register the specified Domain |
| <CopyableCode code="purchase_privacy" /> | `EXEC` | <CopyableCode code="domain, data__consent" /> | Purchase privacy for a specified domain |
| <CopyableCode code="renew" /> | `EXEC` | <CopyableCode code="domain" /> | Renew the specified Domain |
| <CopyableCode code="transfer_in" /> | `EXEC` | <CopyableCode code="domain, data__authCode, data__consent" /> | Purchase and start or restart transfer process |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="domain" /> | Update details for the specified Domain |
| <CopyableCode code="update_contacts" /> | `EXEC` | <CopyableCode code="domain, data__contactRegistrant" /> | Update domain |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="data__consent, data__domain" /> | Validate the request body using the Domain Purchase Schema for the specified TLD |
| <CopyableCode code="verify_email" /> | `EXEC` | <CopyableCode code="domain" /> | Re-send Contact E-mail Verification for specified Domain |
