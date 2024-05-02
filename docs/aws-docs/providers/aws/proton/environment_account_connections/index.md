---
title: environment_account_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - environment_account_connections
  - proton
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>environment_account_connections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment_account_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema describing various properties for AWS Proton Environment Account Connections resources.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.proton.environment_account_connections</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the environment account connection.</td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn
FROM aws.proton.environment_account_connections
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>environment_account_connections</code> resource, the following permissions are required:

### Create
```json
proton:CreateEnvironmentAccountConnection,
proton:TagResource,
iam:PassRole,
proton:ListTagsForResource,
proton:GetEnvironmentAccountConnection
```

### List
```json
proton:ListEnvironmentAccountConnections
```

