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


Used to retrieve a list of <code>deployments</code> in a region or to create or delete a <code>deployments</code> resource, use <code>deployment</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ApiGateway::Deployment`` resource deploys an API Gateway ``RestApi`` resource to a stage so that clients can call the API over the internet. The stage acts as an environment.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.deployments" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="deployment_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rest_api_id" /></td><td><code>string</code></td><td>The string identifier of the associated RestApi.</td></tr>
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
deployment_id,
rest_api_id
FROM aws.apigateway.deployments
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>deployment</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- deployment.iql (required properties only)
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
-- deployment.iql (all properties)
INSERT INTO aws.apigateway.deployments (
 DeploymentCanarySettings,
 Description,
 RestApiId,
 StageDescription,
 StageName,
 region
)
SELECT 
 '{{ DeploymentCanarySettings }}',
 '{{ Description }}',
 '{{ RestApiId }}',
 '{{ StageDescription }}',
 '{{ StageName }}',
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
      - name: DeploymentCanarySettings
        value:
          PercentTraffic: null
          StageVariableOverrides: {}
          UseStageCache: '{{ UseStageCache }}'
      - name: Description
        value: '{{ Description }}'
      - name: RestApiId
        value: '{{ RestApiId }}'
      - name: StageDescription
        value:
          AccessLogSetting:
            DestinationArn: '{{ DestinationArn }}'
            Format: '{{ Format }}'
          CacheClusterEnabled: '{{ CacheClusterEnabled }}'
          CacheClusterSize: '{{ CacheClusterSize }}'
          CacheDataEncrypted: '{{ CacheDataEncrypted }}'
          CacheTtlInSeconds: '{{ CacheTtlInSeconds }}'
          CachingEnabled: '{{ CachingEnabled }}'
          CanarySetting:
            DeploymentId: '{{ DeploymentId }}'
            PercentTraffic: null
            StageVariableOverrides: {}
            UseStageCache: '{{ UseStageCache }}'
          ClientCertificateId: '{{ ClientCertificateId }}'
          DataTraceEnabled: '{{ DataTraceEnabled }}'
          Description: '{{ Description }}'
          DocumentationVersion: '{{ DocumentationVersion }}'
          LoggingLevel: '{{ LoggingLevel }}'
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
          MetricsEnabled: '{{ MetricsEnabled }}'
          Tags:
            - Value: '{{ Value }}'
              Key: '{{ Key }}'
          ThrottlingBurstLimit: '{{ ThrottlingBurstLimit }}'
          ThrottlingRateLimit: null
          TracingEnabled: '{{ TracingEnabled }}'
          Variables: {}
      - name: StageName
        value: '{{ StageName }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.apigateway.deployments
WHERE data__Identifier = '<DeploymentId|RestApiId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>deployments</code> resource, the following permissions are required:

### Create
```json
apigateway:POST,
apigateway:PATCH,
apigateway:PUT,
apigateway:GET
```

### Delete
```json
apigateway:GET,
apigateway:DELETE
```

### List
```json
apigateway:GET
```

