---
title: fast_launch_images
hide_title: false
hide_table_of_contents: false
keywords:
  - fast_launch_images
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fast_launch_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2_api.fast_launch_images</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `imageId` | `string` | The image ID that identifies the fast-launch enabled Windows image. |
| `launchTemplate` | `object` | Identifies the launch template to use for faster launching of the Windows AMI. |
| `maxParallelLaunches` | `integer` | The maximum number of parallel instances that are launched for creating resources. |
| `ownerId` | `string` | The owner ID for the fast-launch enabled Windows AMI. |
| `resourceType` | `string` | The resource type that is used for pre-provisioning the Windows AMI. Supported values include: &lt;code&gt;snapshot&lt;/code&gt;. |
| `snapshotConfiguration` | `object` | Configuration settings for creating and managing pre-provisioned snapshots for a fast-launch enabled Windows AMI. |
| `state` | `string` | The current state of faster launching for the specified Windows AMI. |
| `stateTransitionReason` | `string` | The reason that faster launching for the Windows AMI changed to the current state. |
| `stateTransitionTime` | `string` | The time that faster launching for the Windows AMI changed to the current state. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `fast_launch_images_Describe` | `SELECT` | `region` |
