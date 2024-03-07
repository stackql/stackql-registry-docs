---
title: theme
hide_title: false
hide_table_of_contents: false
keywords:
  - theme
  - quicksight
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>theme</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>theme</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>theme</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.quicksight.theme</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>aws_account_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>base_theme_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>created_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>last_updated_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>permissions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>theme_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>version</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>version_description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>theme</code> resource, the following permissions are required:

### Read
```json
quicksight:DescribeTheme,
quicksight:DescribeThemePermissions,
quicksight:ListTagsForResource
```

### Update
```json
quicksight:DescribeTheme,
quicksight:DescribeThemePermissions,
quicksight:UpdateTheme,
quicksight:UpdateThemePermissions,
quicksight:TagResource,
quicksight:UntagResource,
quicksight:ListTagsForResource
```

### Delete
```json
quicksight:DescribeTheme,
quicksight:DeleteTheme
```


## Example
```sql
SELECT
region,
arn,
aws_account_id,
base_theme_id,
configuration,
created_time,
last_updated_time,
name,
permissions,
tags,
theme_id,
type,
version,
version_description
FROM awscc.quicksight.theme
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ThemeId&gt;'
AND data__Identifier = '&lt;AwsAccountId&gt;'
```
