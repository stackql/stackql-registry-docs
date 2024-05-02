---
title: application
hide_title: false
hide_table_of_contents: false
keywords:
  - application
  - m2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>application</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents an application that runs on an AWS Mainframe Modernization Environment</td></tr>
<tr><td><b>Id</b></td><td><code>aws.m2.application</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>application_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>application_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>definition</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>engine_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td>The ID or the Amazon Resource Name (ARN) of the customer managed KMS Key used for encrypting application-related resources.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
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
application_arn,
application_id,
definition,
description,
engine_type,
kms_key_id,
name,
role_arn,
tags
FROM aws.m2.application
WHERE data__Identifier = '<ApplicationArn>';
```

## Permissions

To operate on the <code>application</code> resource, the following permissions are required:

### Read
```json
m2:GetApplication,
m2:ListTagsForResource
```

### Update
```json
m2:UpdateApplication,
m2:GetApplication,
m2:ListTagsForResource,
m2:TagResource,
m2:UntagResource,
s3:GetObject,
s3:ListBucket
```

### Delete
```json
elasticloadbalancing:DeleteListener,
elasticloadbalancing:DeleteTargetGroup,
logs:DeleteLogDelivery,
m2:GetApplication,
m2:DeleteApplication
```

