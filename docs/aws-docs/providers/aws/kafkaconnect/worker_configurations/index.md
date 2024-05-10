---
title: worker_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - worker_configurations
  - kafkaconnect
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


Used to retrieve a list of <code>worker_configurations</code> in a region or to create or delete a <code>worker_configurations</code> resource, use <code>worker_configuration</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>worker_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The configuration of the workers, which are the processes that run the connector logic.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kafkaconnect.worker_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="worker_configuration_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the custom configuration.</td></tr>
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
worker_configuration_arn
FROM aws.kafkaconnect.worker_configurations
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
 "Name": "{{ Name }}",
 "PropertiesFileContent": "{{ PropertiesFileContent }}"
}
>>>
--required properties only
INSERT INTO aws.kafkaconnect.worker_configurations (
 Name,
 PropertiesFileContent,
 region
)
SELECT 
{{ Name }},
 {{ PropertiesFileContent }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "Description": "{{ Description }}",
 "PropertiesFileContent": "{{ PropertiesFileContent }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.kafkaconnect.worker_configurations (
 Name,
 Description,
 PropertiesFileContent,
 Tags,
 region
)
SELECT 
 {{ Name }},
 {{ Description }},
 {{ PropertiesFileContent }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.kafkaconnect.worker_configurations
WHERE data__Identifier = '<WorkerConfigurationArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>worker_configurations</code> resource, the following permissions are required:

### Create
```json
kafkaconnect:DescribeWorkerConfiguration,
kafkaconnect:CreateWorkerConfiguration,
kafkaconnect:TagResource,
kafkaconnect:ListTagsForResource
```

### Delete
```json
kafkaconnect:DescribeWorkerConfiguration,
kafkaconnect:DeleteWorkerConfiguration
```

### List
```json
kafkaconnect:ListWorkerConfigurations
```

