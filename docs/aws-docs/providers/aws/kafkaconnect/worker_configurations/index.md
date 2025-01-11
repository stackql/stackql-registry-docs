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

Creates, updates, deletes or gets a <code>worker_configuration</code> resource or lists <code>worker_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>worker_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The configuration of the workers, which are the processes that run the connector logic.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kafkaconnect.worker_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the worker configuration.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A summary description of the worker configuration.</td></tr>
<tr><td><CopyableCode code="worker_configuration_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the custom configuration.</td></tr>
<tr><td><CopyableCode code="properties_file_content" /></td><td><code>string</code></td><td>Base64 encoded contents of connect-distributed.properties file.</td></tr>
<tr><td><CopyableCode code="revision" /></td><td><code>integer</code></td><td>The description of a revision of the worker configuration.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-workerconfiguration.html"><code>AWS::KafkaConnect::WorkerConfiguration</code></a>.

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
    <td><CopyableCode code="Name, PropertiesFileContent, region" /></td>
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
Gets all <code>worker_configurations</code> in a region.
```sql
SELECT
region,
name,
description,
worker_configuration_arn,
properties_file_content,
revision,
tags
FROM aws.kafkaconnect.worker_configurations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>worker_configuration</code>.
```sql
SELECT
region,
name,
description,
worker_configuration_arn,
properties_file_content,
revision,
tags
FROM aws.kafkaconnect.worker_configurations
WHERE region = 'us-east-1' AND data__Identifier = '<WorkerConfigurationArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>worker_configuration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.kafkaconnect.worker_configurations (
 Name,
 PropertiesFileContent,
 region
)
SELECT 
'{{ Name }}',
 '{{ PropertiesFileContent }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.kafkaconnect.worker_configurations (
 Name,
 Description,
 PropertiesFileContent,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ PropertiesFileContent }}',
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
  - name: worker_configuration
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: PropertiesFileContent
        value: '{{ PropertiesFileContent }}'
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

### Read
```json
kafkaconnect:DescribeWorkerConfiguration,
kafkaconnect:ListTagsForResource
```

### Update
```json
kafkaconnect:DescribeWorkerConfiguration,
kafkaconnect:ListTagsForResource,
kafkaconnect:TagResource,
kafkaconnect:UntagResource
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
