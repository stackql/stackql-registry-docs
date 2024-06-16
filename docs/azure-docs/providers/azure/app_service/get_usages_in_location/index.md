---
title: get_usages_in_location
hide_title: false
hide_table_of_contents: false
keywords:
  - get_usages_in_location
  - app_service
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
<tr><td><b>Name</b></td><td><code>get_usages_in_location</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.get_usages_in_location" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `object` | Localizable string object containing the name and a localized value. |
| <CopyableCode code="currentValue" /> | `integer` | The current value of the resource counter. |
| <CopyableCode code="limit" /> | `integer` | The resource limit. |
| <CopyableCode code="nextResetTime" /> | `string` | Next reset time for the resource counter. |
| <CopyableCode code="unit" /> | `string` | Units of measurement for the quota resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> |
