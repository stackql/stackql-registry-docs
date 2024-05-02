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
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Used to retrieve a list of <code>launch_templates</code> in a region or create a <code>launch_templates</code> resource, use <code>launch_template</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>launch_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies the properties for creating a launch template.&lt;br&#x2F;&gt; The minimum required properties for specifying a launch template are as follows:&lt;br&#x2F;&gt;  +  You must specify at least one property for the launch template data.&lt;br&#x2F;&gt;  +  You do not need to specify a name for the launch template. If you do not specify a name, CFN creates the name for you.&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; A launch template can contain some or all of the configuration information to launch an instance. When you launch an instance using a launch template, instance properties that are not specified in the launch template use default values, except the ``ImageId`` property, which has no default value. If you do not specify an AMI ID for the launch template ``ImageId`` property, you must specify an AMI ID for the instance ``ImageId`` property.&lt;br&#x2F;&gt; For more information, see &#91;Launch an instance from a launch template&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSEC2&#x2F;latest&#x2F;UserGuide&#x2F;ec2-launch-templates.html) in the *Amazon EC2 User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.launch_templates</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>launch_template_id</code></td><td><code>string</code></td><td></td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
launch_template_id
FROM aws.ec2.launch_templates
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>launch_templates</code> resource, the following permissions are required:

### Create
```json
ec2:CreateLaunchTemplate,
ec2:CreateTags
```

### List
```json
ec2:DescribeLaunchTemplates
```

