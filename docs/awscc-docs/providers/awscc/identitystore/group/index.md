---
title: group
hide_title: false
hide_table_of_contents: false
keywords:
  - group
  - identitystore
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
<tr><td><b>Id</b></td><td><code>awscc.identitystore.group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A string containing the description of the group.</td></tr>
<tr><td><code>display_name</code></td><td><code>string</code></td><td>A string containing the name of the group. This value is commonly displayed when the group is referenced.</td></tr>
<tr><td><code>group_id</code></td><td><code>string</code></td><td>The unique identifier for a group in the identity store.</td></tr>
<tr><td><code>identity_store_id</code></td><td><code>string</code></td><td>The globally unique identifier for the identity store.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
description,
display_name,
group_id,
identity_store_id
FROM awscc.identitystore.group
WHERE data__Identifier = '<GroupId>|<IdentityStoreId>';
```

## Permissions

To operate on the <code>group</code> resource, the following permissions are required:

### Read
```json
identitystore:DescribeGroup
```

### Update
```json
identitystore:DescribeGroup,
identitystore:UpdateGroup
```

### Delete
```json
identitystore:DescribeGroup,
identitystore:DeleteGroup
```

