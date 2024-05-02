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
Gets or operates on an individual <code>launch_template</code> resource, use <code>launch_templates</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>launch_template</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies the properties for creating a launch template.&lt;br&#x2F;&gt; The minimum required properties for specifying a launch template are as follows:&lt;br&#x2F;&gt;  +  You must specify at least one property for the launch template data.&lt;br&#x2F;&gt;  +  You do not need to specify a name for the launch template. If you do not specify a name, CFN creates the name for you.&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; A launch template can contain some or all of the configuration information to launch an instance. When you launch an instance using a launch template, instance properties that are not specified in the launch template use default values, except the ``ImageId`` property, which has no default value. If you do not specify an AMI ID for the launch template ``ImageId`` property, you must specify an AMI ID for the instance ``ImageId`` property.&lt;br&#x2F;&gt; For more information, see &#91;Launch an instance from a launch template&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSEC2&#x2F;latest&#x2F;UserGuide&#x2F;ec2-launch-templates.html) in the *Amazon EC2 User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.launch_template</code></td></tr>
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

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.ec2.launch_template
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

