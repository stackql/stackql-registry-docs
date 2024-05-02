---
title: agreement
hide_title: false
hide_table_of_contents: false
keywords:
  - agreement
  - transfer
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>agreement</code> resource, use <code>agreements</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agreement</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Transfer::Agreement</td></tr>
<tr><td><b>Id</b></td><td><code>aws.transfer.agreement</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A textual description for the agreement.</td></tr>
<tr><td><code>server_id</code></td><td><code>string</code></td><td>A unique identifier for the server.</td></tr>
<tr><td><code>local_profile_id</code></td><td><code>string</code></td><td>A unique identifier for the local profile.</td></tr>
<tr><td><code>partner_profile_id</code></td><td><code>string</code></td><td>A unique identifier for the partner profile.</td></tr>
<tr><td><code>base_directory</code></td><td><code>string</code></td><td>Specifies the base directory for the agreement.</td></tr>
<tr><td><code>access_role</code></td><td><code>string</code></td><td>Specifies the access role for the agreement.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>Specifies the status of the agreement.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Key-value pairs that can be used to group and search for agreements. Tags are metadata attached to agreements for any purpose.</td></tr>
<tr><td><code>agreement_id</code></td><td><code>string</code></td><td>A unique identifier for the agreement.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Specifies the unique Amazon Resource Name (ARN) for the agreement.</td></tr>
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
description,
server_id,
local_profile_id,
partner_profile_id,
base_directory,
access_role,
status,
tags,
agreement_id,
arn
FROM aws.transfer.agreement
WHERE data__Identifier = '<AgreementId>|<ServerId>';
```

## Permissions

To operate on the <code>agreement</code> resource, the following permissions are required:

### Read
```json
transfer:DescribeAgreement
```

### Update
```json
transfer:UpdateAgreement,
transfer:UnTagResource,
transfer:TagResource,
iam:PassRole
```

### Delete
```json
transfer:DeleteAgreement
```

