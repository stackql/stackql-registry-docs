---
title: ipam_scopes
hide_title: false
hide_table_of_contents: false
keywords:
  - ipam_scopes
  - ec2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>ipam_scopes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ipam_scopes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>ipam_scopes</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.ipam_scopes</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ipam_scope_id</code></td><td><code>string</code></td><td>Id of the IPAM scope.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
ipam_scope_id
FROM awscc.ec2.ipam_scopes
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>ipam_scopes</code> resource, the following permissions are required:

### Create
```json
ec2:CreateIpamScope,
ec2:DescribeIpamScopes,
ec2:CreateTags
```

### List
```json
ec2:DescribeIpamScopes
```

