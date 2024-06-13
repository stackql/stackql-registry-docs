---
title: component_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - component_versions
  - greengrassv2
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

Creates, updates, deletes or gets a <code>component_version</code> resource or lists <code>component_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>component_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource for Greengrass component version.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.greengrassv2.component_versions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="component_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="component_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="inline_recipe" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="lambda_function" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="region" /></td>
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
List all <code>component_versions</code> in a region.
```sql
SELECT
region,
arn
FROM aws.greengrassv2.component_versions
WHERE region = 'us-east-1';
```
Gets all properties from a <code>component_version</code>.
```sql
SELECT
region,
arn,
component_name,
component_version,
inline_recipe,
lambda_function,
tags
FROM aws.greengrassv2.component_versions
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>component_version</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.greengrassv2.component_versions (
 InlineRecipe,
 LambdaFunction,
 Tags,
 region
)
SELECT 
'{{ InlineRecipe }}',
 '{{ LambdaFunction }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.greengrassv2.component_versions (
 InlineRecipe,
 LambdaFunction,
 Tags,
 region
)
SELECT 
 '{{ InlineRecipe }}',
 '{{ LambdaFunction }}',
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
  - name: component_version
    props:
      - name: InlineRecipe
        value: '{{ InlineRecipe }}'
      - name: LambdaFunction
        value:
          LambdaArn: '{{ LambdaArn }}'
          ComponentName: '{{ ComponentName }}'
          ComponentVersion: '{{ ComponentVersion }}'
          ComponentPlatforms:
            - Name: '{{ Name }}'
              Attributes: {}
          ComponentDependencies: {}
          ComponentLambdaParameters:
            EventSources:
              - Topic: '{{ Topic }}'
                Type: '{{ Type }}'
            MaxQueueSize: '{{ MaxQueueSize }}'
            MaxInstancesCount: '{{ MaxInstancesCount }}'
            MaxIdleTimeInSeconds: '{{ MaxIdleTimeInSeconds }}'
            TimeoutInSeconds: '{{ TimeoutInSeconds }}'
            StatusTimeoutInSeconds: '{{ StatusTimeoutInSeconds }}'
            Pinned: '{{ Pinned }}'
            InputPayloadEncodingType: '{{ InputPayloadEncodingType }}'
            ExecArgs:
              - '{{ ExecArgs[0] }}'
            EnvironmentVariables: {}
            LinuxProcessParams:
              IsolationMode: '{{ IsolationMode }}'
              ContainerParams:
                MemorySizeInKB: '{{ MemorySizeInKB }}'
                MountROSysfs: '{{ MountROSysfs }}'
                Volumes:
                  - SourcePath: '{{ SourcePath }}'
                    DestinationPath: null
                    Permission: '{{ Permission }}'
                    AddGroupOwner: '{{ AddGroupOwner }}'
                Devices:
                  - Path: null
                    Permission: null
                    AddGroupOwner: null
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.greengrassv2.component_versions
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>component_versions</code> resource, the following permissions are required:

### Create
```json
greengrass:CreateComponentVersion,
greengrass:DescribeComponent,
greengrass:ListTagsForResource,
greengrass:TagResource,
lambda:GetFunction,
s3:GetObject
```

### Read
```json
greengrass:DescribeComponent,
greengrass:ListTagsForResource
```

### Update
```json
greengrass:DescribeComponent,
greengrass:ListTagsForResource,
greengrass:TagResource,
greengrass:UntagResource
```

### Delete
```json
greengrass:DeleteComponent
```

### List
```json
greengrass:ListComponentVersions
```

