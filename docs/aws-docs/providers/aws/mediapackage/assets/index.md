---
title: assets
hide_title: false
hide_table_of_contents: false
keywords:
  - assets
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
Retrieves a list of <code>assets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.mediapackage.assets</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The ARN of the Asset.</td></tr><tr><td><code>CreatedAt</code></td><td><code>string</code></td><td>The time the Asset was initially submitted for Ingest.</td></tr><tr><td><code>EgressEndpoints</code></td><td><code>array</code></td><td>The list of egress endpoints available for the Asset.</td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td>The unique identifier for the Asset.</td></tr><tr><td><code>PackagingGroupId</code></td><td><code>string</code></td><td>The ID of the PackagingGroup for the Asset.</td></tr><tr><td><code>ResourceId</code></td><td><code>string</code></td><td>The resource ID to include in SPEKE key requests.</td></tr><tr><td><code>SourceArn</code></td><td><code>string</code></td><td>ARN of the source object in S3.</td></tr><tr><td><code>SourceRoleArn</code></td><td><code>string</code></td><td>The IAM role_arn used to access the source S3 bucket.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.mediapackage.assets
WHERE region = 'us-east-1'
```
