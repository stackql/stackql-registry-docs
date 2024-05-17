---
title: launch_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - launch_templates
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
<tr><td><b>Name</b></td><td><code>launch_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.launch_templates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="createTime" /> | `string` | The time launch template was created. |
| <CopyableCode code="createdBy" /> | `string` | The principal that created the launch template.  |
| <CopyableCode code="defaultVersionNumber" /> | `integer` | The version number of the default version of the launch template. |
| <CopyableCode code="latestVersionNumber" /> | `integer` | The version number of the latest version of the launch template. |
| <CopyableCode code="launchTemplateId" /> | `string` | The ID of the launch template. |
| <CopyableCode code="launchTemplateName" /> | `string` | The name of the launch template. |
| <CopyableCode code="tagSet" /> | `array` | The tags for the launch template. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="launch_templates_Describe" /> | `SELECT` | <CopyableCode code="region" /> | Describes one or more launch templates. |
| <CopyableCode code="launch_template_Create" /> | `INSERT` | <CopyableCode code="LaunchTemplateData, LaunchTemplateName, region" /> | &lt;p&gt;Creates a launch template.&lt;/p&gt; &lt;p&gt;A launch template contains the parameters to launch an instance. When you launch an instance using &lt;a&gt;RunInstances&lt;/a&gt;, you can specify a launch template instead of providing the launch parameters in the request. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html"&gt;Launching an instance from a launch template&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you want to clone an existing launch template as the basis for creating a new launch template, you can use the Amazon EC2 console. The API, SDKs, and CLI do not support cloning a template. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html#create-launch-template-from-existing-launch-template"&gt;Create a launch template from an existing launch template&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| <CopyableCode code="launch_template_Delete" /> | `DELETE` | <CopyableCode code="region" /> | Deletes a launch template. Deleting a launch template deletes all of its versions. |
| <CopyableCode code="launch_template_Modify" /> | `EXEC` | <CopyableCode code="region" /> | Modifies a launch template. You can specify which version of the launch template to set as the default version. When launching an instance, the default version applies when a launch template version is not specified. |
