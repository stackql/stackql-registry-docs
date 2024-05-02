---
title: server_certificate
hide_title: false
hide_table_of_contents: false
keywords:
  - server_certificate
  - iam
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>server_certificate</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server_certificate</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IAM::ServerCertificate</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iam.server_certificate</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>certificate_body</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>certificate_chain</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>server_certificate_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>path</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>private_key</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the server certificate</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
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
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
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
certificate_body,
certificate_chain,
server_certificate_name,
path,
private_key,
arn,
tags
FROM aws.iam.server_certificate
WHERE data__Identifier = '<ServerCertificateName>';
```

## Permissions

To operate on the <code>server_certificate</code> resource, the following permissions are required:

### Read
```json
iam:GetServerCertificate
```

### Update
```json
iam:TagServerCertificate,
iam:UntagServerCertificate,
iam:ListServerCertificateTags,
iam:GetServerCertificate
```

### Delete
```json
iam:DeleteServerCertificate
```

