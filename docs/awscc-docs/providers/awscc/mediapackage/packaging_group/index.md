---
title: packaging_group
hide_title: false
hide_table_of_contents: false
keywords:
  - packaging_group
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
Gets an individual <code>packaging_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>packaging_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>packaging_group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.mediapackage.packaging_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The ID of the PackagingGroup.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The ARN of the PackagingGroup.</td></tr>
<tr><td><code>domain_name</code></td><td><code>string</code></td><td>The fully qualified domain name for Assets in the PackagingGroup.</td></tr>
<tr><td><code>authorization</code></td><td><code>object</code></td><td>CDN Authorization</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
<tr><td><code>egress_access_logs</code></td><td><code>object</code></td><td>The configuration parameters for egress access logging.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>packaging_group</code> resource, the following permissions are required:

### Read
<pre>
mediapackage-vod:DescribePackagingGroup</pre>

### Update
<pre>
mediapackage-vod:DescribePackagingGroup,
mediapackage-vod:UpdatePackagingGroup,
mediapackage-vod:ConfigureLogs,
mediapackage-vod:TagResource,
iam:PassRole,
iam:CreateServiceLinkedRole</pre>

### Delete
<pre>
mediapackage-vod:DescribePackagingGroup,
mediapackage-vod:DeletePackagingGroup</pre>


## Example
```sql
SELECT
region,
id,
arn,
domain_name,
authorization,
tags,
egress_access_logs
FROM awscc.mediapackage.packaging_group
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
