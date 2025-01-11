---
title: pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - pipelines
  - osis
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

Creates, updates, deletes or gets a <code>pipeline</code> resource or lists <code>pipelines</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An OpenSearch Ingestion Service Data Prepper pipeline running Data Prepper.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.osis.pipelines" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="buffer_options" /></td><td><code>object</code></td><td>Key-value pairs to configure buffering.</td></tr>
<tr><td><CopyableCode code="encryption_at_rest_options" /></td><td><code>object</code></td><td>Key-value pairs to configure encryption at rest.</td></tr>
<tr><td><CopyableCode code="log_publishing_options" /></td><td><code>object</code></td><td>Key-value pairs to configure log publishing.</td></tr>
<tr><td><CopyableCode code="max_units" /></td><td><code>integer</code></td><td>The maximum pipeline capacity, in Ingestion OpenSearch Compute Units (OCUs).</td></tr>
<tr><td><CopyableCode code="min_units" /></td><td><code>integer</code></td><td>The minimum pipeline capacity, in Ingestion OpenSearch Compute Units (OCUs).</td></tr>
<tr><td><CopyableCode code="pipeline_configuration_body" /></td><td><code>string</code></td><td>The Data Prepper pipeline configuration.</td></tr>
<tr><td><CopyableCode code="pipeline_name" /></td><td><code>string</code></td><td>Name of the OpenSearch Ingestion Service pipeline to create. Pipeline names are unique across the pipelines owned by an account within an AWS Region.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="vpc_options" /></td><td><code>object</code></td><td>Container for the values required to configure VPC access for the pipeline. If you don't specify these values, OpenSearch Ingestion Service creates the pipeline with a public endpoint.</td></tr>
<tr><td><CopyableCode code="vpc_endpoints" /></td><td><code>array</code></td><td>The VPC interface endpoints that have access to the pipeline.</td></tr>
<tr><td><CopyableCode code="vpc_endpoint_service" /></td><td><code>string</code></td><td>The VPC endpoint service name for the pipeline.</td></tr>
<tr><td><CopyableCode code="pipeline_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the pipeline.</td></tr>
<tr><td><CopyableCode code="ingest_endpoint_urls" /></td><td><code>array</code></td><td>A list of endpoints that can be used for ingesting data into a pipeline</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-osis-pipeline.html"><code>AWS::OSIS::Pipeline</code></a>.

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
    <td><CopyableCode code="MaxUnits, MinUnits, PipelineConfigurationBody, PipelineName, region" /></td>
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
Gets all <code>pipelines</code> in a region.
```sql
SELECT
region,
buffer_options,
encryption_at_rest_options,
log_publishing_options,
max_units,
min_units,
pipeline_configuration_body,
pipeline_name,
tags,
vpc_options,
vpc_endpoints,
vpc_endpoint_service,
pipeline_arn,
ingest_endpoint_urls
FROM aws.osis.pipelines
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>pipeline</code>.
```sql
SELECT
region,
buffer_options,
encryption_at_rest_options,
log_publishing_options,
max_units,
min_units,
pipeline_configuration_body,
pipeline_name,
tags,
vpc_options,
vpc_endpoints,
vpc_endpoint_service,
pipeline_arn,
ingest_endpoint_urls
FROM aws.osis.pipelines
WHERE region = 'us-east-1' AND data__Identifier = '<PipelineArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>pipeline</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.osis.pipelines (
 MaxUnits,
 MinUnits,
 PipelineConfigurationBody,
 PipelineName,
 region
)
SELECT 
'{{ MaxUnits }}',
 '{{ MinUnits }}',
 '{{ PipelineConfigurationBody }}',
 '{{ PipelineName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.osis.pipelines (
 BufferOptions,
 EncryptionAtRestOptions,
 LogPublishingOptions,
 MaxUnits,
 MinUnits,
 PipelineConfigurationBody,
 PipelineName,
 Tags,
 VpcOptions,
 region
)
SELECT 
 '{{ BufferOptions }}',
 '{{ EncryptionAtRestOptions }}',
 '{{ LogPublishingOptions }}',
 '{{ MaxUnits }}',
 '{{ MinUnits }}',
 '{{ PipelineConfigurationBody }}',
 '{{ PipelineName }}',
 '{{ Tags }}',
 '{{ VpcOptions }}',
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
  - name: pipeline
    props:
      - name: BufferOptions
        value:
          PersistentBufferEnabled: '{{ PersistentBufferEnabled }}'
      - name: EncryptionAtRestOptions
        value:
          KmsKeyArn: '{{ KmsKeyArn }}'
      - name: LogPublishingOptions
        value:
          IsLoggingEnabled: '{{ IsLoggingEnabled }}'
          CloudWatchLogDestination:
            LogGroup: '{{ LogGroup }}'
      - name: MaxUnits
        value: '{{ MaxUnits }}'
      - name: MinUnits
        value: '{{ MinUnits }}'
      - name: PipelineConfigurationBody
        value: '{{ PipelineConfigurationBody }}'
      - name: PipelineName
        value: '{{ PipelineName }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: VpcOptions
        value:
          SecurityGroupIds:
            - '{{ SecurityGroupIds[0] }}'
          SubnetIds:
            - '{{ SubnetIds[0] }}'
          VpcEndpointManagement: '{{ VpcEndpointManagement }}'
          VpcAttachmentOptions:
            AttachToVpc: '{{ AttachToVpc }}'
            CidrBlock: '{{ CidrBlock }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.osis.pipelines
WHERE data__Identifier = '<PipelineArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>pipelines</code> resource, the following permissions are required:

### Create
```json
osis:CreatePipeline,
osis:GetPipeline,
osis:TagResource,
osis:ListTagsForResource,
iam:PassRole,
iam:CreateServiceLinkedRole,
logs:CreateLogDelivery,
kms:DescribeKey
```

### Read
```json
osis:GetPipeline,
osis:ListTagsForResource
```

### Update
```json
osis:UpdatePipeline,
osis:GetPipeline,
osis:ListTagsForResource,
osis:TagResource,
osis:UntagResource,
iam:PassRole,
logs:GetLogDelivery,
logs:UpdateLogDelivery,
logs:ListLogDeliveries,
kms:DescribeKey
```

### Delete
```json
osis:DeletePipeline,
osis:GetPipeline,
logs:GetLogDelivery,
logs:DeleteLogDelivery,
logs:ListLogDeliveries
```

### List
```json
osis:ListPipelines
```
