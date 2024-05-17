---
title: hosts
hide_title: false
hide_table_of_contents: false
keywords:
  - hosts
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
<tr><td><b>Name</b></td><td><code>hosts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.hosts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="allocationTime" /> | `string` | The time that the Dedicated Host was allocated. |
| <CopyableCode code="allowsMultipleInstanceTypes" /> | `string` | Indicates whether the Dedicated Host supports multiple instance types of the same instance family. If the value is &lt;code&gt;on&lt;/code&gt;, the Dedicated Host supports multiple instance types in the instance family. If the value is &lt;code&gt;off&lt;/code&gt;, the Dedicated Host supports a single instance type only. |
| <CopyableCode code="autoPlacement" /> | `string` | Whether auto-placement is on or off. |
| <CopyableCode code="availabilityZone" /> | `string` | The Availability Zone of the Dedicated Host. |
| <CopyableCode code="availabilityZoneId" /> | `string` | The ID of the Availability Zone in which the Dedicated Host is allocated. |
| <CopyableCode code="availableCapacity" /> | `object` | The capacity information for instances that can be launched onto the Dedicated Host.  |
| <CopyableCode code="clientToken" /> | `string` | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html"&gt;Ensuring Idempotency&lt;/a&gt;. |
| <CopyableCode code="hostId" /> | `string` | The ID of the Dedicated Host. |
| <CopyableCode code="hostProperties" /> | `object` | Describes the properties of a Dedicated Host. |
| <CopyableCode code="hostRecovery" /> | `string` | Indicates whether host recovery is enabled or disabled for the Dedicated Host. |
| <CopyableCode code="hostReservationId" /> | `string` | The reservation ID of the Dedicated Host. This returns a &lt;code&gt;null&lt;/code&gt; response if the Dedicated Host doesn't have an associated reservation. |
| <CopyableCode code="instances" /> | `array` | The IDs and instance type that are currently running on the Dedicated Host. |
| <CopyableCode code="memberOfServiceLinkedResourceGroup" /> | `boolean` | Indicates whether the Dedicated Host is in a host resource group. If &lt;b&gt;memberOfServiceLinkedResourceGroup&lt;/b&gt; is &lt;code&gt;true&lt;/code&gt;, the host is in a host resource group; otherwise, it is not. |
| <CopyableCode code="outpostArn" /> | `string` | The Amazon Resource Name (ARN) of the Amazon Web Services Outpost on which the Dedicated Host is allocated. |
| <CopyableCode code="ownerId" /> | `string` | The ID of the Amazon Web Services account that owns the Dedicated Host. |
| <CopyableCode code="releaseTime" /> | `string` | The time that the Dedicated Host was released. |
| <CopyableCode code="state" /> | `string` | The Dedicated Host's state. |
| <CopyableCode code="tagSet" /> | `array` | Any tags assigned to the Dedicated Host. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="hosts_Describe" /> | `SELECT` | <CopyableCode code="region" /> | &lt;p&gt;Describes the specified Dedicated Hosts or all your Dedicated Hosts.&lt;/p&gt; &lt;p&gt;The results describe only the Dedicated Hosts in the Region you're currently using. All listed instances consume capacity on your Dedicated Host. Dedicated Hosts that have recently been released are listed with the state &lt;code&gt;released&lt;/code&gt;.&lt;/p&gt; |
| <CopyableCode code="hosts_Allocate" /> | `EXEC` | <CopyableCode code="AvailabilityZone, Quantity, region" /> | Allocates a Dedicated Host to your account. At a minimum, specify the supported instance type or instance family, the Availability Zone in which to allocate the host, and the number of hosts to allocate. |
| <CopyableCode code="hosts_Modify" /> | `EXEC` | <CopyableCode code="HostId, region" /> | &lt;p&gt;Modify the auto-placement setting of a Dedicated Host. When auto-placement is enabled, any instances that you launch with a tenancy of &lt;code&gt;host&lt;/code&gt; but without a specific host ID are placed onto any available Dedicated Host in your account that has auto-placement enabled. When auto-placement is disabled, you need to provide a host ID to have the instance launch onto a specific host. If no host ID is provided, the instance is launched onto a suitable host with auto-placement enabled.&lt;/p&gt; &lt;p&gt;You can also use this API action to modify a Dedicated Host to support either multiple instance types in an instance family, or to support a specific instance type only.&lt;/p&gt; |
| <CopyableCode code="hosts_Release" /> | `EXEC` | <CopyableCode code="HostId, region" /> | &lt;p&gt;When you no longer want to use an On-Demand Dedicated Host it can be released. On-Demand billing is stopped and the host goes into &lt;code&gt;released&lt;/code&gt; state. The host ID of Dedicated Hosts that have been released can no longer be specified in another request, for example, to modify the host. You must stop or terminate all instances on a host before it can be released.&lt;/p&gt; &lt;p&gt;When Dedicated Hosts are released, it may take some time for them to stop counting toward your limit and you may receive capacity errors when trying to allocate new Dedicated Hosts. Wait a few minutes and then try again.&lt;/p&gt; &lt;p&gt;Released hosts still appear in a &lt;a&gt;DescribeHosts&lt;/a&gt; response.&lt;/p&gt; |
