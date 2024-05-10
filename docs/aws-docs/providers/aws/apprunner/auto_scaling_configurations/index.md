---
title: auto_scaling_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - auto_scaling_configurations
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


Used to retrieve a list of <code>auto_scaling_configurations</code> in a region or to create or delete a <code>auto_scaling_configurations</code> resource, use <code>auto_scaling_configuration</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>auto_scaling_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Describes an AWS App Runner automatic configuration resource that enables automatic scaling of instances used to process web requests. You can share an auto scaling configuration across multiple services.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apprunner.auto_scaling_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="auto_scaling_configuration_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of this auto scaling configuration.</td></tr>
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
auto_scaling_configuration_arn
FROM aws.apprunner.auto_scaling_configurations
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "AutoScalingConfigurationName": "{{ AutoScalingConfigurationName }}",
 "MaxConcurrency": "{{ MaxConcurrency }}",
 "MaxSize": "{{ MaxSize }}",
 "MinSize": "{{ MinSize }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.apprunner.auto_scaling_configurations (
 AutoScalingConfigurationName,
 MaxConcurrency,
 MaxSize,
 MinSize,
 Tags,
 region
)
SELECT 
{{ .AutoScalingConfigurationName }},
 {{ .MaxConcurrency }},
 {{ .MaxSize }},
 {{ .MinSize }},
 {{ .Tags }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AutoScalingConfigurationName": "{{ AutoScalingConfigurationName }}",
 "MaxConcurrency": "{{ MaxConcurrency }}",
 "MaxSize": "{{ MaxSize }}",
 "MinSize": "{{ MinSize }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.apprunner.auto_scaling_configurations (
 AutoScalingConfigurationName,
 MaxConcurrency,
 MaxSize,
 MinSize,
 Tags,
 region
)
SELECT 
 {{ .AutoScalingConfigurationName }},
 {{ .MaxConcurrency }},
 {{ .MaxSize }},
 {{ .MinSize }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.apprunner.auto_scaling_configurations
WHERE data__Identifier = '<AutoScalingConfigurationArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>auto_scaling_configurations</code> resource, the following permissions are required:

### Create
```json
apprunner:CreateAutoScalingConfiguration,
apprunner:DescribeAutoScalingConfiguration,
apprunner:TagResource
```

### Delete
```json
apprunner:DeleteAutoScalingConfiguration
```

### List
```json
apprunner:ListAutoScalingConfiguration
```

