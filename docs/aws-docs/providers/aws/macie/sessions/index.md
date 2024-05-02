---
title: sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - sessions
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
Retrieves a list of <code>sessions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sessions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Macie::Session resource specifies a new Amazon Macie session. A session is an object that represents the Amazon Macie service. A session is required for Amazon Macie to become operational.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.macie.sessions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>aws_account_id</code></td><td><code>string</code></td><td>AWS account ID of customer</td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
aws_account_id
FROM aws.macie.sessions
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>sessions</code> resource, the following permissions are required:

### Create
```json
macie2:GetMacieSession,
macie2:EnableMacie
```

### List
```json
macie2:GetMacieSession
```

