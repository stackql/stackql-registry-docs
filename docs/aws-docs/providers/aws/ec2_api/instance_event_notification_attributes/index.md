---
title: instance_event_notification_attributes
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_event_notification_attributes
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
<tr><td><b>Name</b></td><td><code>instance_event_notification_attributes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.instance_event_notification_attributes" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="instance_event_notification_attributes_Describe" /> | `SELECT` | <CopyableCode code="region" /> | Describes the tag keys that are registered to appear in scheduled event notifications for resources in the current Region. |
| <CopyableCode code="instance_event_notification_attributes_Deregister" /> | `EXEC` | <CopyableCode code="region" /> | Deregisters tag keys to prevent tags that have the specified tag keys from being included in scheduled event notifications for resources in the Region. |
| <CopyableCode code="instance_event_notification_attributes_Register" /> | `EXEC` | <CopyableCode code="region" /> | &lt;p&gt;Registers a set of tag keys to include in scheduled event notifications for your resources. &lt;/p&gt; &lt;p&gt;To remove tags, use &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeregisterInstanceEventNotificationAttributes.html"&gt;DeregisterInstanceEventNotificationAttributes&lt;/a&gt;.&lt;/p&gt; |
