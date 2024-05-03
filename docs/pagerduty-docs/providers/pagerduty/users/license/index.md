---
title: license
hide_title: false
hide_table_of_contents: false
keywords:
  - license
  - users
  - pagerduty    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, manage, and integrate PagerDuty resources using SQL
custom_edit_url: null
image: /img/providers/pagerduty/stackql-pagerduty-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>license</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.users.license" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Uniquely identifies the resource |
| <CopyableCode code="name" /> | `string` | Name of the License.<br /> |
| <CopyableCode code="description" /> | `string` | Description of the License. May include the names of add-ons associated with<br />the License, if there are any.<br /> |
| <CopyableCode code="html_url" /> | `string` | HTML URL to access the License |
| <CopyableCode code="role_group" /> | `string` | Indicates whether this License is assignable to full or stakeholder Users |
| <CopyableCode code="self" /> | `string` | API URL to access the License |
| <CopyableCode code="summary" /> | `string` | Summary of the License |
| <CopyableCode code="type" /> | `string` | Type of object |
| <CopyableCode code="valid_roles" /> | `array` | The roles a User with this License can have |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_user_license" /> | `SELECT` | <CopyableCode code="id" /> |
| <CopyableCode code="_get_user_license" /> | `EXEC` | <CopyableCode code="id" /> |
