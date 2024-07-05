---
title: observability_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - observability_configurations
  - apprunner
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

Creates, updates, deletes or gets an <code>observability_configuration</code> resource or lists <code>observability_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>observability_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::AppRunner::ObservabilityConfiguration resource is an AWS App Runner resource type that specifies an App Runner observability configuration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apprunner.observability_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="observability_configuration_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of this ObservabilityConfiguration</td></tr>
<tr><td><CopyableCode code="observability_configuration_name" /></td><td><code>string</code></td><td>A name for the observability configuration. When you use it for the first time in an AWS Region, App Runner creates revision number 1 of this name. When you use the same name in subsequent calls, App Runner creates incremental revisions of the configuration.</td></tr>
<tr><td><CopyableCode code="observability_configuration_revision" /></td><td><code>integer</code></td><td>The revision of this observability configuration. It's unique among all the active configurations ('Status': 'ACTIVE') that share the same ObservabilityConfigurationName.</td></tr>
<tr><td><CopyableCode code="latest" /></td><td><code>boolean</code></td><td>It's set to true for the configuration with the highest Revision among all configurations that share the same Name. It's set to false otherwise.</td></tr>
<tr><td><CopyableCode code="trace_configuration" /></td><td><code>object</code></td><td>The configuration of the tracing feature within this observability configuration. If you don't specify it, App Runner doesn't enable tracing.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of metadata items that you can associate with your observability configuration resource. A tag is a key-value pair.</td></tr>
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
    <td><CopyableCode code=", region" /></td>
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
Gets all <code>observability_configurations</code> in a region.
```sql
SELECT
region,
observability_configuration_arn,
observability_configuration_name,
observability_configuration_revision,
latest,
trace_configuration,
tags
FROM aws.apprunner.observability_configurations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>observability_configuration</code>.
```sql
SELECT
region,
observability_configuration_arn,
observability_configuration_name,
observability_configuration_revision,
latest,
trace_configuration,
tags
FROM aws.apprunner.observability_configurations
WHERE region = 'us-east-1' AND data__Identifier = '<ObservabilityConfigurationArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>observability_configuration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.apprunner.observability_configurations (
 ,
 region
)
SELECT 
'{{  }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.apprunner.observability_configurations (
 ObservabilityConfigurationName,
 TraceConfiguration,
 Tags,
 region
)
SELECT 
 '{{ ObservabilityConfigurationName }}',
 '{{ TraceConfiguration }}',
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
  - name: observability_configuration
    props:
      - name: ObservabilityConfigurationName
        value: '{{ ObservabilityConfigurationName }}'
      - name: TraceConfiguration
        value:
          Vendor: '{{ Vendor }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.apprunner.observability_configurations
WHERE data__Identifier = '<ObservabilityConfigurationArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>observability_configurations</code> resource, the following permissions are required:

### Create
```json
apprunner:CreateObservabilityConfiguration,
apprunner:DescribeObservabilityConfiguration,
apprunner:TagResource
```

### Read
```json
apprunner:DescribeObservabilityConfiguration
```

### Delete
```json
apprunner:DeleteObservabilityConfiguration
```

### List
```json
apprunner:ListObservabilityConfigurations
```

