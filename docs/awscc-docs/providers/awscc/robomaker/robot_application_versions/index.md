---
title: robot_application_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - robot_application_versions
  - robomaker
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>robot_application_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>robot_application_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>robot_application_versions</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.robomaker.robot_application_versions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>robot_application_versions</code> resource, the following permissions are required:

### Create
<pre>
robomaker:CreateRobotApplicationVersion,
s3:GetObject,
ecr:BatchGetImage,
ecr:GetAuthorizationToken,
ecr:BatchCheckLayerAvailability,
ecr-public:GetAuthorizationToken,
sts:GetServiceBearerToken</pre>


## Example
```sql
SELECT
region,
arn
FROM awscc.robomaker.robot_application_versions
WHERE region = 'us-east-1'
```
