---
title: flows
hide_title: false
hide_table_of_contents: false
keywords:
  - flows
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

Used to retrieve a list of <code>flows</code> in a region or create a <code>flows</code> resource, use <code>flow</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::AppFlow::Flow.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appflow.flows" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="flow_name" /></td><td><code>string</code></td><td>Name of the flow.</td></tr>
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
flow_name
FROM aws.appflow.flows
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>flows</code> resource, the following permissions are required:

### Create
```json
appflow:CreateFlow,
appflow:StartFlow,
appflow:TagResource,
appflow:ListTagsForResource,
appflow:UseConnectorProfile,
iam:PassRole,
s3:ListAllMyBuckets,
s3:GetBucketLocation,
s3:GetBucketPolicy,
kms:ListGrants,
kms:ListKeys,
kms:DescribeKey,
kms:ListAliases,
kms:CreateGrant,
secretsmanager:CreateSecret,
secretsmanager:PutResourcePolicy
```

### List
```json
appflow:ListFlows
```

