---
title: studio_lifecycle_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - studio_lifecycle_configs
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

Creates, updates, deletes or gets a <code>studio_lifecycle_config</code> resource or lists <code>studio_lifecycle_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>studio_lifecycle_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::StudioLifecycleConfig</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.studio_lifecycle_configs" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="studio_lifecycle_config_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Lifecycle Configuration.</td></tr>
<tr><td><CopyableCode code="studio_lifecycle_config_app_type" /></td><td><code>string</code></td><td>The App type that the Lifecycle Configuration is attached to.</td></tr>
<tr><td><CopyableCode code="studio_lifecycle_config_content" /></td><td><code>string</code></td><td>The content of your Amazon SageMaker Studio Lifecycle Configuration script. This content must be base64 encoded.</td></tr>
<tr><td><CopyableCode code="studio_lifecycle_config_name" /></td><td><code>string</code></td><td>The name of the Amazon SageMaker Studio Lifecycle Configuration.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags to be associated with the Lifecycle Configuration. Each tag consists of a key and an optional value. Tag keys must be unique per resource. Tags are searchable using the Search API.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-studiolifecycleconfig.html"><code>AWS::SageMaker::StudioLifecycleConfig</code></a>.

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
    <td><CopyableCode code="StudioLifecycleConfigAppType, StudioLifecycleConfigContent, StudioLifecycleConfigName, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
Gets all <code>studio_lifecycle_configs</code> in a region.
```sql
SELECT
region,
studio_lifecycle_config_arn,
studio_lifecycle_config_app_type,
studio_lifecycle_config_content,
studio_lifecycle_config_name,
tags
FROM aws.sagemaker.studio_lifecycle_configs
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>studio_lifecycle_config</code>.
```sql
SELECT
region,
studio_lifecycle_config_arn,
studio_lifecycle_config_app_type,
studio_lifecycle_config_content,
studio_lifecycle_config_name,
tags
FROM aws.sagemaker.studio_lifecycle_configs
WHERE region = 'us-east-1' AND data__Identifier = '<StudioLifecycleConfigName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>studio_lifecycle_config</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.sagemaker.studio_lifecycle_configs (
 StudioLifecycleConfigAppType,
 StudioLifecycleConfigContent,
 StudioLifecycleConfigName,
 region
)
SELECT 
'{{ StudioLifecycleConfigAppType }}',
 '{{ StudioLifecycleConfigContent }}',
 '{{ StudioLifecycleConfigName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.sagemaker.studio_lifecycle_configs (
 StudioLifecycleConfigAppType,
 StudioLifecycleConfigContent,
 StudioLifecycleConfigName,
 Tags,
 region
)
SELECT 
 '{{ StudioLifecycleConfigAppType }}',
 '{{ StudioLifecycleConfigContent }}',
 '{{ StudioLifecycleConfigName }}',
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
  - name: studio_lifecycle_config
    props:
      - name: StudioLifecycleConfigAppType
        value: '{{ StudioLifecycleConfigAppType }}'
      - name: StudioLifecycleConfigContent
        value: '{{ StudioLifecycleConfigContent }}'
      - name: StudioLifecycleConfigName
        value: '{{ StudioLifecycleConfigName }}'
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
DELETE FROM aws.sagemaker.studio_lifecycle_configs
WHERE data__Identifier = '<StudioLifecycleConfigName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>studio_lifecycle_configs</code> resource, the following permissions are required:

### Create
```json
sagemaker:CreateStudioLifecycleConfig,
sagemaker:DescribeStudioLifecycleConfig,
sagemaker:AddTags,
sagemaker:ListTags
```

### Read
```json
sagemaker:DescribeStudioLifecycleConfig,
sagemaker:ListTags
```

### Delete
```json
sagemaker:DeleteStudioLifecycleConfig,
sagemaker:DescribeStudioLifecycleConfig,
sagemaker:DeleteTags,
sagemaker:ListTags
```

### List
```json
sagemaker:ListStudioLifecycleConfigs,
sagemaker:ListTags
```
