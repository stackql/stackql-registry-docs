---
title: access_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - access_policy
  - opensearchserverless
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>access_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>access_policy</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.opensearchserverless.access_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the policy</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the policy</td></tr>
<tr><td><code>policy</code></td><td><code>string</code></td><td>The JSON policy document that is the content for the policy</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
type,
description,
policy
FROM awscc.opensearchserverless.access_policy
WHERE data__Identifier = '<Type>|<Name>';
```

## Permissions

To operate on the <code>access_policy</code> resource, the following permissions are required:

### Read
```json
aoss:GetAccessPolicy
```

### Update
```json
aoss:UpdateAccessPolicy,
aoss:GetAccessPolicy
```

### Delete
```json
aoss:DeleteAccessPolicy,
aoss:GetAccessPolicy
```

