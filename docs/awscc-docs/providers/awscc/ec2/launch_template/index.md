---
title: launch_template
hide_title: false
hide_table_of_contents: false
keywords:
  - launch_template
  - ec2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>launch_template</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>launch_template</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>launch_template</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.launch_template</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>launch_template_name</code></td><td><code>string</code></td><td>A name for the launch template.</td></tr>
<tr><td><code>launch_template_data</code></td><td><code>object</code></td><td>The information for the launch template.</td></tr>
<tr><td><code>version_description</code></td><td><code>string</code></td><td>A description for the first version of the launch template.</td></tr>
<tr><td><code>tag_specifications</code></td><td><code>array</code></td><td>The tags to apply to the launch template on creation. To tag the launch template, the resource type must be ``launch-template``.&lt;br&#x2F;&gt; To specify the tags for the resources that are created when an instance is launched, you must use &#91;TagSpecifications&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-resource-ec2-launchtemplate.html#cfn-ec2-launchtemplate-tagspecifications).</td></tr>
<tr><td><code>latest_version_number</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>launch_template_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>default_version_number</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
launch_template_name,
launch_template_data,
version_description,
tag_specifications,
latest_version_number,
launch_template_id,
default_version_number
FROM awscc.ec2.launch_template
WHERE data__Identifier = '<LaunchTemplateId>';
```

## Permissions

To operate on the <code>launch_template</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeLaunchTemplates
```

### Update
```json
ec2:CreateLaunchTemplateVersion
```

### Delete
```json
ec2:DeleteLaunchTemplate,
ec2:DeleteTags,
ec2:DescribeLaunchTemplates
```

