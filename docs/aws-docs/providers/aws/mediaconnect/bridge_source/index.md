---
title: bridge_source
hide_title: false
hide_table_of_contents: false
keywords:
  - bridge_source
  - mediaconnect
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>bridge_source</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bridge_source</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaConnect::BridgeSource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.mediaconnect.bridge_source</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the source.</td></tr>
<tr><td><code>bridge_arn</code></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) of the bridge.</td></tr>
<tr><td><code>flow_source</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>network_source</code></td><td><code>object</code></td><td></td></tr>
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
name,
bridge_arn,
flow_source,
network_source
FROM aws.mediaconnect.bridge_source
WHERE data__Identifier = '<BridgeArn>|<Name>';
```

## Permissions

To operate on the <code>bridge_source</code> resource, the following permissions are required:

### Read
```json
mediaconnect:DescribeBridge
```

### Update
```json
mediaconnect:DescribeBridge,
mediaconnect:UpdateBridgeSource
```

### Delete
```json
mediaconnect:RemoveBridgeSource
```

