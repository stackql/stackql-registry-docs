---
title: fast_snapshot_restores
hide_title: false
hide_table_of_contents: false
keywords:
  - fast_snapshot_restores
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
<tr><td><b>Name</b></td><td><code>fast_snapshot_restores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.fast_snapshot_restores</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `optimizingTime` | `string` | The time at which fast snapshot restores entered the &lt;code&gt;optimizing&lt;/code&gt; state. |
| `state` | `string` | The state of fast snapshot restores. |
| `disablingTime` | `string` | The time at which fast snapshot restores entered the &lt;code&gt;disabling&lt;/code&gt; state. |
| `ownerAlias` | `string` | The Amazon Web Services owner alias that enabled fast snapshot restores on the snapshot. This is intended for future use. |
| `enabledTime` | `string` | The time at which fast snapshot restores entered the &lt;code&gt;enabled&lt;/code&gt; state. |
| `snapshotId` | `string` | The ID of the snapshot. |
| `enablingTime` | `string` | The time at which fast snapshot restores entered the &lt;code&gt;enabling&lt;/code&gt; state. |
| `disabledTime` | `string` | The time at which fast snapshot restores entered the &lt;code&gt;disabled&lt;/code&gt; state. |
| `stateTransitionReason` | `string` | &lt;p&gt;The reason for the state transition. The possible values are as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Client.UserInitiated&lt;/code&gt; - The state successfully transitioned to &lt;code&gt;enabling&lt;/code&gt; or &lt;code&gt;disabling&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Client.UserInitiated - Lifecycle state transition&lt;/code&gt; - The state successfully transitioned to &lt;code&gt;optimizing&lt;/code&gt;, &lt;code&gt;enabled&lt;/code&gt;, or &lt;code&gt;disabled&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `ownerId` | `string` | The ID of the Amazon Web Services account that enabled fast snapshot restores on the snapshot. |
| `availabilityZone` | `string` | The Availability Zone. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `fast_snapshot_restores_Describe` | `SELECT` |  | Describes the state of fast snapshot restores for your snapshots. |
| `fast_snapshot_restores_Disable` | `EXEC` | `AvailabilityZone, SourceSnapshotId` | Disables fast snapshot restores for the specified snapshots in the specified Availability Zones. |
| `fast_snapshot_restores_Enable` | `EXEC` | `AvailabilityZone, SourceSnapshotId` | &lt;p&gt;Enables fast snapshot restores for the specified snapshots in the specified Availability Zones.&lt;/p&gt; &lt;p&gt;You get the full benefit of fast snapshot restores after they enter the &lt;code&gt;enabled&lt;/code&gt; state. To get the current state of fast snapshot restores, use &lt;a&gt;DescribeFastSnapshotRestores&lt;/a&gt;. To disable fast snapshot restores, use &lt;a&gt;DisableFastSnapshotRestores&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-fast-snapshot-restore.html"&gt;Amazon EBS fast snapshot restore&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
