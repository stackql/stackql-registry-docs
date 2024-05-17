---
title: placement_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - placement_groups
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
<tr><td><b>Name</b></td><td><code>placement_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.placement_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="groupArn" /> | `string` | The Amazon Resource Name (ARN) of the placement group. |
| <CopyableCode code="groupId" /> | `string` | The ID of the placement group. |
| <CopyableCode code="groupName" /> | `string` | The name of the placement group. |
| <CopyableCode code="partitionCount" /> | `integer` | The number of partitions. Valid only if &lt;b&gt;strategy&lt;/b&gt; is set to &lt;code&gt;partition&lt;/code&gt;. |
| <CopyableCode code="state" /> | `string` | The state of the placement group. |
| <CopyableCode code="strategy" /> | `string` | The placement strategy. |
| <CopyableCode code="tagSet" /> | `array` | Any tags applied to the placement group. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="placement_groups_Describe" /> | `SELECT` | <CopyableCode code="region" /> | Describes the specified placement groups or all of your placement groups. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html"&gt;Placement groups&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;. |
| <CopyableCode code="placement_group_Create" /> | `INSERT` | <CopyableCode code="region" /> | &lt;p&gt;Creates a placement group in which to launch instances. The strategy of the placement group determines how the instances are organized within the group. &lt;/p&gt; &lt;p&gt;A &lt;code&gt;cluster&lt;/code&gt; placement group is a logical grouping of instances within a single Availability Zone that benefit from low network latency, high network throughput. A &lt;code&gt;spread&lt;/code&gt; placement group places instances on distinct hardware. A &lt;code&gt;partition&lt;/code&gt; placement group places groups of instances in different partitions, where instances in one partition do not share the same hardware with instances in another partition.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html"&gt;Placement groups&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt; |
| <CopyableCode code="placement_group_Delete" /> | `DELETE` | <CopyableCode code="GroupName, region" /> | Deletes the specified placement group. You must terminate all instances in the placement group before you can delete the placement group. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html"&gt;Placement groups&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;. |
