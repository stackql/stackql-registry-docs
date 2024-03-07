---
title: space
hide_title: false
hide_table_of_contents: false
keywords:
  - space
  - sagemaker
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>space</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>space</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>space</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.sagemaker.space</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>space_arn</code></td><td><code>string</code></td><td>The space Amazon Resource Name (ARN).</td></tr>
<tr><td><code>domain_id</code></td><td><code>string</code></td><td>The ID of the associated Domain.</td></tr>
<tr><td><code>space_name</code></td><td><code>string</code></td><td>A name for the Space.</td></tr>
<tr><td><code>space_settings</code></td><td><code>object</code></td><td>A collection of settings.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of tags to apply to the space.</td></tr>
<tr><td><code>ownership_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>space_sharing_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>space_display_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>url</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
space_arn,
domain_id,
space_name,
space_settings,
tags,
ownership_settings,
space_sharing_settings,
space_display_name,
url
FROM awscc.sagemaker.space
WHERE region = 'us-east-1'
AND data__Identifier = '{DomainId}';
AND data__Identifier = '{SpaceName}';
```

## Permissions

To operate on the <code>space</code> resource, the following permissions are required:

### Read
```json
sagemaker:DescribeSpace
```

### Update
```json
sagemaker:UpdateSpace,
sagemaker:DescribeSpace
```

### Delete
```json
sagemaker:DeleteSpace,
sagemaker:DescribeSpace
```

