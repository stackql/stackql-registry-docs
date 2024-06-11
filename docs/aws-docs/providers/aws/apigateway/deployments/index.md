---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - apigateway
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

Creates, updates, deletes or gets a <code>deployment</code> resource or lists <code>deployments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGateway::Deployment</code> resource deploys an API Gateway <code>RestApi</code> resource to a stage so that clients can call the API over the internet. The stage acts as an environment.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.deployments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="deployment_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description for the Deployment resource to create.</td></tr>
<tr><td><CopyableCode code="stage_description" /></td><td><code>object</code></td><td>The description of the Stage resource for the Deployment resource to create. To specify a stage description, you must also provide a stage name.</td></tr>
<tr><td><CopyableCode code="stage_name" /></td><td><code>string</code></td><td>The name of the Stage resource for the Deployment resource to create.</td></tr>
<tr><td><CopyableCode code="rest_api_id" /></td><td><code>string</code></td><td>The string identifier of the associated RestApi.</td></tr>
<tr><td><CopyableCode code="deployment_canary_settings" /></td><td><code>object</code></td><td>The input configuration for a canary deployment.</td></tr>
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
    <td><CopyableCode code="RestApiId, region" /></td>
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
List all <code>deployments</code> in a region.
```sql
SELECT
region,
deployment_id,
rest_api_id
FROM aws.apigateway.deployments
WHERE region = 'us-east-1';
```
Gets all properties from a <code>deployment</code>.
```sql
SELECT
region,
deployment_id,
description,
stage_description,
stage_name,
rest_api_id,
deployment_canary_settings
FROM aws.apigateway.deployments
WHERE region = 'us-east-1' AND data__Identifier = '<DeploymentId>|<RestApiId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>deployment</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.apigateway.deployments (
 RestApiId,
 region
)
SELECT 
'{{ RestApiId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.apigateway.deployments (
 Description,
 StageDescription,
 StageName,
 RestApiId,
 DeploymentCanarySettings,
 region
)
SELECT 
 '{{ Description }}',
 '{{ StageDescription }}',
 '{{ StageName }}',
 '{{ RestApiId }}',
 '{{ DeploymentCanarySettings }}',
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
  - name: deployment
    props:
      - name: Description
        value: '{{ Description }}'
      - name: StageDescription
        value:
          CacheTtlInSeconds: '{{ CacheTtlInSeconds }}'
          Description: '{{ Description }}'
          LoggingLevel: '{{ LoggingLevel }}'
          CanarySetting:
            DeploymentId: '{{ DeploymentId }}'
            PercentTraffic: null
            StageVariableOverrides: {}
            UseStageCache: '{{ UseStageCache }}'
          ThrottlingRateLimit: null
          ClientCertificateId: '{{ ClientCertificateId }}'
          Variables: {}
          DocumentationVersion: '{{ DocumentationVersion }}'
          CacheDataEncrypted: '{{ CacheDataEncrypted }}'
          DataTraceEnabled: '{{ DataTraceEnabled }}'
          ThrottlingBurstLimit: '{{ ThrottlingBurstLimit }}'
          CachingEnabled: '{{ CachingEnabled }}'
          TracingEnabled: '{{ TracingEnabled }}'
          MethodSettings:
            - CacheDataEncrypted: '{{ CacheDataEncrypted }}'
              CacheTtlInSeconds: '{{ CacheTtlInSeconds }}'
              CachingEnabled: '{{ CachingEnabled }}'
              DataTraceEnabled: '{{ DataTraceEnabled }}'
              HttpMethod: '{{ HttpMethod }}'
              LoggingLevel: '{{ LoggingLevel }}'
              MetricsEnabled: '{{ MetricsEnabled }}'
              ResourcePath: '{{ ResourcePath }}'
              ThrottlingBurstLimit: '{{ ThrottlingBurstLimit }}'
              ThrottlingRateLimit: null
          AccessLogSetting:
            DestinationArn: '{{ DestinationArn }}'
            Format: '{{ Format }}'
          CacheClusterSize: '{{ CacheClusterSize }}'
          MetricsEnabled: '{{ MetricsEnabled }}'
          Tags:
            - Value: '{{ Value }}'
              Key: '{{ Key }}'
          CacheClusterEnabled: '{{ CacheClusterEnabled }}'
      - name: StageName
        value: '{{ StageName }}'
      - name: RestApiId
        value: '{{ RestApiId }}'
      - name: DeploymentCanarySettings
        value:
          StageVariableOverrides: {}
          PercentTraffic: null
          UseStageCache: '{{ UseStageCache }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.apigateway.deployments
WHERE data__Identifier = '<DeploymentId|RestApiId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>deployments</code> resource, the following permissions are required:

### Read
```json
apigateway:GET
```

### Create
```json
apigateway:POST,
apigateway:PATCH,
apigateway:PUT,
apigateway:GET
```

### Update
```json
apigateway:PATCH,
apigateway:GET,
apigateway:PUT,
apigateway:DELETE
```

### List
```json
apigateway:GET
```

### Delete
```json
apigateway:GET,
apigateway:DELETE
```

