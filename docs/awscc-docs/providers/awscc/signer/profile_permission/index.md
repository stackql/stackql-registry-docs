---
title: profile_permission
hide_title: false
hide_table_of_contents: false
keywords:
  - profile_permission
  - signer
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>profile_permission</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profile_permission</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>profile_permission</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.signer.profile_permission</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>profile_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>profile_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>action</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>principal</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>statement_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
profile_name,
profile_version,
action,
principal,
statement_id
FROM awscc.signer.profile_permission
WHERE data__Identifier = '<StatementId>|<ProfileName>';
```

## Permissions

To operate on the <code>profile_permission</code> resource, the following permissions are required:

### Read
```json
signer:ListProfilePermissions
```

### Delete
```json
signer:RemoveProfilePermission,
signer:ListProfilePermissions
```

