---
title: global_network
hide_title: false
hide_table_of_contents: false
keywords:
  - global_network
  - networkmanager
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>global_network</code> resource, use <code>global_networks</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_network</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::NetworkManager::GlobalNetwork type specifies a global network of the user's account</td></tr>
<tr><td><b>Id</b></td><td><code>aws.networkmanager.global_network</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the global network.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the global network.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags for the global network.</td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td>The date and time that the global network was created.</td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td>The state of the global network.</td></tr>
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
arn,
id,
description,
tags,
created_at,
state
FROM aws.networkmanager.global_network
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>global_network</code> resource, the following permissions are required:

### Read
```json
networkmanager:DescribeGlobalNetworks
```

### Update
```json
networkmanager:UpdateGlobalNetwork,
networkmanager:DescribeGlobalNetworks,
networkmanager:TagResource,
networkmanager:UntagResource,
networkmanager:ListTagsForResource
```

### Delete
```json
networkmanager:DeleteGlobalNetwork,
networkmanager:DescribeGlobalNetworks
```

