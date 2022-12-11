---
title: fast_launch
hide_title: false
hide_table_of_contents: false
keywords:
  - fast_launch
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
<tr><td><b>Name</b></td><td><code>fast_launch</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.fast_launch</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `fast_launch_Disable` | `EXEC` | `ImageId` | &lt;p&gt;Discontinue faster launching for a Windows AMI, and clean up existing pre-provisioned snapshots. When you disable faster launching, the AMI uses the standard launch process for each instance. All pre-provisioned snapshots must be removed before you can enable faster launching again.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To change these settings, you must own the AMI.&lt;/p&gt; &lt;/note&gt; |
| `fast_launch_Enable` | `EXEC` | `ImageId` | &lt;p&gt;When you enable faster launching for a Windows AMI, images are pre-provisioned, using snapshots to launch instances up to 65% faster. To create the optimized Windows image, Amazon EC2 launches an instance and runs through Sysprep steps, rebooting as required. Then it creates a set of reserved snapshots that are used for subsequent launches. The reserved snapshots are automatically replenished as they are used, depending on your settings for launch frequency.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To change these settings, you must own the AMI.&lt;/p&gt; &lt;/note&gt; |
