---
title: node
hide_title: false
hide_table_of_contents: false
keywords:
  - node
  - managedblockchain
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>node</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>node</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>node</td></tr>
<tr><td><b>Id</b></td><td><code>aws.managedblockchain.node</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>node_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>member_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>network_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>node_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
node_id,
member_id,
arn,
network_id,
node_configuration
FROM aws.managedblockchain.node
WHERE region = 'us-east-1'
AND data__Identifier = '<NodeId>'
```
