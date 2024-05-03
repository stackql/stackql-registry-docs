---
title: collectors
hide_title: false
hide_table_of_contents: false
keywords:
  - collectors
  - ingest_budgets
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
<tr><td><b>Name</b></td><td><code>collectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.ingest_budgets.collectors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique identifier for the Collector. |
| <CopyableCode code="name" /> | `string` | The name of the Collector. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getAssignedCollectors" /> | `SELECT` | <CopyableCode code="id, region" /> | Get a list of Collectors assigned to an ingest budget. The response is paginated with a default limit of 100 Collectors per page. |
| <CopyableCode code="removeCollectorFromBudget" /> | `DELETE` | <CopyableCode code="collectorId, id, region" /> | Remove Collector from a budget. |
| <CopyableCode code="assignCollectorToBudget" /> | `EXEC` | <CopyableCode code="collectorId, id, region" /> | Assign a Collector to a budget. |
