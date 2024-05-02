---
title: authorizer
hide_title: false
hide_table_of_contents: false
keywords:
  - authorizer
  - iot
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>authorizer</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorizer</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates an authorizer.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iot.authorizer</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>authorizer_function_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>authorizer_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>signing_disabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>token_key_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>token_signing_public_keys</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>enable_caching_for_http</code></td><td><code>boolean</code></td><td></td></tr>
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
authorizer_function_arn,
arn,
authorizer_name,
signing_disabled,
status,
token_key_name,
token_signing_public_keys,
enable_caching_for_http,
tags
FROM aws.iot.authorizer
WHERE data__Identifier = '<AuthorizerName>';
```

## Permissions

To operate on the <code>authorizer</code> resource, the following permissions are required:

### Read
```json
iot:DescribeAuthorizer,
iot:ListTagsForResource
```

### Update
```json
iot:UpdateAuthorizer,
iot:DescribeAuthorizer,
iot:TagResource,
iot:UntagResource,
iot:ListTagsForResource
```

### Delete
```json
iot:UpdateAuthorizer,
iot:DeleteAuthorizer,
iot:DescribeAuthorizer
```

