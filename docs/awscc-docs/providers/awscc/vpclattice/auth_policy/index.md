---
title: auth_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - auth_policy
  - vpclattice
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>auth_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>auth_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>auth_policy</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.vpclattice.auth_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>resource_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>policy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
resource_identifier,
policy,
state
FROM awscc.vpclattice.auth_policy
WHERE region = 'us-east-1'
AND data__Identifier = '{ResourceIdentifier}';
```

## Permissions

To operate on the <code>auth_policy</code> resource, the following permissions are required:

### Read
```json
vpc-lattice:GetAuthPolicy
```

### Update
```json
vpc-lattice:GetAuthPolicy,
vpc-lattice:PutAuthPolicy
```

### Delete
```json
vpc-lattice:GetAuthPolicy,
vpc-lattice:DeleteAuthPolicy
```

