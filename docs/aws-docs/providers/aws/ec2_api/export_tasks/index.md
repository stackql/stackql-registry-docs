---
title: export_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - export_tasks
  - ec2_api
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>export_tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.export_tasks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | A description of the resource being exported. |
| <CopyableCode code="exportTaskId" /> | `string` | The ID of the export task. |
| <CopyableCode code="exportToS3" /> | `object` | Describes the format and location for the export task. |
| <CopyableCode code="instanceExport" /> | `object` | Describes an instance to export. |
| <CopyableCode code="state" /> | `string` | The state of the export task. |
| <CopyableCode code="statusMessage" /> | `string` | The status message related to the export task. |
| <CopyableCode code="tagSet" /> | `array` | The tags for the export task. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="export_tasks_Describe" /> | `SELECT` | <CopyableCode code="region" /> | Describes the specified export instance tasks or all of your export instance tasks. |
| <CopyableCode code="export_task_Cancel" /> | `EXEC` | <CopyableCode code="ExportTaskId, region" /> | Cancels an active export task. The request removes all artifacts of the export, including any partially-created Amazon S3 objects. If the export task is complete or is in the process of transferring the final disk image, the command fails and returns an error. |
