---
title: account
hide_title: false
hide_table_of_contents: false
keywords:
  - account
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.account.account" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="active_promotions" /> | `array` |  |
| <CopyableCode code="active_since" /> | `string` | The datetime of when the account was activated. |
| <CopyableCode code="address_1" /> | `string` | First line of this Account's billing address. |
| <CopyableCode code="address_2" /> | `string` | Second line of this Account's billing address. |
| <CopyableCode code="balance" /> | `number` | This Account's balance, in US dollars. |
| <CopyableCode code="balance_uninvoiced" /> | `number` | This Account's current estimated invoice in US dollars. This is not your final invoice balance. Transfer charges are not included in the estimate.<br /> |
| <CopyableCode code="billing_source" /> | `string` | The source of service charges for this Account, as determined by its relationship with Akamai.<br />Accounts that are associated with Akamai-specific customers return a value of `akamai`.<br />All other Accounts return a value of `linode`.<br /> |
| <CopyableCode code="capabilities" /> | `array` | A list of capabilities your account supports.<br /> |
| <CopyableCode code="city" /> | `string` | The city for this Account's billing address. |
| <CopyableCode code="company" /> | `string` | The company name associated with this Account. |
| <CopyableCode code="country" /> | `string` | The two-letter ISO 3166 country code of this Account's billing address.<br /> |
| <CopyableCode code="credit_card" /> | `object` | Credit Card information associated with this Account. |
| <CopyableCode code="email" /> | `string` | The email address of the person associated with this Account. |
| <CopyableCode code="euuid" /> | `string` | An external unique identifier for this account.<br /> |
| <CopyableCode code="first_name" /> | `string` | The first name of the person associated with this Account. |
| <CopyableCode code="last_name" /> | `string` | The last name of the person associated with this Account. |
| <CopyableCode code="phone" /> | `string` | The phone number associated with this Account. |
| <CopyableCode code="state" /> | `string` | If billing address is in the United States (US) or Canada (CA), only the two-letter ISO 3166 State or Province code are accepted. If entering a US military address, state abbreviations (AA, AE, AP) should be entered. If the address is outside the US or CA, this is the Province associated with the Account's billing address.<br /> |
| <CopyableCode code="tax_id" /> | `string` | The tax identification number associated with this Account, for tax calculations in some countries. If you do not live in a country that collects tax, this should be an empty string (`""`).<br /> |
| <CopyableCode code="zip" /> | `string` | The zip code of this Account's billing address. The following restrictions apply:<br /><br />- May only consist of letters, numbers, spaces, and hyphens.<br />- Must not contain more than 9 letter or number characters.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getAccount" /> | `SELECT` |  | Returns the contact and billing information related to your Account.<br /> |
| <CopyableCode code="_getAccount" /> | `EXEC` |  | Returns the contact and billing information related to your Account.<br /> |
| <CopyableCode code="cancelAccount" /> | `EXEC` |  | Cancels an active Linode account. This action will cause Linode to attempt to charge the credit card on file for the remaining balance. An error will occur if Linode fails to charge the credit card on file. Restricted users will not be able to cancel an account.<br /> |
| <CopyableCode code="updateAccount" /> | `EXEC` |  | Updates contact and billing information related to your Account.<br /> |
