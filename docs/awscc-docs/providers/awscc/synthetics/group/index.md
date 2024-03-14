---
title: group
hide_title: false
hide_table_of_contents: false
keywords:
  - group
  - synthetics
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.synthetics.group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of the group.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Id of the group.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>resource_arns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
id,
tags,
resource_arns
FROM awscc.synthetics.group
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>group</code> resource, the following permissions are required:

### Update
```json
synthetics:AssociateResource,
synthetics:DisassociateResource,
synthetics:TagResource,
synthetics:UntagResource,
synthetics:GetGroup,
synthetics:ListGroupResources
```

### Read
```json
synthetics:GetGroup,
synthetics:ListTagsForResource,
synthetics:ListGroupResources
```

### Delete
```json
synthetics:DeleteGroup,
synthetics:GetGroup
```

