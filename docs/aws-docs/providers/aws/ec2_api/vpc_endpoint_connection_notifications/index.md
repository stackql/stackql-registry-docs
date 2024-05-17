---
title: vpc_endpoint_connection_notifications
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_endpoint_connection_notifications
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
<tr><td><b>Name</b></td><td><code>vpc_endpoint_connection_notifications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.vpc_endpoint_connection_notifications" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="connectionEvents" /> | `array` | The events for the notification. Valid values are &lt;code&gt;Accept&lt;/code&gt;, &lt;code&gt;Connect&lt;/code&gt;, &lt;code&gt;Delete&lt;/code&gt;, and &lt;code&gt;Reject&lt;/code&gt;. |
| <CopyableCode code="connectionNotificationArn" /> | `string` | The ARN of the SNS topic for the notification. |
| <CopyableCode code="connectionNotificationId" /> | `string` | The ID of the notification. |
| <CopyableCode code="connectionNotificationState" /> | `string` | The state of the notification. |
| <CopyableCode code="connectionNotificationType" /> | `string` | The type of notification. |
| <CopyableCode code="serviceId" /> | `string` | The ID of the endpoint service. |
| <CopyableCode code="vpcEndpointId" /> | `string` | The ID of the VPC endpoint. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="vpc_endpoint_connection_notifications_Describe" /> | `SELECT` | <CopyableCode code="region" /> | Describes the connection notifications for VPC endpoints and VPC endpoint services. |
| <CopyableCode code="vpc_endpoint_connection_notification_Create" /> | `INSERT` | <CopyableCode code="ConnectionEvents, ConnectionNotificationArn, region" /> | &lt;p&gt;Creates a connection notification for a specified VPC endpoint or VPC endpoint service. A connection notification notifies you of specific endpoint events. You must create an SNS topic to receive notifications. For more information, see &lt;a href="https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html"&gt;Create a Topic&lt;/a&gt; in the &lt;i&gt;Amazon Simple Notification Service Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can create a connection notification for interface endpoints only.&lt;/p&gt; |
| <CopyableCode code="vpc_endpoint_connection_notifications_Delete" /> | `DELETE` | <CopyableCode code="ConnectionNotificationId, region" /> | Deletes one or more VPC endpoint connection notifications. |
| <CopyableCode code="vpc_endpoint_connection_notification_Modify" /> | `EXEC` | <CopyableCode code="ConnectionNotificationId, region" /> | Modifies a connection notification for VPC endpoint or VPC endpoint service. You can change the SNS topic for the notification, or the events for which to be notified.  |
