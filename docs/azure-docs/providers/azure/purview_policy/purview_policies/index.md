---
title: purview_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - purview_policies
  - purview_policy
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>purview_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview_policy.purview_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="decisionRules" /> | `array` | Array of decision rules for the policy |
| <CopyableCode code="etag" /> | `string` | The etag version of a policy |
| <CopyableCode code="expiryTime" /> | `string` | The timestamp of the expiry time of the policy (UTC). |
| <CopyableCode code="kind" /> | `string` | The policy kind |
| <CopyableCode code="members" /> | `object` | Policy member |
| <CopyableCode code="requestor" /> | `string` | The AAD member who requested the policy |
| <CopyableCode code="scopes" /> | `array` | Array of scopes where the policy is published |
| <CopyableCode code="source" /> | `string` | The policy source |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> |
