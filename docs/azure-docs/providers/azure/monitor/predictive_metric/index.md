---
title: predictive_metric
hide_title: false
hide_table_of_contents: false
keywords:
  - predictive_metric
  - monitor
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
<tr><td><b>Name</b></td><td><code>predictive_metric</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.predictive_metric" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="data" /> | `array` | the value of the collection. |
| <CopyableCode code="interval" /> | `string` | The interval (window size) for which the metric data was returned in.  This may be adjusted in the future and returned back from what was originally requested.  This is not present if a metadata request was made. |
| <CopyableCode code="metricName" /> | `string` | The metrics being queried |
| <CopyableCode code="targetResourceId" /> | `string` | resource of the predictive metric. |
| <CopyableCode code="timespan" /> | `string` | The timespan for which the data was retrieved. Its value consists of two datetimes concatenated, separated by '/'.  This may be adjusted in the future and returned back from what was originally requested. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="aggregation, autoscaleSettingName, resourceGroupName, subscriptionId" /> |
