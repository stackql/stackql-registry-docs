---
title: connector_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - connector_profiles
  - appflow
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>connector_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connector_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>connector_profiles</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.appflow.connector_profiles</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>connector_profile_name</code></td><td><code>string</code></td><td>The maximum number of items to retrieve in a single batch.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>connector_profiles</code> resource, the following permissions are required:

### Create
```json
appflow:CreateConnectorProfile,
kms:ListKeys,
kms:DescribeKey,
kms:ListAliases,
kms:CreateGrant,
kms:ListGrants,
iam:PassRole,
secretsmanager:CreateSecret,
secretsmanager:GetSecretValue,
secretsmanager:PutResourcePolicy
```

### List
```json
appflow:DescribeConnectorProfiles
```


## Example
```sql
SELECT
region,
connector_profile_name
FROM awscc.appflow.connector_profiles
WHERE region = 'us-east-1'
```
