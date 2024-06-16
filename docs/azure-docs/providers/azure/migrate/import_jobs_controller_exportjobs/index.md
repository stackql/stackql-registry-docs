---
title: import_jobs_controller_exportjobs
hide_title: false
hide_table_of_contents: false
keywords:
  - import_jobs_controller_exportjobs
  - migrate
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
<tr><td><b>Name</b></td><td><code>import_jobs_controller_exportjobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.import_jobs_controller_exportjobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the relative ARM name to get job. |
| <CopyableCode code="name" /> | `string` | Gets or sets the Job ID. |
| <CopyableCode code="displayName" /> | `string` | Gets or sets the Display name. |
| <CopyableCode code="endTime" /> | `string` | Gets or sets the Job end time. |
| <CopyableCode code="properties" /> | `object` |  Export Imported Machines JobEntity Properties  |
| <CopyableCode code="startTime" /> | `string` | Gets or sets the Job start time. |
| <CopyableCode code="status" /> | `string` | Gets or sets the Job status. |
| <CopyableCode code="type" /> | `string` | Type name for export job. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> |
