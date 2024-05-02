---
title: core_network
hide_title: false
hide_table_of_contents: false
keywords:
  - core_network
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
Gets or operates on an individual <code>core_network</code> resource, use <code>core_networks</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>core_network</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::NetworkManager::CoreNetwork Resource Type Definition.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.networkmanager.core_network</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>global_network_id</code></td><td><code>string</code></td><td>The ID of the global network that your core network is a part of.</td></tr>
<tr><td><code>core_network_id</code></td><td><code>string</code></td><td>The Id of core network</td></tr>
<tr><td><code>core_network_arn</code></td><td><code>string</code></td><td>The ARN (Amazon resource name) of core network</td></tr>
<tr><td><code>policy_document</code></td><td><code>object</code></td><td>Live policy document for the core network, you must provide PolicyDocument in Json Format</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of core network</td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td>The creation time of core network</td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td>The state of core network</td></tr>
<tr><td><code>segments</code></td><td><code>array</code></td><td>The segments within a core network.</td></tr>
<tr><td><code>edges</code></td><td><code>array</code></td><td>The edges within a core network.</td></tr>
<tr><td><code>owner_account</code></td><td><code>string</code></td><td>Owner of the core network</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags for the global network.</td></tr>
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
global_network_id,
core_network_id,
core_network_arn,
policy_document,
description,
created_at,
state,
segments,
edges,
owner_account,
tags
FROM aws.networkmanager.core_network
WHERE data__Identifier = '<CoreNetworkId>';
```

## Permissions

To operate on the <code>core_network</code> resource, the following permissions are required:

### Read
```json
networkmanager:GetCoreNetwork,
networkmanager:GetCoreNetworkPolicy
```

### Update
```json
networkmanager:UpdateCoreNetwork,
networkmanager:GetCoreNetwork,
networkmanager:ListTagsForResource,
networkmanager:PutCoreNetworkPolicy,
networkmanager:GetCoreNetworkPolicy,
networkmanager:ExecuteCoreNetworkChangeSet,
networkmanager:TagResource,
networkmanager:UntagResource,
ec2:DescribeRegions
```

### Delete
```json
networkmanager:DeleteCoreNetwork,
networkmanager:UntagResource,
networkmanager:GetCoreNetwork,
networkmanager:GetCoreNetworkPolicy,
ec2:DescribeRegions
```

