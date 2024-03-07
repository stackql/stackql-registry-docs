---
title: addons
hide_title: false
hide_table_of_contents: false
keywords:
  - addons
  - eks
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>addons</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>addons</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>addons</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.eks.addons</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>cluster_name</code></td><td><code>string</code></td><td>Name of Cluster</td></tr>
<tr><td><code>addon_name</code></td><td><code>string</code></td><td>Name of Addon</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
cluster_name,
addon_name
FROM awscc.eks.addons
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>addons</code> resource, the following permissions are required:

### Create
```json
eks:CreateAddon,
eks:DescribeAddon,
eks:TagResource,
iam:PassRole
```

### List
```json
eks:ListAddons
```

