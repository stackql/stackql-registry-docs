---
title: group
hide_title: false
hide_table_of_contents: false
keywords:
  - group
  - resourcegroups
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
<tr><td><b>Id</b></td><td><code>awscc.resourcegroups.group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the resource group</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the resource group</td></tr>
<tr><td><code>resource_query</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Resource Group ARN.</td></tr>
<tr><td><code>configuration</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>resources</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
description,
resource_query,
tags,
arn,
configuration,
resources
FROM awscc.resourcegroups.group
WHERE region = 'us-east-1'
AND data__Identifier = '{Name}';
```

## Permissions

To operate on the <code>group</code> resource, the following permissions are required:

### Read
```json
resource-groups:GetGroup,
resource-groups:GetGroupQuery,
resource-groups:GetTags,
resource-groups:GetGroupConfiguration,
resource-groups:ListGroupResources
```

### Update
```json
resource-groups:UpdateGroup,
resource-groups:GetTags,
resource-groups:GetGroupQuery,
resource-groups:UpdateGroupQuery,
resource-groups:Tag,
resource-groups:Untag,
resource-groups:PutGroupConfiguration,
resource-groups:GetGroupConfiguration,
resource-groups:ListGroupResources,
resource-groups:GroupResources,
resource-groups:UnGroupResources
```

### Delete
```json
resource-groups:DeleteGroup,
resource-groups:UnGroupResources
```

