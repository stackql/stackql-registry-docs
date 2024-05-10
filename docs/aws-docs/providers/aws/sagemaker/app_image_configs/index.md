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


Used to retrieve a list of <code>app_image_configs</code> in a region or to create or delete a <code>app_image_configs</code> resource, use <code>app_image_config</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app_image_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::AppImageConfig</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.app_image_configs" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="app_image_config_name" /></td><td><code>string</code></td><td>The Name of the AppImageConfig.</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
app_image_config_name
FROM aws.sagemaker.app_image_configs
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>app_image_config</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- app_image_config.iql (required properties only)
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
-- app_image_config.iql (all properties)
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

## `DELETE` Example

```sql
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

### Delete
```json
sagemaker:DeleteAppImageConfig,
sagemaker:DescribeAppImageConfig
```

### List
```json
sagemaker:ListAppImageConfigs
```

