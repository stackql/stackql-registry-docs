---
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
  - opsworkscm
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>servers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>servers</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.opsworkscm.servers</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>server_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
server_name
FROM awscc.opsworkscm.servers
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>servers</code> resource, the following permissions are required:

### Create
```json
opsworks-cm:CreateServer,
opsworks-cm:DescribeServers,
iam:PassRole
```

### List
```json
opsworks-cm:DescribeServers,
opsworks-cm:ListTagsForResource
```

