---
title: app_image_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - app_image_configs
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

Creates, updates, deletes or gets an <code>app_image_config</code> resource or lists <code>app_image_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app_image_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::AppImageConfig</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.app_image_configs" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="app_image_config_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the AppImageConfig.</td></tr>
<tr><td><CopyableCode code="app_image_config_name" /></td><td><code>string</code></td><td>The Name of the AppImageConfig.</td></tr>
<tr><td><CopyableCode code="kernel_gateway_image_config" /></td><td><code>object</code></td><td>The KernelGatewayImageConfig.</td></tr>
<tr><td><CopyableCode code="jupyter_lab_app_image_config" /></td><td><code>object</code></td><td>The JupyterLabAppImageConfig.</td></tr>
<tr><td><CopyableCode code="code_editor_app_image_config" /></td><td><code>object</code></td><td>The CodeEditorAppImageConfig.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of tags to apply to the AppImageConfig.</td></tr>
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
    <td><CopyableCode code="AppImageConfigName, region" /></td>
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
Gets all <code>app_image_configs</code> in a region.
```sql
SELECT
region,
app_image_config_arn,
app_image_config_name,
kernel_gateway_image_config,
jupyter_lab_app_image_config,
code_editor_app_image_config,
tags
FROM aws.sagemaker.app_image_configs
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>app_image_config</code>.
```sql
SELECT
region,
app_image_config_arn,
app_image_config_name,
kernel_gateway_image_config,
jupyter_lab_app_image_config,
code_editor_app_image_config,
tags
FROM aws.sagemaker.app_image_configs
WHERE region = 'us-east-1' AND data__Identifier = '<AppImageConfigName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>app_image_config</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.sagemaker.app_image_configs (
 AppImageConfigName,
 region
)
SELECT 
'{{ AppImageConfigName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.sagemaker.app_image_configs (
 AppImageConfigName,
 KernelGatewayImageConfig,
 JupyterLabAppImageConfig,
 CodeEditorAppImageConfig,
 Tags,
 region
)
SELECT 
 '{{ AppImageConfigName }}',
 '{{ KernelGatewayImageConfig }}',
 '{{ JupyterLabAppImageConfig }}',
 '{{ CodeEditorAppImageConfig }}',
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
  - name: app_image_config
    props:
      - name: AppImageConfigName
        value: '{{ AppImageConfigName }}'
      - name: KernelGatewayImageConfig
        value:
          FileSystemConfig:
            DefaultGid: '{{ DefaultGid }}'
            DefaultUid: '{{ DefaultUid }}'
            MountPath: '{{ MountPath }}'
          KernelSpecs:
            - DisplayName: '{{ DisplayName }}'
              Name: '{{ Name }}'
      - name: JupyterLabAppImageConfig
        value:
          ContainerConfig:
            ContainerArguments:
              - '{{ ContainerArguments[0] }}'
            ContainerEntrypoint:
              - '{{ ContainerEntrypoint[0] }}'
            ContainerEnvironmentVariables:
              - Value: '{{ Value }}'
                Key: '{{ Key }}'
      - name: CodeEditorAppImageConfig
        value:
          ContainerConfig: null
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
DELETE FROM aws.sagemaker.app_image_configs
WHERE data__Identifier = '<AppImageConfigName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>app_image_configs</code> resource, the following permissions are required:

### Create
```json
sagemaker:CreateAppImageConfig,
sagemaker:DescribeAppImageConfig
```

### Read
```json
sagemaker:DescribeAppImageConfig
```

### Update
```json
sagemaker:UpdateAppImageConfig,
sagemaker:DescribeAppImageConfig
```

### Delete
```json
sagemaker:DeleteAppImageConfig,
sagemaker:DescribeAppImageConfig
```

### List
```json
sagemaker:ListAppImageConfigs
```

