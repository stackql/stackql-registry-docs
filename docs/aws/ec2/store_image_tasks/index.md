---
title: store_image_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - store_image_tasks
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
<tr><td><b>Name</b></td><td><code>store_image_tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.store_image_tasks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `amiId` | `string` | The ID of the AMI that is being stored. |
| `bucket` | `string` | The name of the Amazon S3 bucket that contains the stored AMI object. |
| `progressPercentage` | `integer` | The progress of the task as a percentage. |
| `s3objectKey` | `string` | The name of the stored AMI object in the bucket. |
| `storeTaskFailureReason` | `string` | If the tasks fails, the reason for the failure is returned. If the task succeeds, &lt;code&gt;null&lt;/code&gt; is returned. |
| `storeTaskState` | `string` | The state of the store task (&lt;code&gt;InProgress&lt;/code&gt;, &lt;code&gt;Completed&lt;/code&gt;, or &lt;code&gt;Failed&lt;/code&gt;). |
| `taskStartTime` | `string` | The time the task started. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `store_image_tasks_Describe` | `SELECT` |  | &lt;p&gt;Describes the progress of the AMI store tasks. You can describe the store tasks for specified AMIs. If you don't specify the AMIs, you get a paginated list of store tasks from the last 31 days.&lt;/p&gt; &lt;p&gt;For each AMI task, the response indicates if the task is &lt;code&gt;InProgress&lt;/code&gt;, &lt;code&gt;Completed&lt;/code&gt;, or &lt;code&gt;Failed&lt;/code&gt;. For tasks &lt;code&gt;InProgress&lt;/code&gt;, the response shows the estimated progress as a percentage.&lt;/p&gt; &lt;p&gt;Tasks are listed in reverse chronological order. Currently, only tasks from the past 31 days can be viewed.&lt;/p&gt; &lt;p&gt;To use this API, you must have the required permissions. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-store-restore.html#ami-s3-permissions"&gt;Permissions for storing and restoring AMIs using Amazon S3&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-store-restore.html"&gt;Store and restore an AMI using Amazon S3&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| `store_image_task_Create` | `INSERT` | `Bucket, ImageId` | &lt;p&gt;Stores an AMI as a single object in an Amazon S3 bucket.&lt;/p&gt; &lt;p&gt;To use this API, you must have the required permissions. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-store-restore.html#ami-s3-permissions"&gt;Permissions for storing and restoring AMIs using Amazon S3&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-store-restore.html"&gt;Store and restore an AMI using Amazon S3&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
