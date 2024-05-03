---
title: action_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - action_plans
  - deployment_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>action_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.deployment_admin.action_plans" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="eTag" /> | `string` | Entity tag of the resource |
| <CopyableCode code="location" /> | `string` | Location of the resource. |
| <CopyableCode code="properties" /> | `object` | Action Plan Properties |
| <CopyableCode code="type" /> | `string` | Type of Resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="planId, subscriptionId" /> | Gets the specified action plan |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets the list of action plans |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Gets the list of action plans |
