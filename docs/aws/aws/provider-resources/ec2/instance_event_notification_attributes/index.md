---
title: instance_event_notification_attributes
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_event_notification_attributes
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
<tr><td><b>Name</b></td><td><code>instance_event_notification_attributes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.instance_event_notification_attributes</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `instance_event_notification_attributes_Describe` | `SELECT` |  | Describes the tag keys that are registered to appear in scheduled event notifications for resources in the current Region. |
| `instance_event_notification_attributes_Deregister` | `EXEC` |  | Deregisters tag keys to prevent tags that have the specified tag keys from being included in scheduled event notifications for resources in the Region. |
| `instance_event_notification_attributes_Register` | `EXEC` |  | &lt;p&gt;Registers a set of tag keys to include in scheduled event notifications for your resources. &lt;/p&gt; &lt;p&gt;To remove tags, use &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeregisterInstanceEventNotificationAttributes.html"&gt;DeregisterInstanceEventNotificationAttributes&lt;/a&gt;.&lt;/p&gt; |
