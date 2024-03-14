---
title: service
hide_title: false
hide_table_of_contents: false
keywords:
  - service
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
Gets an individual <code>service</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>service</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.vpclattice.service</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>auth_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>dns_entry</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>last_updated_at</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>certificate_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>custom_domain_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
auth_type,
created_at,
dns_entry,
id,
last_updated_at,
name,
status,
certificate_arn,
custom_domain_name,
tags
FROM awscc.vpclattice.service
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>service</code> resource, the following permissions are required:

### Read
```json
vpc-lattice:GetService,
vpc-lattice:ListTagsForResource
```

### Update
```json
vpc-lattice:UpdateService,
vpc-lattice:TagResource,
vpc-lattice:UntagResource,
vpc-lattice:GetService,
vpc-lattice:ListTagsForResource
```

### Delete
```json
vpc-lattice:DeleteService,
vpc-lattice:GetService
```

