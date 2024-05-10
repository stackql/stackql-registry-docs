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


Used to retrieve a list of <code>observability_configurations</code> in a region or to create or delete a <code>observability_configurations</code> resource, use <code>observability_configuration</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>observability_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::AppRunner::ObservabilityConfiguration resource  is an AWS App Runner resource type that specifies an App Runner observability configuration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apprunner.observability_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="observability_configuration_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of this ObservabilityConfiguration</td></tr>
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
observability_configuration_arn
FROM aws.apprunner.observability_configurations
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>observability_configuration</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- observability_configuration.iql (required properties only)
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
-- observability_configuration.iql (all properties)
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

## `DELETE` Example

```sql
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

### Delete
```json
apprunner:DeleteObservabilityConfiguration
```

### List
```json
apprunner:ListObservabilityConfigurations
```

