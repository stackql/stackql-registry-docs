---
title: domain
hide_title: false
hide_table_of_contents: false
keywords:
  - domain
  - voiceid
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>domain</code> resource, use <code>domains</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::VoiceID::Domain resource specifies an Amazon VoiceID Domain.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.voiceid.domain</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>domain_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>server_side_encryption_configuration</code></td><td><code>object</code></td><td></td></tr>
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
description,
domain_id,
name,
server_side_encryption_configuration,
tags
FROM aws.voiceid.domain
WHERE data__Identifier = '<DomainId>';
```

## Permissions

To operate on the <code>domain</code> resource, the following permissions are required:

### Read
```json
voiceid:DescribeDomain,
voiceid:ListTagsForResource,
kms:Decrypt
```

### Update
```json
voiceid:DescribeDomain,
voiceid:UpdateDomain,
voiceid:TagResource,
voiceid:UntagResource,
voiceid:ListTagsForResource,
kms:CreateGrant,
kms:Decrypt,
kms:DescribeKey
```

### Delete
```json
voiceid:DeleteDomain,
voiceid:DescribeDomain,
kms:Decrypt
```

