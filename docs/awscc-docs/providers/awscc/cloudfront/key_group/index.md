---
title: key_group
hide_title: false
hide_table_of_contents: false
keywords:
  - key_group
  - cloudfront
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>key_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>key_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>key_group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cloudfront.key_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>key_group_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>last_modified_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
key_group_config,
last_modified_time
FROM awscc.cloudfront.key_group
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>key_group</code> resource, the following permissions are required:

### Delete
```json
cloudfront:DeleteKeyGroup,
cloudfront:GetKeyGroup
```

### Read
```json
cloudfront:GetKeyGroup
```

### Update
```json
cloudfront:UpdateKeyGroup,
cloudfront:GetKeyGroup
```

