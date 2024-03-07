---
title: global_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - global_networks
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
Retrieves a list of <code>global_networks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>global_networks</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.networkmanager.global_networks</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>global_networks</code> resource, the following permissions are required:

### Create
```json
networkmanager:CreateGlobalNetwork,
networkmanager:DescribeGlobalNetworks,
networkmanager:TagResource,
iam:CreateServiceLinkedRole
```

### List
```json
networkmanager:DescribeGlobalNetworks
```


## Example
```sql
SELECT
region,
id
FROM awscc.networkmanager.global_networks
WHERE region = 'us-east-1'
```
