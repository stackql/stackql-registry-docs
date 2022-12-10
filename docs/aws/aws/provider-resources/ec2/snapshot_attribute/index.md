---
title: snapshot_attribute
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshot_attribute
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
<tr><td><b>Name</b></td><td><code>snapshot_attribute</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.snapshot_attribute</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `snapshotId` | `string` | The ID of the EBS snapshot. |
| `createVolumePermission` | `array` | The users and groups that have the permissions for creating volumes from the snapshot. |
| `productCodes` | `array` | The product codes. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `snapshot_attribute_Describe` | `SELECT` | `Attribute, SnapshotId` | &lt;p&gt;Describes the specified attribute of the specified snapshot. You can specify only one attribute at a time.&lt;/p&gt; &lt;p&gt;For more information about EBS snapshots, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html"&gt;Amazon EBS snapshots&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| `snapshot_attribute_Modify` | `EXEC` | `SnapshotId` | &lt;p&gt;Adds or removes permission settings for the specified snapshot. You may add or remove specified Amazon Web Services account IDs from a snapshot's list of create volume permissions, but you cannot do both in a single operation. If you need to both add and remove account IDs for a snapshot, you must use multiple operations. You can make up to 500 modifications to a snapshot in a single operation.&lt;/p&gt; &lt;p&gt;Encrypted snapshots and snapshots with Amazon Web Services Marketplace product codes cannot be made public. Snapshots encrypted with your default KMS key cannot be shared with other accounts.&lt;/p&gt; &lt;p&gt;For more information about modifying snapshot permissions, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html"&gt;Share a snapshot&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| `snapshot_attribute_Reset` | `EXEC` | `Attribute, SnapshotId` | &lt;p&gt;Resets permission settings for the specified snapshot.&lt;/p&gt; &lt;p&gt;For more information about modifying snapshot permissions, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html"&gt;Share a snapshot&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
