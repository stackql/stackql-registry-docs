---
title: bucket_notifications
hide_title: false
hide_table_of_contents: false
keywords:
  - bucket_notifications
  - s3
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
<tr><td><b>Name</b></td><td><code>bucket_notifications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.s3.bucket_notifications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `CloudFunctionConfiguration` | `object` | Container for specifying the Lambda notification configuration. |
| `QueueConfiguration` | `object` | This data type is deprecated. Use &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_QueueConfiguration.html"&gt;QueueConfiguration&lt;/a&gt; for the same purposes. This data type specifies the configuration for publishing messages to an Amazon Simple Queue Service (Amazon SQS) queue when Amazon S3 detects specified events.  |
| `TopicConfiguration` | `object` | A container for specifying the configuration for publication of messages to an Amazon Simple Notification Service (Amazon SNS) topic when Amazon S3 detects specified events. This data type is deprecated. Use &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_TopicConfiguration.html"&gt;TopicConfiguration&lt;/a&gt; instead. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `bucket_notifications_Get` | `SELECT` | `notification` |  No longer used, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketNotificationConfiguration.html"&gt;GetBucketNotificationConfiguration&lt;/a&gt;. |
| `bucket_notifications_Put` | `EXEC` | `notification` |  No longer used, see the &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketNotificationConfiguration.html"&gt;PutBucketNotificationConfiguration&lt;/a&gt; operation. |
