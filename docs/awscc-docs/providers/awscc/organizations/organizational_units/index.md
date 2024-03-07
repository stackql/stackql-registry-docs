---
title: organizational_units
hide_title: false
hide_table_of_contents: false
keywords:
  - organizational_units
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
Retrieves a list of <code>organizational_units</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organizational_units</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>organizational_units</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.organizations.organizational_units</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The unique identifier (ID) associated with this OU.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id
FROM awscc.organizations.organizational_units
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>organizational_units</code> resource, the following permissions are required:

### Create
```json
organizations:CreateOrganizationalUnit,
organizations:DescribeOrganizationalUnit,
organizations:ListParents,
organizations:ListTagsForResource,
organizations:TagResource
```

### List
```json
organizations:ListOrganizationalUnitsForParent
```

