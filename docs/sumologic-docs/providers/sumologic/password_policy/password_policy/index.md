---
title: password_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - password_policy
  - password_policy
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>password_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.password_policy.password_policy" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountLockoutDurationInMins" /> | `integer` | The duration of time in minutes that a locked-out account remained locked before getting unlocked automatically. |
| <CopyableCode code="accountLockoutThreshold" /> | `integer` | Number of failed login attempts allowed before account is locked-out. |
| <CopyableCode code="failedLoginResetDurationInMins" /> | `integer` | The duration of time in minutes that must elapse from the first failed login attempt after which failed login count is reset to 0. |
| <CopyableCode code="maxLength" /> | `integer` | The maximum length of the password. (Setting this to any value other than 128 is no longer supported; this field may be deprecated in the future.) |
| <CopyableCode code="maxPasswordAgeInDays" /> | `integer` | Maximum number of days that a password can be used before user is required to change it. Put -1 if the user should not have to change their password. |
| <CopyableCode code="minLength" /> | `integer` | The minimum length of the password. |
| <CopyableCode code="minUniquePasswords" /> | `integer` | The minimum number of unique new passwords that a user must use before an old password can be reused. |
| <CopyableCode code="mustContainDigits" /> | `boolean` | If the password must contain digits. |
| <CopyableCode code="mustContainLowercase" /> | `boolean` | If the password must contain lower case characters. |
| <CopyableCode code="mustContainSpecialChars" /> | `boolean` | If the password must contain special characters. |
| <CopyableCode code="mustContainUppercase" /> | `boolean` | If the password must contain upper case characters. |
| <CopyableCode code="rememberMfa" /> | `boolean` | If MFA should be remembered on the browser. |
| <CopyableCode code="requireMfa" /> | `boolean` | If MFA should be required to log in. By default, this field is set to `false`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getPasswordPolicy" /> | `SELECT` | <CopyableCode code="region" /> | Get the current password policy. |
| <CopyableCode code="setPasswordPolicy" /> | `EXEC` | <CopyableCode code="region" /> | Update the current password policy. |
