---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - data_box_edge
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
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_box_edge.jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The name of the object. |
| <CopyableCode code="endTime" /> | `string` | The UTC date and time at which the job completed. |
| <CopyableCode code="error" /> | `object` | The job error information containing the list of job errors. |
| <CopyableCode code="percentComplete" /> | `integer` | The percentage of the job that is complete. |
| <CopyableCode code="properties" /> | `object` | The properties for the job. |
| <CopyableCode code="startTime" /> | `string` | The UTC date and time at which the job started. |
| <CopyableCode code="status" /> | `string` | The current status of the job. |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, name, resourceGroupName, subscriptionId" /> |
