---
title: test_job_streams
hide_title: false
hide_table_of_contents: false
keywords:
  - test_job_streams
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
<tr><td><b>Name</b></td><td><code>test_job_streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.test_job_streams" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the id of the resource. |
| <CopyableCode code="properties" /> | `object` | Definition of the job stream. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, jobStreamId, resourceGroupName, runbookName, subscriptionId" /> | Retrieve a test job stream of the test job identified by runbook name and stream id. |
| <CopyableCode code="list_by_test_job" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, runbookName, subscriptionId" /> | Retrieve a list of test job streams identified by runbook name. |
