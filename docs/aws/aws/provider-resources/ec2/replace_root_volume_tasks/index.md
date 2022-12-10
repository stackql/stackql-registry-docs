---
title: replace_root_volume_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - replace_root_volume_tasks
  - ec2
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replace_root_volume_tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.replace_root_volume_tasks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `replaceRootVolumeTaskId` | `string` | The ID of the root volume replacement task. |
| `startTime` | `string` | The time the task was started. |
| `tagSet` | `array` | The tags assigned to the task. |
| `taskState` | `string` | &lt;p&gt;The state of the task. The task can be in one of the following states:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;pending&lt;/code&gt; - the replacement volume is being created.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;in-progress&lt;/code&gt; - the original volume is being detached and the replacement volume is being attached.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;succeeded&lt;/code&gt; - the replacement volume has been successfully attached to the instance and the instance is available.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;failing&lt;/code&gt; - the replacement task is in the process of failing.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;failed&lt;/code&gt; - the replacement task has failed but the original root volume is still attached.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;failing-detached&lt;/code&gt; - the replacement task is in the process of failing. The instance might have no root volume attached.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;failed-detached&lt;/code&gt; - the replacement task has failed and the instance has no root volume attached.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `completeTime` | `string` | The time the task completed. |
| `instanceId` | `string` | The ID of the instance for which the root volume replacement task was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `replace_root_volume_tasks_Describe` | `SELECT` |  | Describes a root volume replacement task. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-restoring-volume.html#replace-root"&gt;Replace a root volume&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;. |
| `replace_root_volume_task_Create` | `INSERT` | `InstanceId` | &lt;p&gt;Creates a root volume replacement task for an Amazon EC2 instance. The root volume can either be restored to its initial launch state, or it can be restored using a specific snapshot.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-restoring-volume.html#replace-root"&gt;Replace a root volume&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
