---
title: conformance_packs
hide_title: false
hide_table_of_contents: false
keywords:
  - conformance_packs
  - config
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>conformance_packs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>conformance_packs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>conformance_packs</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.config.conformance_packs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>conformance_pack_name</code></td><td><code>string</code></td><td>Name of the conformance pack which will be assigned as the unique identifier.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
conformance_pack_name
FROM awscc.config.conformance_packs
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>conformance_packs</code> resource, the following permissions are required:

### Create
```json
config:PutConformancePack,
config:DescribeConformancePackStatus,
config:DescribeConformancePacks,
s3:GetObject,
s3:GetBucketAcl,
iam:CreateServiceLinkedRole,
iam:PassRole
```

### List
```json
config:DescribeConformancePacks
```

