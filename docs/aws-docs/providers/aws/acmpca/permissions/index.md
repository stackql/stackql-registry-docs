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
<tr><td><b>Id</b></td><td><code>aws.acmpca.permissions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Actions</code></td><td><code>array</code></td><td>The actions that the specified AWS service principal can use. Actions IssueCertificate, GetCertificate and ListPermissions must be provided.</td></tr><tr><td><code>CertificateAuthorityArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Private Certificate Authority that grants the permission.</td></tr><tr><td><code>Principal</code></td><td><code>string</code></td><td>The AWS service or identity that receives the permission. At this time, the only valid principal is acm.amazonaws.com.</td></tr><tr><td><code>SourceAccount</code></td><td><code>string</code></td><td>The ID of the calling account.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.acmpca.permissions
WHERE region = 'us-east-1'
```
