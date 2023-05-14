---
title: phone_number
hide_title: false
hide_table_of_contents: false
keywords:
  - phone_number
  - profile
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
<tr><td><b>Name</b></td><td><code>phone_number</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.profile.phone_number</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `deleteProfilePhoneNumber` | `DELETE` |  | Delete the verified phone number for the User making this request.<br /><br />Use this command to opt out of SMS messages for the requesting User after a phone number has been verified with the **Phone Number Verify** ([POST /profile/phone-number/verify](/docs/api/profile/#phone-number-verify)) command.<br /> |
| `postProfilePhoneNumber` | `EXEC` | `data__iso_code, data__phone_number` | Send a one-time verification code via SMS message to the submitted phone number. Providing your phone number helps ensure you can securely access your Account in case other ways to connect are lost. Your phone number is only used to verify your identity by sending an SMS message. Standard carrier messaging fees may apply.<br /><br />* By accessing this command you are opting in to receive SMS messages. You can opt out of SMS messages by using the **Phone Number Delete** ([DELETE /profile/phone-number](/docs/api/profile/#phone-number-delete)) command after your phone number is verified.<br /><br />* Verification codes are valid for 10 minutes after they are sent.<br /><br />* Subsequent requests made prior to code expiration result in sending the same code.<br /><br />Once a verification code is received, verify your phone number with the **Phone Number Verify** ([POST /profile/phone-number/verify](/docs/api/profile/#phone-number-verify)) command.<br /> |
| `postProfilePhoneNumberVerify` | `EXEC` | `data__otp_code` | Verify a phone number by confirming the one-time code received via SMS message after accessing the **Phone Verification Code Send** ([POST /profile/phone-number](/docs/api/profile/#phone-number-verification-code-send)) command.<br /><br />* Verification codes are valid for 10 minutes after they are sent.<br /><br />* Only the same User that made the verification code request can use that code with this command.<br /><br />Once completed, the verified phone number is assigned to the User making the request. To change the verified phone number for a User, first use the **Phone Number Delete** ([DELETE /profile/phone-number](/docs/api/profile/#phone-number-delete)) command, then begin the verification process again with the **Phone Verification Code Send** ([POST /profile/phone-number](/docs/api/profile/#phone-number-verification-code-send)) command.<br /> |
