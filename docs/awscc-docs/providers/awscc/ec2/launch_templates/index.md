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
Retrieves a list of <code>launch_templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>launch_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>launch_templates</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.launch_templates</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>launch_template_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
launch_template_id
FROM awscc.ec2.launch_templates
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

