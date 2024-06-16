---
title: applications_allowed_upgrade_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - applications_allowed_upgrade_plans
  - managed_applications
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
<tr><td><b>Name</b></td><td><code>applications_allowed_upgrade_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_applications.applications_allowed_upgrade_plans" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The plan name. |
| <CopyableCode code="product" /> | `string` | The product code. |
| <CopyableCode code="promotionCode" /> | `string` | The promotion code. |
| <CopyableCode code="publisher" /> | `string` | The publisher ID. |
| <CopyableCode code="version" /> | `string` | The plan's version. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="applicationName, resourceGroupName, subscriptionId" /> |
