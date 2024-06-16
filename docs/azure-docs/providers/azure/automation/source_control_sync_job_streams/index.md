---
title: source_control_sync_job_streams
hide_title: false
hide_table_of_contents: false
keywords:
  - source_control_sync_job_streams
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
<tr><td><b>Name</b></td><td><code>source_control_sync_job_streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.source_control_sync_job_streams" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource id. |
| <CopyableCode code="properties" /> | `object` | Definition of source control sync job stream by id properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, sourceControlName, sourceControlSyncJobId, streamId, subscriptionId" /> | Retrieve a sync job stream identified by stream id. |
| <CopyableCode code="list_by_sync_job" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, sourceControlName, sourceControlSyncJobId, subscriptionId" /> | Retrieve a list of sync job streams identified by sync job id. |
