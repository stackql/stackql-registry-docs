---
title: connector_profile
hide_title: false
hide_table_of_contents: false
keywords:
  - connector_profile
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>connector_profile</code> resource, use <code>connector_profiles</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connector_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppFlow::ConnectorProfile</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appflow.connector_profile" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="connector_profile_arn" /></td><td><code>string</code></td><td>Unique identifier for connector profile resources</td></tr>
<tr><td><CopyableCode code="connector_label" /></td><td><code>string</code></td><td>The label of the connector. The label is unique for each ConnectorRegistration in your AWS account. Only needed if calling for CUSTOMCONNECTOR connector type&#x2F;.</td></tr>
<tr><td><CopyableCode code="connector_profile_name" /></td><td><code>string</code></td><td>The maximum number of items to retrieve in a single batch.</td></tr>
<tr><td><CopyableCode code="kms_arn" /></td><td><code>string</code></td><td>The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.</td></tr>
<tr><td><CopyableCode code="connector_type" /></td><td><code>string</code></td><td>List of Saas providers that need connector profile to be created</td></tr>
<tr><td><CopyableCode code="connection_mode" /></td><td><code>string</code></td><td>Mode in which data transfer should be enabled. Private connection mode is currently enabled for Salesforce, Snowflake, Trendmicro and Singular</td></tr>
<tr><td><CopyableCode code="connector_profile_config" /></td><td><code>object</code></td><td>Connector specific configurations needed to create connector profile</td></tr>
<tr><td><CopyableCode code="credentials_arn" /></td><td><code>string</code></td><td>A unique Arn for Connector-Profile resource</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
connector_profile_arn,
connector_label,
connector_profile_name,
kms_arn,
connector_type,
connection_mode,
connector_profile_config,
credentials_arn
FROM aws.appflow.connector_profile
WHERE region = 'us-east-1' AND data__Identifier = '<ConnectorProfileName>';
```


## Permissions

To operate on the <code>connector_profile</code> resource, the following permissions are required:

### Read
```json
appflow:DescribeConnectorProfiles
```

### Update
```json
appflow:UpdateConnectorProfile,
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

