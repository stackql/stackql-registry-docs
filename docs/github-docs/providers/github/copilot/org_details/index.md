---
title: org_details
hide_title: false
hide_table_of_contents: false
keywords:
  - org_details
  - copilot
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>org_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.copilot.org_details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="public_code_suggestions" /> | `string` | The organization policy for allowing or disallowing Copilot to make suggestions that match public code. |
| <CopyableCode code="seat_breakdown" /> | `object` | The breakdown of Copilot for Business seats for the organization. |
| <CopyableCode code="seat_management_setting" /> | `string` | The mode of assigning new seats. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_copilot_organization_details" /> | `SELECT` | <CopyableCode code="org" /> |
