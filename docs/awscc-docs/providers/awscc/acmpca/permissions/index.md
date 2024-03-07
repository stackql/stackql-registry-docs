---
title: permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - permissions
  - acmpca
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>permissions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>permissions</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.acmpca.permissions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>certificate_authority_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Private Certificate Authority that grants the permission.</td></tr>
<tr><td><code>principal</code></td><td><code>string</code></td><td>The AWS service or identity that receives the permission. At this time, the only valid principal is acm.amazonaws.com.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
certificate_authority_arn,
principal
FROM awscc.acmpca.permissions
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>permissions</code> resource, the following permissions are required:

### Create
```json
acm-pca:CreatePermission,
acm-pca:ListPermissions
```

