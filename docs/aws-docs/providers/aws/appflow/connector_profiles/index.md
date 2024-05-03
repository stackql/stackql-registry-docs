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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Used to retrieve a list of <code>connector_profiles</code> in a region or create a <code>connector_profiles</code> resource, use <code>connector_profile</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connector_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppFlow::ConnectorProfile</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appflow.connector_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="connector_profile_name" /></td><td><code>string</code></td><td>The maximum number of items to retrieve in a single batch.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
connector_profile_name
FROM aws.appflow.connector_profiles
WHERE region = 'us-east-1'
```

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

