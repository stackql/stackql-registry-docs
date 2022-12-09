---
title: vpc_endpoint_connection_notifications
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_endpoint_connection_notifications
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
<tr><td><b>Name</b></td><td><code>vpc_endpoint_connection_notifications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.vpc_endpoint_connection_notifications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `connectionNotificationArn` | `string` | The ARN of the SNS topic for the notification. |
| `connectionNotificationId` | `string` | The ID of the notification. |
| `connectionNotificationState` | `string` | The state of the notification. |
| `connectionNotificationType` | `string` | The type of notification. |
| `serviceId` | `string` | The ID of the endpoint service. |
| `vpcEndpointId` | `string` | The ID of the VPC endpoint. |
| `connectionEvents` | `array` | The events for the notification. Valid values are &lt;code&gt;Accept&lt;/code&gt;, &lt;code&gt;Connect&lt;/code&gt;, &lt;code&gt;Delete&lt;/code&gt;, and &lt;code&gt;Reject&lt;/code&gt;. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `vpc_endpoint_connection_notifications_Describe` | `SELECT` |  | Describes the connection notifications for VPC endpoints and VPC endpoint services. |
| `vpc_endpoint_connection_notification_Create` | `INSERT` | `ConnectionEvents, ConnectionNotificationArn` | &lt;p&gt;Creates a connection notification for a specified VPC endpoint or VPC endpoint service. A connection notification notifies you of specific endpoint events. You must create an SNS topic to receive notifications. For more information, see &lt;a href="https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html"&gt;Create a Topic&lt;/a&gt; in the &lt;i&gt;Amazon Simple Notification Service Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can create a connection notification for interface endpoints only.&lt;/p&gt; |
| `vpc_endpoint_connection_notifications_Delete` | `DELETE` | `ConnectionNotificationId` | Deletes one or more VPC endpoint connection notifications. |
| `vpc_endpoint_connection_notification_Modify` | `EXEC` | `ConnectionNotificationId` | Modifies a connection notification for VPC endpoint or VPC endpoint service. You can change the SNS topic for the notification, or the events for which to be notified.  |
