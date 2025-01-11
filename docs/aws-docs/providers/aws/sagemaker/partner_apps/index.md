---
title: partner_apps
hide_title: false
hide_table_of_contents: false
keywords:
  - partner_apps
  - sagemaker
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

Creates, updates, deletes or gets a <code>partner_app</code> resource or lists <code>partner_apps</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>partner_apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::PartnerApp</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.partner_apps" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the created PartnerApp.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name for the PartnerApp.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of PartnerApp.</td></tr>
<tr><td><CopyableCode code="execution_role_arn" /></td><td><code>string</code></td><td>The execution role for the user.</td></tr>
<tr><td><CopyableCode code="tier" /></td><td><code>string</code></td><td>The tier of the PartnerApp.</td></tr>
<tr><td><CopyableCode code="enable_iam_session_based_identity" /></td><td><code>boolean</code></td><td>Enables IAM Session based Identity for PartnerApp.</td></tr>
<tr><td><CopyableCode code="application_config" /></td><td><code>object</code></td><td>A collection of settings that specify the maintenance schedule for the PartnerApp.</td></tr>
<tr><td><CopyableCode code="auth_type" /></td><td><code>string</code></td><td>The Auth type of PartnerApp.</td></tr>
<tr><td><CopyableCode code="base_url" /></td><td><code>string</code></td><td>The AppServerUrl based on app and account-info.</td></tr>
<tr><td><CopyableCode code="maintenance_config" /></td><td><code>object</code></td><td>A collection of settings that specify the maintenance schedule for the PartnerApp.</td></tr>
<tr><td><CopyableCode code="client_token" /></td><td><code>string</code></td><td>The client token for the PartnerApp.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of tags to apply to the PartnerApp.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-partnerapp.html"><code>AWS::SageMaker::PartnerApp</code></a>.

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
    <td><CopyableCode code="Name, Type, AuthType, ExecutionRoleArn, Tier, region" /></td>
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
Gets all <code>partner_apps</code> in a region.
```sql
SELECT
region,
arn,
name,
type,
execution_role_arn,
tier,
enable_iam_session_based_identity,
application_config,
auth_type,
base_url,
maintenance_config,
client_token,
tags
FROM aws.sagemaker.partner_apps
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>partner_app</code>.
```sql
SELECT
region,
arn,
name,
type,
execution_role_arn,
tier,
enable_iam_session_based_identity,
application_config,
auth_type,
base_url,
maintenance_config,
client_token,
tags
FROM aws.sagemaker.partner_apps
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>partner_app</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.sagemaker.partner_apps (
 Name,
 Type,
 ExecutionRoleArn,
 Tier,
 AuthType,
 region
)
SELECT 
'{{ Name }}',
 '{{ Type }}',
 '{{ ExecutionRoleArn }}',
 '{{ Tier }}',
 '{{ AuthType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.sagemaker.partner_apps (
 Name,
 Type,
 ExecutionRoleArn,
 Tier,
 EnableIamSessionBasedIdentity,
 ApplicationConfig,
 AuthType,
 MaintenanceConfig,
 ClientToken,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Type }}',
 '{{ ExecutionRoleArn }}',
 '{{ Tier }}',
 '{{ EnableIamSessionBasedIdentity }}',
 '{{ ApplicationConfig }}',
 '{{ AuthType }}',
 '{{ MaintenanceConfig }}',
 '{{ ClientToken }}',
 '{{ Tags }}',
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
  - name: partner_app
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Type
        value: '{{ Type }}'
      - name: ExecutionRoleArn
        value: '{{ ExecutionRoleArn }}'
      - name: Tier
        value: '{{ Tier }}'
      - name: EnableIamSessionBasedIdentity
        value: '{{ EnableIamSessionBasedIdentity }}'
      - name: ApplicationConfig
        value:
          AdminUsers:
            - '{{ AdminUsers[0] }}'
          Arguments: {}
      - name: AuthType
        value: '{{ AuthType }}'
      - name: MaintenanceConfig
        value:
          MaintenanceWindowStart: '{{ MaintenanceWindowStart }}'
      - name: ClientToken
        value: '{{ ClientToken }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.sagemaker.partner_apps
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>partner_apps</code> resource, the following permissions are required:

### Create
```json
sagemaker:CreatePartnerApp,
sagemaker:DescribePartnerApp,
sagemaker:AddTags,
sagemaker:ListTags,
iam:PassRole
```

### Read
```json
sagemaker:DescribePartnerApp,
sagemaker:ListTags
```

### Update
```json
sagemaker:UpdatePartnerApp,
sagemaker:DescribePartnerApp,
sagemaker:AddTags,
sagemaker:ListTags,
sagemaker:DeleteTags
```

### Delete
```json
sagemaker:DeletePartnerApp,
sagemaker:DescribePartnerApp,
sagemaker:DeleteTags
```

### List
```json
sagemaker:ListPartnerApps,
sagemaker:DescribePartnerApp,
sagemaker:ListTags
```
