---
title: dsc_compilation_job_stream
hide_title: false
hide_table_of_contents: false
keywords:
  - dsc_compilation_job_stream
  - automation
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
<tr><td><b>Name</b></td><td><code>dsc_compilation_job_stream</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.dsc_compilation_job_stream" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the id of the resource. |
| <CopyableCode code="properties" /> | `object` | Definition of the job stream. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, jobId, jobStreamId, resourceGroupName, subscriptionId" /> | Retrieve the job stream identified by job stream id. |
| <CopyableCode code="list_by_job" /> | `SELECT` | <CopyableCode code="automationAccountName, jobId, resourceGroupName, subscriptionId" /> | Retrieve all the job streams for the compilation Job. |
| <CopyableCode code="_list_by_job" /> | `EXEC` | <CopyableCode code="automationAccountName, jobId, resourceGroupName, subscriptionId" /> | Retrieve all the job streams for the compilation Job. |
