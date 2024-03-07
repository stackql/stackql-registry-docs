---
title: connect_peers
hide_title: false
hide_table_of_contents: false
keywords:
  - connect_peers
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
Retrieves a list of <code>connect_peers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connect_peers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>connect_peers</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.networkmanager.connect_peers</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>connect_peer_id</code></td><td><code>string</code></td><td>The ID of the Connect peer.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>connect_peers</code> resource, the following permissions are required:

### Create
```json
networkmanager:GetConnectPeer,
networkmanager:CreateConnectPeer,
networkmanager:TagResource,
ec2:DescribeRegions
```

### List
```json
networkmanager:ListConnectPeers
```


## Example
```sql
SELECT
region,
connect_peer_id
FROM awscc.networkmanager.connect_peers
WHERE region = 'us-east-1'
```
