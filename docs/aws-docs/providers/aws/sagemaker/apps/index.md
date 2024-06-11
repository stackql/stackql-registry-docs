---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
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

Creates, updates, deletes or gets an <code>app</code> resource or lists <code>apps</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::App</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.apps" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="app_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the app.</td></tr>
<tr><td><CopyableCode code="app_name" /></td><td><code>string</code></td><td>The name of the app.</td></tr>
<tr><td><CopyableCode code="app_type" /></td><td><code>string</code></td><td>The type of app.</td></tr>
<tr><td><CopyableCode code="domain_id" /></td><td><code>string</code></td><td>The domain ID.</td></tr>
<tr><td><CopyableCode code="resource_spec" /></td><td><code>object</code></td><td>The instance type and the Amazon Resource Name (ARN) of the SageMaker image created on the instance.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of tags to apply to the app.</td></tr>
<tr><td><CopyableCode code="user_profile_name" /></td><td><code>string</code></td><td>The user profile name.</td></tr>
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
    <td><CopyableCode code="AppName, AppType, DomainId, UserProfileName, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
List all <code>apps</code> in a region.
```sql
SELECT
region,
app_name,
app_type,
domain_id,
user_profile_name
FROM aws.sagemaker.apps
WHERE region = 'us-east-1';
```
Gets all properties from an <code>app</code>.
```sql
SELECT
region,
app_arn,
app_name,
app_type,
domain_id,
resource_spec,
tags,
user_profile_name
FROM aws.sagemaker.apps
WHERE region = 'us-east-1' AND data__Identifier = '<AppName>|<AppType>|<DomainId>|<UserProfileName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>app</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.sagemaker.apps (
 AppName,
 AppType,
 DomainId,
 UserProfileName,
 region
)
SELECT 
'{{ AppName }}',
 '{{ AppType }}',
 '{{ DomainId }}',
 '{{ UserProfileName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.sagemaker.apps (
 AppName,
 AppType,
 DomainId,
 ResourceSpec,
 Tags,
 UserProfileName,
 region
)
SELECT 
 '{{ AppName }}',
 '{{ AppType }}',
 '{{ DomainId }}',
 '{{ ResourceSpec }}',
 '{{ Tags }}',
 '{{ UserProfileName }}',
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
  - name: app
    props:
      - name: AppName
        value: '{{ AppName }}'
      - name: AppType
        value: '{{ AppType }}'
      - name: DomainId
        value: '{{ DomainId }}'
      - name: ResourceSpec
        value:
          InstanceType: '{{ InstanceType }}'
          SageMakerImageArn: '{{ SageMakerImageArn }}'
          SageMakerImageVersionArn: '{{ SageMakerImageVersionArn }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: UserProfileName
        value: '{{ UserProfileName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.sagemaker.apps
WHERE data__Identifier = '<AppName|AppType|DomainId|UserProfileName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>apps</code> resource, the following permissions are required:

### Create
```json
sagemaker:CreateApp,
sagemaker:DescribeApp
```

### Read
```json
sagemaker:DescribeApp,
sagemaker:DescribeApp
```

### Delete
```json
sagemaker:DeleteApp,
sagemaker:DescribeApp
```

### List
```json
sagemaker:ListApps
```

