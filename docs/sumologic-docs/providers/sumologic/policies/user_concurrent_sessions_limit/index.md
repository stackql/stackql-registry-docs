---
title: user_concurrent_sessions_limit
hide_title: false
hide_table_of_contents: false
keywords:
  - user_concurrent_sessions_limit
  - policies
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
<tr><td><b>Name</b></td><td><code>user_concurrent_sessions_limit</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.policies.user_concurrent_sessions_limit" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="enabled" /> | `boolean` | Whether the User Concurrent Sessions Limit policy is enabled. |
| <CopyableCode code="maxConcurrentSessions" /> | `integer` | Maximum number of concurrent sessions a user may have. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getUserConcurrentSessionsLimitPolicy" /> | `SELECT` | <CopyableCode code="region" /> | Get the User Concurrent Sessions Limit policy. When enabled, the number of concurrent sessions a user may have is limited to the value entered. If a user exceeds the allowed number of sessions, the user's oldest session will be logged out to accommodate the new one. Disabling this policy means a user may have an unlimited number of concurrent sessions. [Learn More](https://help.sumologic.com/Manage/Security/Set_a_Limit_for_User_Concurrent_Sessions) |
| <CopyableCode code="setUserConcurrentSessionsLimitPolicy" /> | `EXEC` | <CopyableCode code="data__enabled, region" /> | Set the User Concurrent Sessions Limit policy. When enabled, the number of concurrent sessions a user may have is limited to the value entered. If a user exceeds the allowed number of sessions, the user's oldest session will be logged out to accommodate the new one. Disabling this policy means a user may have an unlimited number of concurrent sessions. [Learn More](https://help.sumologic.com/Manage/Security/Set_a_Limit_for_User_Concurrent_Sessions) |
