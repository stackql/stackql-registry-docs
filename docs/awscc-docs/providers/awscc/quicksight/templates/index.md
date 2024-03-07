---
title: templates
hide_title: false
hide_table_of_contents: false
keywords:
  - templates
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
Retrieves a list of <code>templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>templates</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.quicksight.templates</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>aws_account_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>template_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
aws_account_id,
template_id
FROM awscc.quicksight.templates
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>templates</code> resource, the following permissions are required:

### Create
```json
quicksight:DescribeTemplate,
quicksight:DescribeTemplatePermissions,
quicksight:CreateTemplate,
quicksight:DescribeAnalysis,
quicksight:TagResource,
quicksight:UntagResource,
quicksight:ListTagsForResource
```

### List
```json
quicksight:ListTemplates
```

