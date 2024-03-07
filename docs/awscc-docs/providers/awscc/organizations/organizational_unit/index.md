---
title: organizational_unit
hide_title: false
hide_table_of_contents: false
keywords:
  - organizational_unit
  - organizations
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>organizational_unit</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organizational_unit</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>organizational_unit</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.organizations.organizational_unit</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of this OU.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The unique identifier (ID) associated with this OU.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The friendly name of this OU.</td></tr>
<tr><td><code>parent_id</code></td><td><code>string</code></td><td>The unique identifier (ID) of the parent root or OU that you want to create the new OU in.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of tags that you want to attach to the newly created OU.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>organizational_unit</code> resource, the following permissions are required:

### Read
```json
organizations:DescribeOrganizationalUnit,
organizations:ListParents,
organizations:ListTagsForResource
```

### Update
```json
organizations:DescribeOrganizationalUnit,
organizations:ListParents,
organizations:ListTagsForResource,
organizations:TagResource,
organizations:UntagResource,
organizations:UpdateOrganizationalUnit
```

### Delete
```json
organizations:DeleteOrganizationalUnit
```


## Example
```sql
SELECT
region,
arn,
id,
name,
parent_id,
tags
FROM awscc.organizations.organizational_unit
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
