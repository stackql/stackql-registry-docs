---
title: image_builders
hide_title: false
hide_table_of_contents: false
keywords:
  - image_builders
  - appstream
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>image_builders</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_builders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>image_builders</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.appstream.image_builders</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>image_builders</code> resource, the following permissions are required:

### Create
<pre>
appstream:CreateImageBuilder,
appstream:CreateImageBuilderStreamingURL,
appstream:CreateStreamingURL,
appstream:DeleteImageBuilder,
appstream:DescribeImageBuilders,
appstream:StartImageBuilder,
appstream:StopImageBuilder,
iam:CreateServiceLinkedRole,
iam:DeleteServiceLinkedRole,
iam:GetServiceLinkedRoleDeletionStatus</pre>

### List
<pre>
appstream:CreateImageBuilder,
appstream:CreateImageBuilderStreamingURL,
appstream:CreateStreamingURL,
appstream:DeleteImageBuilder,
appstream:DescribeImageBuilders,
appstream:StartImageBuilder,
appstream:StopImageBuilder,
iam:CreateServiceLinkedRole,
iam:DeleteServiceLinkedRole,
iam:GetServiceLinkedRoleDeletionStatus</pre>


## Example
```sql
SELECT
region,
name
FROM awscc.appstream.image_builders
WHERE region = 'us-east-1'
```
