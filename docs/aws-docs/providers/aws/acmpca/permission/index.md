---
title: permission
hide_title: false
hide_table_of_contents: false
keywords:
  - permission
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
Gets an individual <code>permission</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>permission</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Permission set on private certificate authority</td></tr>
<tr><td><b>Id</b></td><td><code>aws.acmpca.permission</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>actions</code></td><td><code>array</code></td><td>The actions that the specified AWS service principal can use. Actions IssueCertificate, GetCertificate and ListPermissions must be provided.</td></tr>
<tr><td><code>certificate_authority_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Private Certificate Authority that grants the permission.</td></tr>
<tr><td><code>principal</code></td><td><code>string</code></td><td>The AWS service or identity that receives the permission. At this time, the only valid principal is acm.amazonaws.com.</td></tr>
<tr><td><code>source_account</code></td><td><code>string</code></td><td>The ID of the calling account.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
actions,
certificate_authority_arn,
principal,
source_account
FROM aws.acmpca.permission
WHERE data__Identifier = '<CertificateAuthorityArn>|<Principal>';
```

## Permissions

To operate on the <code>permission</code> resource, the following permissions are required:

### Read
```json
acm-pca:ListPermissions
```

### Delete
```json
acm-pca:DeletePermission
```

