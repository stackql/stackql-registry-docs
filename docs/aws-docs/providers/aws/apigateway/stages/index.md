---
title: stages
hide_title: false
hide_table_of_contents: false
keywords:
  - stages
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

Creates, updates, deletes or gets a <code>stage</code> resource or lists <code>stages</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGateway::Stage</code> resource creates a stage for a deployment.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.stages" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="access_log_setting" /></td><td><code>object</code></td><td>The <code>AccessLogSetting</code> property type specifies settings for logging access in this stage.<br /><code>AccessLogSetting</code> is a property of the &#91;AWS::ApiGateway::Stage&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.html) resource.</td></tr>
<tr><td><CopyableCode code="cache_cluster_enabled" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="cache_cluster_size" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="canary_setting" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="client_certificate_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="deployment_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="documentation_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="method_settings" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="rest_api_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stage_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tracing_enabled" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="variables" /></td><td><code>object</code></td><td>A map (string-to-string map) that defines the stage variables, where the variable name is the key and the variable value is the value. Variable names are limited to alphanumeric characters. Values must match the following regular expression: <code>&#91;A-Za-z0-9-._~:/?#&=,&#93;+</code>.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.html"><code>AWS::ApiGateway::Stage</code></a>.

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
Gets all <code>stages</code> in a region.
```sql
SELECT
region,
access_log_setting,
cache_cluster_enabled,
cache_cluster_size,
canary_setting,
client_certificate_id,
deployment_id,
description,
documentation_version,
method_settings,
rest_api_id,
stage_name,
tags,
tracing_enabled,
variables
FROM aws.apigateway.stages
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>stage</code>.
```sql
SELECT
region,
access_log_setting,
cache_cluster_enabled,
cache_cluster_size,
canary_setting,
client_certificate_id,
deployment_id,
description,
documentation_version,
method_settings,
rest_api_id,
stage_name,
tags,
tracing_enabled,
variables
FROM aws.apigateway.stages
WHERE region = 'us-east-1' AND data__Identifier = '<RestApiId>|<StageName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>stage</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.apigateway.stages (
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
INSERT INTO aws.apigateway.stages (
 AccessLogSetting,
 CacheClusterEnabled,
 CacheClusterSize,
 CanarySetting,
 ClientCertificateId,
 DeploymentId,
 Description,
 DocumentationVersion,
 MethodSettings,
 RestApiId,
 StageName,
 Tags,
 TracingEnabled,
 Variables,
 region
)
SELECT 
 '{{ AccessLogSetting }}',
 '{{ CacheClusterEnabled }}',
 '{{ CacheClusterSize }}',
 '{{ CanarySetting }}',
 '{{ ClientCertificateId }}',
 '{{ DeploymentId }}',
 '{{ Description }}',
 '{{ DocumentationVersion }}',
 '{{ MethodSettings }}',
 '{{ RestApiId }}',
 '{{ StageName }}',
 '{{ Tags }}',
 '{{ TracingEnabled }}',
 '{{ Variables }}',
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
  - name: stage
    props:
      - name: AccessLogSetting
        value:
          DestinationArn: '{{ DestinationArn }}'
          Format: '{{ Format }}'
      - name: CacheClusterEnabled
        value: '{{ CacheClusterEnabled }}'
      - name: CacheClusterSize
        value: '{{ CacheClusterSize }}'
      - name: CanarySetting
        value:
          DeploymentId: '{{ DeploymentId }}'
          PercentTraffic: null
          StageVariableOverrides: {}
          UseStageCache: '{{ UseStageCache }}'
      - name: ClientCertificateId
        value: '{{ ClientCertificateId }}'
      - name: DeploymentId
        value: '{{ DeploymentId }}'
      - name: Description
        value: '{{ Description }}'
      - name: DocumentationVersion
        value: '{{ DocumentationVersion }}'
      - name: MethodSettings
        value:
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
      - name: RestApiId
        value: '{{ RestApiId }}'
      - name: StageName
        value: '{{ StageName }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: TracingEnabled
        value: '{{ TracingEnabled }}'
      - name: Variables
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.apigateway.stages
WHERE data__Identifier = '<RestApiId|StageName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>stages</code> resource, the following permissions are required:

### Create
```json
apigateway:POST,
apigateway:PATCH,
apigateway:GET,
apigateway:PUT
```

### Read
```json
apigateway:GET
```

### Update
```json
apigateway:GET,
apigateway:PATCH,
apigateway:PUT,
apigateway:DELETE
```

### Delete
```json
apigateway:DELETE
```

### List
```json
apigateway:GET
```
