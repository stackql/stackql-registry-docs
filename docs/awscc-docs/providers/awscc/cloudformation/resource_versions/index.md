---
title: resource_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_versions
  - cloudformation
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>resource_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resource_versions</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cloudformation.resource_versions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the type, here the ResourceVersion. This is used to uniquely identify a ResourceVersion resource</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>resource_versions</code> resource, the following permissions are required:

### Create
```json
cloudformation:DescribeTypeRegistration,
cloudformation:RegisterType,
iam:PassRole,
s3:GetObject,
s3:ListBucket,
kms:Decrypt,
cloudformation:ListTypeVersions,
cloudformation:DeregisterType,
cloudformation:DescribeType
```

### List
```json
cloudformation:ListTypes
```


## Example
```sql
SELECT
region,
arn
FROM awscc.cloudformation.resource_versions
WHERE region = 'us-east-1'
```
