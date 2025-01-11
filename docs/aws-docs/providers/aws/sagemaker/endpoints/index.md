---
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
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

Creates, updates, deletes or gets an <code>endpoint</code> resource or lists <code>endpoints</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::Endpoint</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.endpoints" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="deployment_config" /></td><td><code>object</code></td><td>Specifies deployment configuration for updating the SageMaker endpoint. Includes rollback and update policies.</td></tr>
<tr><td><CopyableCode code="endpoint_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the endpoint.</td></tr>
<tr><td><CopyableCode code="endpoint_config_name" /></td><td><code>string</code></td><td>The name of the endpoint configuration for the SageMaker endpoint. This is a required property.</td></tr>
<tr><td><CopyableCode code="endpoint_name" /></td><td><code>string</code></td><td>The name of the SageMaker endpoint. This name must be unique within an AWS Region.</td></tr>
<tr><td><CopyableCode code="exclude_retained_variant_properties" /></td><td><code>array</code></td><td>Specifies a list of variant properties that you want to exclude when updating an endpoint.</td></tr>
<tr><td><CopyableCode code="retain_all_variant_properties" /></td><td><code>boolean</code></td><td>When set to true, retains all variant properties for an endpoint when it is updated.</td></tr>
<tr><td><CopyableCode code="retain_deployment_config" /></td><td><code>boolean</code></td><td>When set to true, retains the deployment configuration during endpoint updates.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html"><code>AWS::SageMaker::Endpoint</code></a>.

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
    <td><CopyableCode code="EndpointConfigName, region" /></td>
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
Gets all <code>endpoints</code> in a region.
```sql
SELECT
region,
deployment_config,
endpoint_arn,
endpoint_config_name,
endpoint_name,
exclude_retained_variant_properties,
retain_all_variant_properties,
retain_deployment_config,
tags
FROM aws.sagemaker.endpoints
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>endpoint</code>.
```sql
SELECT
region,
deployment_config,
endpoint_arn,
endpoint_config_name,
endpoint_name,
exclude_retained_variant_properties,
retain_all_variant_properties,
retain_deployment_config,
tags
FROM aws.sagemaker.endpoints
WHERE region = 'us-east-1' AND data__Identifier = '<EndpointArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>endpoint</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.sagemaker.endpoints (
 EndpointConfigName,
 region
)
SELECT 
'{{ EndpointConfigName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.sagemaker.endpoints (
 DeploymentConfig,
 EndpointConfigName,
 ExcludeRetainedVariantProperties,
 RetainAllVariantProperties,
 RetainDeploymentConfig,
 Tags,
 region
)
SELECT 
 '{{ DeploymentConfig }}',
 '{{ EndpointConfigName }}',
 '{{ ExcludeRetainedVariantProperties }}',
 '{{ RetainAllVariantProperties }}',
 '{{ RetainDeploymentConfig }}',
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
  - name: endpoint
    props:
      - name: DeploymentConfig
        value:
          AutoRollbackConfiguration:
            Alarms:
              - AlarmName: '{{ AlarmName }}'
          BlueGreenUpdatePolicy:
            MaximumExecutionTimeoutInSeconds: '{{ MaximumExecutionTimeoutInSeconds }}'
            TerminationWaitInSeconds: '{{ TerminationWaitInSeconds }}'
            TrafficRoutingConfiguration:
              CanarySize:
                Type: '{{ Type }}'
                Value: '{{ Value }}'
              LinearStepSize: null
              Type: '{{ Type }}'
              WaitIntervalInSeconds: '{{ WaitIntervalInSeconds }}'
          RollingUpdatePolicy:
            MaximumBatchSize: null
            MaximumExecutionTimeoutInSeconds: '{{ MaximumExecutionTimeoutInSeconds }}'
            RollbackMaximumBatchSize: null
            WaitIntervalInSeconds: '{{ WaitIntervalInSeconds }}'
      - name: EndpointConfigName
        value: '{{ EndpointConfigName }}'
      - name: ExcludeRetainedVariantProperties
        value:
          - VariantPropertyType: '{{ VariantPropertyType }}'
      - name: RetainAllVariantProperties
        value: '{{ RetainAllVariantProperties }}'
      - name: RetainDeploymentConfig
        value: '{{ RetainDeploymentConfig }}'
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
DELETE FROM aws.sagemaker.endpoints
WHERE data__Identifier = '<EndpointArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>endpoints</code> resource, the following permissions are required:

### Create
```json
sagemaker:CreateEndpoint,
sagemaker:DescribeEndpoint,
sagemaker:AddTags
```

### Read
```json
sagemaker:DescribeEndpoint,
sagemaker:ListTags
```

### Update
```json
sagemaker:UpdateEndpoint,
sagemaker:DescribeEndpoint,
sagemaker:AddTags,
sagemaker:DeleteTags
```

### Delete
```json
sagemaker:DeleteEndpoint,
sagemaker:DescribeEndpoint
```

### List
```json
sagemaker:ListEndpoints
```
