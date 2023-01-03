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
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>password_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.password_policy.password_policy</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `maxLength` | `integer` | The maximum length of the password. (Setting this to any value other than 128 is no longer supported; this field may be deprecated in the future.) |
| `mustContainDigits` | `boolean` | If the password must contain digits. |
| `requireMfa` | `boolean` | If MFA should be required to log in. By default, this field is set to `false`. |
| `maxPasswordAgeInDays` | `integer` | Maximum number of days that a password can be used before user is required to change it. Put -1 if the user should not have to change their password. |
| `accountLockoutThreshold` | `integer` | Number of failed login attempts allowed before account is locked-out. |
| `mustContainLowercase` | `boolean` | If the password must contain lower case characters. |
| `mustContainUppercase` | `boolean` | If the password must contain upper case characters. |
| `rememberMfa` | `boolean` | If MFA should be remembered on the browser. |
| `accountLockoutDurationInMins` | `integer` | The duration of time in minutes that a locked-out account remained locked before getting unlocked automatically. |
| `minLength` | `integer` | The minimum length of the password. |
| `minUniquePasswords` | `integer` | The minimum number of unique new passwords that a user must use before an old password can be reused. |
| `mustContainSpecialChars` | `boolean` | If the password must contain special characters. |
| `failedLoginResetDurationInMins` | `integer` | The duration of time in minutes that must elapse from the first failed login attempt after which failed login count is reset to 0. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getPasswordPolicy` | `SELECT` |  | Get the current password policy. |
| `setPasswordPolicy` | `EXEC` |  | Update the current password policy. |
