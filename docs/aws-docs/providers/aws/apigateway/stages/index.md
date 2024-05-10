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


Used to retrieve a list of <code>stages</code> in a region or to create or delete a <code>stages</code> resource, use <code>stage</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ApiGateway::Stage`` resource creates a stage for a deployment.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.stages" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="rest_api_id" /></td><td><code>string</code></td><td>The string identifier of the associated RestApi.</td></tr>
<tr><td><CopyableCode code="stage_name" /></td><td><code>string</code></td><td>The name of the stage is the first path segment in the Uniform Resource Identifier (URI) of a call to API Gateway. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.</td></tr>
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
rest_api_id,
stage_name
FROM aws.apigateway.stages
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
 "RestApiId": "{{ RestApiId }}"
}
>>>
--required properties only
INSERT INTO aws.apigateway.stages (
 RestApiId,
 region
)
SELECT 
{{ RestApiId }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AccessLogSetting": {
  "DestinationArn": "{{ DestinationArn }}",
  "Format": "{{ Format }}"
 },
 "CacheClusterEnabled": "{{ CacheClusterEnabled }}",
 "CacheClusterSize": "{{ CacheClusterSize }}",
 "CanarySetting": {
  "DeploymentId": "{{ DeploymentId }}",
  "PercentTraffic": null,
  "StageVariableOverrides": {},
  "UseStageCache": "{{ UseStageCache }}"
 },
 "ClientCertificateId": "{{ ClientCertificateId }}",
 "DeploymentId": "{{ DeploymentId }}",
 "Description": "{{ Description }}",
 "DocumentationVersion": "{{ DocumentationVersion }}",
 "MethodSettings": [
  {
   "CacheDataEncrypted": "{{ CacheDataEncrypted }}",
   "CacheTtlInSeconds": "{{ CacheTtlInSeconds }}",
   "CachingEnabled": "{{ CachingEnabled }}",
   "DataTraceEnabled": "{{ DataTraceEnabled }}",
   "HttpMethod": "{{ HttpMethod }}",
   "LoggingLevel": "{{ LoggingLevel }}",
   "MetricsEnabled": "{{ MetricsEnabled }}",
   "ResourcePath": "{{ ResourcePath }}",
   "ThrottlingBurstLimit": "{{ ThrottlingBurstLimit }}",
   "ThrottlingRateLimit": null
  }
 ],
 "RestApiId": "{{ RestApiId }}",
 "StageName": "{{ StageName }}",
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ],
 "TracingEnabled": "{{ TracingEnabled }}",
 "Variables": {}
}
>>>
--all properties
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
 {{ AccessLogSetting }},
 {{ CacheClusterEnabled }},
 {{ CacheClusterSize }},
 {{ CanarySetting }},
 {{ ClientCertificateId }},
 {{ DeploymentId }},
 {{ Description }},
 {{ DocumentationVersion }},
 {{ MethodSettings }},
 {{ RestApiId }},
 {{ StageName }},
 {{ Tags }},
 {{ TracingEnabled }},
 {{ Variables }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
apigateway:DELETE
```

### List
```json
apigateway:GET
```

