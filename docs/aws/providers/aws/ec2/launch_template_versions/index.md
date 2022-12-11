---
title: launch_template_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - launch_template_versions
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
<tr><td><b>Name</b></td><td><code>launch_template_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.launch_template_versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `launchTemplateId` | `string` | The ID of the launch template. |
| `launchTemplateName` | `string` | The name of the launch template. |
| `versionDescription` | `string` | The description for the version. |
| `versionNumber` | `integer` | The version number. |
| `createTime` | `string` | The time the version was created. |
| `createdBy` | `string` | The principal that created the version. |
| `defaultVersion` | `boolean` | Indicates whether the version is the default version. |
| `launchTemplateData` | `object` | The information for a launch template.  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `launch_template_versions_Describe` | `SELECT` |  | Describes one or more versions of a specified launch template. You can describe all versions, individual versions, or a range of versions. You can also describe all the latest versions or all the default versions of all the launch templates in your account. |
| `launch_template_version_Create` | `INSERT` | `LaunchTemplateData` | &lt;p&gt;Creates a new version for a launch template. You can specify an existing version of launch template from which to base the new version.&lt;/p&gt; &lt;p&gt;Launch template versions are numbered in the order in which they are created. You cannot specify, change, or replace the numbering of launch template versions.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html#manage-launch-template-versions"&gt;Managing launch template versions&lt;/a&gt;in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| `launch_template_versions_Delete` | `DELETE` | `LaunchTemplateVersion` | Deletes one or more versions of a launch template. You cannot delete the default version of a launch template; you must first assign a different version as the default. If the default version is the only version for the launch template, you must delete the entire launch template using &lt;a&gt;DeleteLaunchTemplate&lt;/a&gt;. |
