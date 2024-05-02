---
title: session
hide_title: false
hide_table_of_contents: false
keywords:
  - session
  - macie
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>session</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>session</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Macie::Session resource specifies a new Amazon Macie session. A session is an object that represents the Amazon Macie service. A session is required for Amazon Macie to become operational.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.macie.session</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>aws_account_id</code></td><td><code>string</code></td><td>AWS account ID of customer</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>A enumeration value that specifies the status of the Macie Session.</td></tr>
<tr><td><code>finding_publishing_frequency</code></td><td><code>string</code></td><td>A enumeration value that specifies how frequently finding updates are published.</td></tr>
<tr><td><code>service_role</code></td><td><code>string</code></td><td>Service role used by Macie</td></tr>
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
aws_account_id,
status,
finding_publishing_frequency,
service_role
FROM aws.macie.session
WHERE data__Identifier = '<AwsAccountId>';
```

## Permissions

To operate on the <code>session</code> resource, the following permissions are required:

### Read
```json
macie2:GetMacieSession
```

### Update
```json
macie2:GetMacieSession,
macie2:UpdateMacieSession
```

### Delete
```json
macie2:DisableMacie
```

