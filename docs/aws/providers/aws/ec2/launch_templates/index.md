---
title: launch_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - launch_templates
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
<tr><td><b>Name</b></td><td><code>launch_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.launch_templates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `launchTemplateName` | `string` | The name of the launch template. |
| `tagSet` | `array` | The tags for the launch template. |
| `createTime` | `string` | The time launch template was created. |
| `createdBy` | `string` | The principal that created the launch template.  |
| `defaultVersionNumber` | `integer` | The version number of the default version of the launch template. |
| `latestVersionNumber` | `integer` | The version number of the latest version of the launch template. |
| `launchTemplateId` | `string` | The ID of the launch template. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `launch_templates_Describe` | `SELECT` |  | Describes one or more launch templates. |
| `launch_template_Create` | `INSERT` | `LaunchTemplateData, LaunchTemplateName` | &lt;p&gt;Creates a launch template.&lt;/p&gt; &lt;p&gt;A launch template contains the parameters to launch an instance. When you launch an instance using &lt;a&gt;RunInstances&lt;/a&gt;, you can specify a launch template instead of providing the launch parameters in the request. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html"&gt;Launching an instance from a launch template&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you want to clone an existing launch template as the basis for creating a new launch template, you can use the Amazon EC2 console. The API, SDKs, and CLI do not support cloning a template. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html#create-launch-template-from-existing-launch-template"&gt;Create a launch template from an existing launch template&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| `launch_template_Delete` | `DELETE` |  | Deletes a launch template. Deleting a launch template deletes all of its versions. |
| `launch_template_Modify` | `EXEC` |  | Modifies a launch template. You can specify which version of the launch template to set as the default version. When launching an instance, the default version applies when a launch template version is not specified. |
