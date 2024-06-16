---
title: usage_aggregates
hide_title: false
hide_table_of_contents: false
keywords:
  - usage_aggregates
  - commerce
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>usage_aggregates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.commerce.usage_aggregates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique Id for the usage aggregate. |
| <CopyableCode code="name" /> | `string` | Name of the usage aggregate. |
| <CopyableCode code="properties" /> | `object` | Describes a sample of the usageAggregation. |
| <CopyableCode code="type" /> | `string` | Type of the resource being returned. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="reportedEndTime, reportedStartTime, subscriptionId" /> |
