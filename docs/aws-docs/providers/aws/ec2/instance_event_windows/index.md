---
title: instance_event_windows
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_event_windows
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
<tr><td><b>Name</b></td><td><code>instance_event_windows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.instance_event_windows</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the event window. |
| `instanceEventWindowId` | `string` | The ID of the event window. |
| `state` | `string` | The current state of the event window. |
| `tagSet` | `array` | The instance tags associated with the event window. |
| `timeRangeSet` | `array` | One or more time ranges defined for the event window. |
| `associationTarget` | `object` | One or more targets associated with the event window. |
| `cronExpression` | `string` | The cron expression defined for the event window. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `instance_event_windows_Describe` | `SELECT` |  | &lt;p&gt;Describes the specified event windows or all event windows.&lt;/p&gt; &lt;p&gt;If you specify event window IDs, the output includes information for only the specified event windows. If you specify filters, the output includes information for only those event windows that meet the filter criteria. If you do not specify event windows IDs or filters, the output includes information for all event windows, which can affect performance. We recommend that you use pagination to ensure that the operation returns quickly and successfully. &lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/event-windows.html"&gt;Define event windows for scheduled events&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt; |
| `instance_event_window_Create` | `INSERT` |  | &lt;p&gt;Creates an event window in which scheduled events for the associated Amazon EC2 instances can run.&lt;/p&gt; &lt;p&gt;You can define either a set of time ranges or a cron expression when creating the event window, but not both. All event window times are in UTC.&lt;/p&gt; &lt;p&gt;You can create up to 200 event windows per Amazon Web Services Region.&lt;/p&gt; &lt;p&gt;When you create the event window, targets (instance IDs, Dedicated Host IDs, or tags) are not yet associated with it. To ensure that the event window can be used, you must associate one or more targets with it by using the &lt;a&gt;AssociateInstanceEventWindow&lt;/a&gt; API.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Event windows are applicable only for scheduled events that stop, reboot, or terminate instances.&lt;/p&gt; &lt;p&gt;Event windows are &lt;i&gt;not&lt;/i&gt; applicable for:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Expedited scheduled events and network maintenance events. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Unscheduled maintenance such as AutoRecovery and unplanned reboots.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/important&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/event-windows.html"&gt;Define event windows for scheduled events&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt; |
| `instance_event_window_Delete` | `DELETE` | `InstanceEventWindowId` | &lt;p&gt;Deletes the specified event window.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/event-windows.html"&gt;Define event windows for scheduled events&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt; |
| `instance_event_window_Associate` | `EXEC` | `AssociationTarget, InstanceEventWindowId` | &lt;p&gt;Associates one or more targets with an event window. Only one type of target (instance IDs, Dedicated Host IDs, or tags) can be specified with an event window.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/event-windows.html"&gt;Define event windows for scheduled events&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt; |
| `instance_event_window_Disassociate` | `EXEC` | `AssociationTarget, InstanceEventWindowId` | &lt;p&gt;Disassociates one or more targets from an event window.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/event-windows.html"&gt;Define event windows for scheduled events&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt; |
| `instance_event_window_Modify` | `EXEC` | `InstanceEventWindowId` | &lt;p&gt;Modifies the specified event window.&lt;/p&gt; &lt;p&gt;You can define either a set of time ranges or a cron expression when modifying the event window, but not both.&lt;/p&gt; &lt;p&gt;To modify the targets associated with the event window, use the &lt;a&gt;AssociateInstanceEventWindow&lt;/a&gt; and &lt;a&gt;DisassociateInstanceEventWindow&lt;/a&gt; API.&lt;/p&gt; &lt;p&gt;If Amazon Web Services has already scheduled an event, modifying an event window won't change the time of the scheduled event.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/event-windows.html"&gt;Define event windows for scheduled events&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt; |
