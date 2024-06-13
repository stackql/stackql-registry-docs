---
title: account_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - account_policies
  - logs
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

Creates, updates, deletes or gets an <code>account_policy</code> resource or lists <code>account_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Logs::AccountPolicy resource specifies a CloudWatch Logs AccountPolicy.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.logs.account_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="account_id" /></td><td><code>string</code></td><td>User account id</td></tr>
<tr><td><CopyableCode code="policy_name" /></td><td><code>string</code></td><td>The name of the account policy</td></tr>
<tr><td><CopyableCode code="policy_document" /></td><td><code>string</code></td><td>The body of the policy document you want to use for this topic.<br />You can only add one policy per PolicyType.<br />The policy must be in JSON string format.<br />Length Constraints: Maximum length of 30720</td></tr>
<tr><td><CopyableCode code="policy_type" /></td><td><code>string</code></td><td>Type of the policy.</td></tr>
<tr><td><CopyableCode code="scope" /></td><td><code>string</code></td><td>Scope for policy application</td></tr>
<tr><td><CopyableCode code="selection_criteria" /></td><td><code>string</code></td><td>Log group selection criteria to apply policy only to a subset of log groups. SelectionCriteria string can be up to 25KB and cloudwatchlogs determines the length of selectionCriteria by using its UTF-8 bytes</td></tr>
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
    <td><CopyableCode code="PolicyName, PolicyType, PolicyDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>account_policies</code> in a region.
```sql
SELECT
region,
account_id,
policy_type,
policy_name
FROM aws.logs.account_policies
WHERE region = 'us-east-1';
```
Gets all properties from an <code>account_policy</code>.
```sql
SELECT
region,
account_id,
policy_name,
policy_document,
policy_type,
scope,
selection_criteria
FROM aws.logs.account_policies
WHERE region = 'us-east-1' AND data__Identifier = '<AccountId>|<PolicyType>|<PolicyName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>account_policy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.logs.account_policies (
 PolicyName,
 PolicyDocument,
 PolicyType,
 region
)
SELECT 
'{{ PolicyName }}',
 '{{ PolicyDocument }}',
 '{{ PolicyType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.logs.account_policies (
 PolicyName,
 PolicyDocument,
 PolicyType,
 Scope,
 SelectionCriteria,
 region
)
SELECT 
 '{{ PolicyName }}',
 '{{ PolicyDocument }}',
 '{{ PolicyType }}',
 '{{ Scope }}',
 '{{ SelectionCriteria }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: account_policy
    props:
      - name: PolicyName
        value: '{{ PolicyName }}'
      - name: PolicyDocument
        value: '{{ PolicyDocument }}'
      - name: PolicyType
        value: '{{ PolicyType }}'
      - name: Scope
        value: '{{ Scope }}'
      - name: SelectionCriteria
        value: '{{ SelectionCriteria }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.logs.account_policies
WHERE data__Identifier = '<AccountId|PolicyType|PolicyName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>account_policies</code> resource, the following permissions are required:

### Create
```json
logs:PutAccountPolicy,
logs:PutDataProtectionPolicy,
logs:DescribeAccountPolicies,
logs:CreateLogDelivery,
s3:REST.PUT.OBJECT,
firehose:TagDeliveryStream,
logs:PutSubscriptionFilter,
logs:DeleteSubscriptionFilter,
iam:PassRole
```

### Read
```json
logs:DescribeAccountPolicies
```

### Update
```json
logs:PutAccountPolicy,
logs:PutDataProtectionPolicy,
logs:DescribeAccountPolicies,
logs:DeleteAccountPolicy,
logs:DeleteDataProtectionPolicy,
logs:CreateLogDelivery,
logs:PutSubscriptionFilter,
logs:DeleteSubscriptionFilter,
s3:REST.PUT.OBJECT,
firehose:TagDeliveryStream,
iam:PassRole
```

### Delete
```json
logs:DeleteAccountPolicy,
logs:DeleteDataProtectionPolicy,
logs:DescribeAccountPolicies,
logs:DeleteSubscriptionFilter,
iam:PassRole
```

### List
```json
logs:DescribeAccountPolicies
```

