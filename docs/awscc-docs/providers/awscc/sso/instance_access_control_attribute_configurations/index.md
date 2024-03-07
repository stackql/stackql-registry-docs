---
title: instance_access_control_attribute_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_access_control_attribute_configurations
  - sso
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>instance_access_control_attribute_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_access_control_attribute_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>instance_access_control_attribute_configurations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.sso.instance_access_control_attribute_configurations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>instance_arn</code></td><td><code>string</code></td><td>The ARN of the AWS SSO instance under which the operation will be executed.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
instance_arn
FROM awscc.sso.instance_access_control_attribute_configurations
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>instance_access_control_attribute_configurations</code> resource, the following permissions are required:

### Create
```json
sso:CreateInstanceAccessControlAttributeConfiguration,
sso:UpdateApplicationProfileForAWSAccountInstance,
sso:DescribeInstanceAccessControlAttributeConfiguration
```

### List
```json
sso:DescribeInstanceAccessControlAttributeConfiguration
```

