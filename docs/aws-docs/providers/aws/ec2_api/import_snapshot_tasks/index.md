---
title: import_snapshot_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - import_snapshot_tasks
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
<tr><td><b>Name</b></td><td><code>import_snapshot_tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.import_snapshot_tasks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | A description of the import snapshot task. |
| <CopyableCode code="importTaskId" /> | `string` | The ID of the import snapshot task. |
| <CopyableCode code="snapshotTaskDetail" /> | `object` | Details about the import snapshot task. |
| <CopyableCode code="tagSet" /> | `array` | The tags for the import snapshot task. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="import_snapshot_tasks_Describe" /> | `SELECT` | <CopyableCode code="region" /> |
