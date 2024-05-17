---
title: bundle_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - bundle_tasks
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
<tr><td><b>Name</b></td><td><code>bundle_tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.bundle_tasks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="bundleId" /> | `string` | The ID of the bundle task. |
| <CopyableCode code="error" /> | `object` | Describes an error for &lt;a&gt;BundleInstance&lt;/a&gt;. |
| <CopyableCode code="instanceId" /> | `string` | The ID of the instance associated with this bundle task. |
| <CopyableCode code="progress" /> | `string` | The level of task completion, as a percent (for example, 20%). |
| <CopyableCode code="startTime" /> | `string` | The time this task started. |
| <CopyableCode code="state" /> | `string` | The state of the task. |
| <CopyableCode code="storage" /> | `object` | Describes the storage location for an instance store-backed AMI. |
| <CopyableCode code="updateTime" /> | `string` | The time of the most recent update for the task. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="bundle_tasks_Describe" /> | `SELECT` | <CopyableCode code="region" /> | &lt;p&gt;Describes the specified bundle tasks or all of your bundle tasks.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Completed bundle tasks are listed for only a limited time. If your bundle task is no longer in the list, you can still register an AMI from it. Just use &lt;code&gt;RegisterImage&lt;/code&gt; with the Amazon S3 bucket name and image manifest name you provided to the bundle task.&lt;/p&gt; &lt;/note&gt; |
| <CopyableCode code="bundle_task_Cancel" /> | `EXEC` | <CopyableCode code="BundleId, region" /> | Cancels a bundling operation for an instance store-backed Windows instance. |
