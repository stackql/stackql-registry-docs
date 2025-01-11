---
title: target_account_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - target_account_configurations
  - fis
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

Creates, updates, deletes or gets a <code>target_account_configuration</code> resource or lists <code>target_account_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>target_account_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::FIS::TargetAccountConfiguration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.fis.target_account_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="experiment_template_id" /></td><td><code>string</code></td><td>The ID of the experiment template.</td></tr>
<tr><td><CopyableCode code="account_id" /></td><td><code>string</code></td><td>The AWS account ID of the target account.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an IAM role for the target account.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the target account.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-targetaccountconfiguration.html"><code>AWS::FIS::TargetAccountConfiguration</code></a>.

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
    <td><CopyableCode code="ExperimentTemplateId, AccountId, RoleArn, region" /></td>
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
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>target_account_configurations</code> in a region.
```sql
SELECT
region,
experiment_template_id,
account_id,
role_arn,
description
FROM aws.fis.target_account_configurations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>target_account_configuration</code>.
```sql
SELECT
region,
experiment_template_id,
account_id,
role_arn,
description
FROM aws.fis.target_account_configurations
WHERE region = 'us-east-1' AND data__Identifier = '<ExperimentTemplateId>|<AccountId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>target_account_configuration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.fis.target_account_configurations (
 ExperimentTemplateId,
 AccountId,
 RoleArn,
 region
)
SELECT 
'{{ ExperimentTemplateId }}',
 '{{ AccountId }}',
 '{{ RoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.fis.target_account_configurations (
 ExperimentTemplateId,
 AccountId,
 RoleArn,
 Description,
 region
)
SELECT 
 '{{ ExperimentTemplateId }}',
 '{{ AccountId }}',
 '{{ RoleArn }}',
 '{{ Description }}',
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
  - name: target_account_configuration
    props:
      - name: ExperimentTemplateId
        value: '{{ ExperimentTemplateId }}'
      - name: AccountId
        value: '{{ AccountId }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Description
        value: '{{ Description }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.fis.target_account_configurations
WHERE data__Identifier = '<ExperimentTemplateId|AccountId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>target_account_configurations</code> resource, the following permissions are required:

### Create
```json
fis:CreateTargetAccountConfiguration
```

### Read
```json
fis:GetTargetAccountConfiguration
```

### Update
```json
fis:UpdateTargetAccountConfiguration
```

### Delete
```json
fis:DeleteTargetAccountConfiguration
```

### List
```json
fis:ListTargetAccountConfigurations
```
