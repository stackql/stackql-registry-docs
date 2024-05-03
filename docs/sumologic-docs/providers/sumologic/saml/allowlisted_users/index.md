---
title: allowlisted_users
hide_title: false
hide_table_of_contents: false
keywords:
  - allowlisted_users
  - saml
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
<tr><td><b>Name</b></td><td><code>allowlisted_users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.saml.allowlisted_users" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="canManageSaml" /> | `boolean` | If the user can manage SAML Configurations. |
| <CopyableCode code="email" /> | `string` | Email of the user. |
| <CopyableCode code="firstName" /> | `string` | First name of the user. |
| <CopyableCode code="isActive" /> | `boolean` | Checks if the user is active. |
| <CopyableCode code="lastLogin" /> | `string` | Timestamp of the last login of the user. |
| <CopyableCode code="lastName" /> | `string` | Last name of the user. |
| <CopyableCode code="userId" /> | `string` | Unique identifier of the user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getAllowlistedUsers" /> | `SELECT` | <CopyableCode code="region" /> | Get a list of allowlisted users. |
| <CopyableCode code="createAllowlistedUser" /> | `INSERT` | <CopyableCode code="userId, region" /> | Allowlist a user from SAML lockdown allowing them to sign in using a password in addition to SAML. |
| <CopyableCode code="deleteAllowlistedUser" /> | `DELETE` | <CopyableCode code="userId, region" /> | Remove an allowlisted user requiring them to sign in using SAML. |
