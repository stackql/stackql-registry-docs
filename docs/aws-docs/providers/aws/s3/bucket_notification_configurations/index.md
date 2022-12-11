---
title: bucket_notification_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - bucket_notification_configurations
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
<tr><td><b>Name</b></td><td><code>bucket_notification_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.s3.bucket_notification_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `QueueConfiguration` | `array` | The Amazon Simple Queue Service queues to publish messages to and the events for which to publish messages. |
| `TopicConfiguration` | `array` | The topic to which notifications are sent and the events for which notifications are generated. |
| `CloudFunctionConfiguration` | `array` | Describes the Lambda functions to invoke and the events for which to invoke them. |
| `EventBridgeConfiguration` | `object` | A container for specifying the configuration for Amazon EventBridge. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `bucket_notification_configurations_Get` | `SELECT` | `notification` | &lt;p&gt;Returns the notification configuration of a bucket.&lt;/p&gt; &lt;p&gt;If notifications are not enabled on the bucket, the action returns an empty &lt;code&gt;NotificationConfiguration&lt;/code&gt; element.&lt;/p&gt; &lt;p&gt;By default, you must be the bucket owner to read the notification configuration of a bucket. However, the bucket owner can use a bucket policy to grant permission to other users to read this configuration with the &lt;code&gt;s3:GetBucketNotification&lt;/code&gt; permission.&lt;/p&gt; &lt;p&gt;For more information about setting and reading the notification configuration on a bucket, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html"&gt;Setting Up Notification of Bucket Events&lt;/a&gt;. For more information about bucket policies, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html"&gt;Using Bucket Policies&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The following action is related to &lt;code&gt;GetBucketNotification&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketNotification.html"&gt;PutBucketNotification&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `bucket_notification_configurations_Put` | `EXEC` | `notification` | &lt;p&gt;Enables notifications of specified events for a bucket. For more information about event notifications, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html"&gt;Configuring Event Notifications&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Using this API, you can replace an existing notification configuration. The configuration is an XML file that defines the event types that you want Amazon S3 to publish and the destination where you want Amazon S3 to publish an event notification when it detects an event of the specified type.&lt;/p&gt; &lt;p&gt;By default, your bucket has no event notifications configured. That is, the notification configuration will be an empty &lt;code&gt;NotificationConfiguration&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;&lt;NotificationConfiguration&gt;&lt;/code&gt; &lt;/p&gt; &lt;p&gt; &lt;code&gt;&lt;/NotificationConfiguration&gt;&lt;/code&gt; &lt;/p&gt; &lt;p&gt;This action replaces the existing notification configuration with the configuration you include in the request body.&lt;/p&gt; &lt;p&gt;After Amazon S3 receives this request, it first verifies that any Amazon Simple Notification Service (Amazon SNS) or Amazon Simple Queue Service (Amazon SQS) destination exists, and that the bucket owner has permission to publish to it by sending a test notification. In the case of Lambda destinations, Amazon S3 verifies that the Lambda function permissions grant Amazon S3 permission to invoke the function from the Amazon S3 bucket. For more information, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html"&gt;Configuring Notifications for Amazon S3 Events&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can disable notifications by adding the empty NotificationConfiguration element.&lt;/p&gt; &lt;p&gt;For more information about the number of event notification configurations that you can create per bucket, see &lt;a href="https://docs.aws.amazon.com/general/latest/gr/s3.html#limits_s3"&gt;Amazon S3 service quotas&lt;/a&gt; in &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;By default, only the bucket owner can configure notifications on a bucket. However, bucket owners can use a bucket policy to grant permission to other users to set this configuration with &lt;code&gt;s3:PutBucketNotification&lt;/code&gt; permission.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The PUT notification is an atomic operation. For example, suppose your notification configuration includes SNS topic, SQS queue, and Lambda function configurations. When you send a PUT request with this configuration, Amazon S3 sends test messages to your SNS topic. If the message fails, the entire PUT action will fail, and Amazon S3 will not add the configuration to your bucket.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Responses&lt;/b&gt; &lt;/p&gt; &lt;p&gt;If the configuration in the request body includes only one &lt;code&gt;TopicConfiguration&lt;/code&gt; specifying only the &lt;code&gt;s3:ReducedRedundancyLostObject&lt;/code&gt; event type, the response will also include the &lt;code&gt;x-amz-sns-test-message-id&lt;/code&gt; header containing the message ID of the test notification sent to the topic.&lt;/p&gt; &lt;p&gt;The following action is related to &lt;code&gt;PutBucketNotificationConfiguration&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketNotificationConfiguration.html"&gt;GetBucketNotificationConfiguration&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
