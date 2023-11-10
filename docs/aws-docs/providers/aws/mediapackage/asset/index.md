---
title: asset
hide_title: false
hide_table_of_contents: false
keywords:
  - asset
  - mediapackage
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>asset</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>asset</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>asset</td></tr>
<tr><td><b>Id</b></td><td><code>aws.mediapackage.asset</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The ARN of the Asset.</td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td>The time the Asset was initially submitted for Ingest.</td></tr>
<tr><td><code>egress_endpoints</code></td><td><code>array</code></td><td>The list of egress endpoints available for the Asset.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The unique identifier for the Asset.</td></tr>
<tr><td><code>packaging_group_id</code></td><td><code>string</code></td><td>The ID of the PackagingGroup for the Asset.</td></tr>
<tr><td><code>resource_id</code></td><td><code>string</code></td><td>The resource ID to include in SPEKE key requests.</td></tr>
<tr><td><code>source_arn</code></td><td><code>string</code></td><td>ARN of the source object in S3.</td></tr>
<tr><td><code>source_role_arn</code></td><td><code>string</code></td><td>The IAM role_arn used to access the source S3 bucket.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
created_at,
egress_endpoints,
id,
packaging_group_id,
resource_id,
source_arn,
source_role_arn,
tags
FROM aws.mediapackage.asset
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
