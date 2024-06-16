---
title: rule_sets_resource_usage
hide_title: false
hide_table_of_contents: false
keywords:
  - rule_sets_resource_usage
  - cdn
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
<tr><td><b>Name</b></td><td><code>rule_sets_resource_usage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.rule_sets_resource_usage" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource identifier. |
| <CopyableCode code="name" /> | `object` | The usage names. |
| <CopyableCode code="currentValue" /> | `integer` | The current value of the usage. |
| <CopyableCode code="limit" /> | `integer` | The limit of usage. |
| <CopyableCode code="unit" /> | `string` | An enum describing the unit of measurement. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="profileName, resourceGroupName, ruleSetName, subscriptionId" /> |
