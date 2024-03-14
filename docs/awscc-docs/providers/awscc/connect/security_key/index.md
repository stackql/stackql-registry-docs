---
title: security_key
hide_title: false
hide_table_of_contents: false
keywords:
  - security_key
  - connect
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>security_key</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_key</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>security_key</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.connect.security_key</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>key</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>instance_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>association_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
key,
instance_id,
association_id
FROM awscc.connect.security_key
WHERE data__Identifier = '<InstanceId>|<AssociationId>';
```

## Permissions

To operate on the <code>security_key</code> resource, the following permissions are required:

### Read
```json
connect:ListSecurityKeys
```

### Delete
```json
connect:DisassociateSecurityKey
```

