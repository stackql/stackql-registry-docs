---
title: licenses
hide_title: false
hide_table_of_contents: false
keywords:
  - licenses
  - licenses
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
<tr><td><b>Name</b></td><td><code>licenses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.licenses.licenses" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Uniquely identifies the resource |
| <CopyableCode code="name" /> | `string` | Name of the License.<br /> |
| <CopyableCode code="description" /> | `string` | Description of the License. May include the names of add-ons associated with<br />the License, if there are any.<br /> |
| <CopyableCode code="allocations_available" /> | `integer` | How many of these licenses are available to be allocated to a user. If this<br />value is "null" then there is no limit on the number of allocations allowed.<br /> |
| <CopyableCode code="current_value" /> | `integer` | How many of these Licenses are currently allocated to Users |
| <CopyableCode code="html_url" /> | `string` | HTML URL to access the License |
| <CopyableCode code="role_group" /> | `string` | Indicates whether this License is assignable to full or stakeholder Users |
| <CopyableCode code="self" /> | `string` | API URL to access the License |
| <CopyableCode code="summary" /> | `string` | Summary of the License |
| <CopyableCode code="type" /> | `string` | Type of object |
| <CopyableCode code="valid_roles" /> | `array` | The roles a User with this License can have |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_licenses" /> | `SELECT` |  |
| <CopyableCode code="_list_licenses" /> | `EXEC` |  |
