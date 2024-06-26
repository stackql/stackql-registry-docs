---
title: profile
hide_title: false
hide_table_of_contents: false
keywords:
  - profile
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.profile.profile" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="authentication_type" /> | `string` | This account's Cloud Manager authentication type. Authentication types are chosen through<br />Cloud Manager and authorized when logging into your account. These authentication types are either<br />the user's password (in conjunction with their username), or the name of their<br />indentity provider such as GitHub. For example, if a user:<br /><br />- Has never used Third-Party Authentication, their authentication type will be `password`.<br />- Is using Third-Party Authentication, their authentication type will be the name of their Identity Provider (eg. `github`).<br />- Has used Third-Party Authentication and has since revoked it, their authentication type will be `password`.<br /><br /><br />**Note:** This functionality may not yet be available in Cloud Manager.<br />See the [Cloud Manager Changelog](/changelog/cloud-manager/) for the latest updates.<br /> |
| <CopyableCode code="authorized_keys" /> | `array` | The list of SSH Keys authorized to use Lish for your User. This value is ignored if `lish_auth_method` is "disabled."<br /> |
| <CopyableCode code="email" /> | `string` | Your email address.  This address will be used for communication with Linode as necessary.<br /> |
| <CopyableCode code="email_notifications" /> | `boolean` | If true, you will receive email notifications about account activity.  If false, you may still receive business-critical communications through email.<br /> |
| <CopyableCode code="ip_whitelist_enabled" /> | `boolean` | If true, logins for your User will only be allowed from whitelisted IPs. This setting is currently deprecated, and cannot be enabled.<br /><br />If you disable this setting, you will not be able to re-enable it.<br /> |
| <CopyableCode code="lish_auth_method" /> | `string` | The authentication methods that are allowed when connecting to [the Linode Shell (Lish)](/docs/guides/lish/).<br />* `keys_only` is the most secure if you intend to use Lish.<br />* `disabled` is recommended if you do not intend to use Lish at all.<br />* If this account's Cloud Manager authentication type is set to a Third-Party Authentication method, `password_keys` cannot be used as your Lish authentication method. To view this account's Cloud Manager `authentication_type` field, send a request to the [View Profile](/docs/api/profile/#profile-view) endpoint.<br /> |
| <CopyableCode code="referrals" /> | `object` | Information about your status in our referral program.<br /><br />This information becomes accessible after this Profile's Account has established at least $25.00 USD of total payments.<br /> |
| <CopyableCode code="restricted" /> | `boolean` | If true, your User has restrictions on what can be accessed on your Account. To get details on what entities/actions you can access/perform, see [/profile/grants](/docs/api/profile/#grants-list).<br /> |
| <CopyableCode code="timezone" /> | `string` | The timezone you prefer to see times in. This is not used by the API directly. It is provided for the benefit of clients such as the Linode Cloud Manager and other clients built on the API. All times returned by the API are in UTC.<br /> |
| <CopyableCode code="two_factor_auth" /> | `boolean` | If true, logins from untrusted computers will require Two Factor Authentication.  See [/profile/tfa-enable](/docs/api/profile/#two-factor-secret-create) to enable Two Factor Authentication.<br /> |
| <CopyableCode code="uid" /> | `integer` | Your unique ID in our system. This value will never change, and can safely be used to identify your User.<br /> |
| <CopyableCode code="username" /> | `string` | Your username, used for logging in to our system.<br /> |
| <CopyableCode code="verified_phone_number" /> | `string` | The phone number verified for this Profile with the **Phone Number Verify** ([POST /profile/phone-number/verify](/docs/api/profile/#phone-number-verify)) command.<br /><br />`null` if this Profile has no verified phone number.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getProfile" /> | `SELECT` |  | Returns information about the current User. This can be used to see who is acting in applications where more than one token is managed. For example, in third-party OAuth applications.<br /><br />This endpoint is always accessible, no matter what OAuth scopes the acting token has.<br /> |
| <CopyableCode code="_getProfile" /> | `EXEC` |  | Returns information about the current User. This can be used to see who is acting in applications where more than one token is managed. For example, in third-party OAuth applications.<br /><br />This endpoint is always accessible, no matter what OAuth scopes the acting token has.<br /> |
| <CopyableCode code="updateProfile" /> | `EXEC` |  | Update information in your Profile.  This endpoint requires the "account:read_write" OAuth Scope.<br /> |
