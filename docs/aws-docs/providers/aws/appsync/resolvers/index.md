---
title: resolvers
hide_title: false
hide_table_of_contents: false
keywords:
  - resolvers
  - appsync
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

Creates, updates, deletes or gets a <code>resolver</code> resource or lists <code>resolvers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolvers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::AppSync::Resolver</code> resource defines the logical GraphQL resolver that you attach to fields in a schema. Request and response templates for resolvers are written in Apache Velocity Template Language (VTL) format. For more information about resolvers, see &#91;Resolver Mapping Template Reference&#93;(https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference.html).<br />When you submit an update, CFNLong updates resources based on differences between what you submit and the stack's current template. To cause this resource to be updated you must change a property value for this resource in the CFNshort template. Changing the S3 file content without changing a property value will not result in an update operation.<br />See &#91;Update Behaviors of Stack Resources&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html) in the *User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appsync.resolvers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="api_id" /></td><td><code>string</code></td><td>The APSYlong GraphQL API to which you want to attach this resolver.</td></tr>
<tr><td><CopyableCode code="caching_config" /></td><td><code>object</code></td><td>The caching configuration for the resolver.</td></tr>
<tr><td><CopyableCode code="code" /></td><td><code>string</code></td><td>The <code>resolver</code> code that contains the request and response functions. When code is used, the <code>runtime</code> is required. The runtime value must be <code>APPSYNC_JS</code>.</td></tr>
<tr><td><CopyableCode code="code_s3_location" /></td><td><code>string</code></td><td>The Amazon S3 endpoint.</td></tr>
<tr><td><CopyableCode code="data_source_name" /></td><td><code>string</code></td><td>The resolver data source name.</td></tr>
<tr><td><CopyableCode code="field_name" /></td><td><code>string</code></td><td>The GraphQL field on a type that invokes the resolver.</td></tr>
<tr><td><CopyableCode code="kind" /></td><td><code>string</code></td><td>The resolver type.<br />+ *UNIT*: A UNIT resolver type. A UNIT resolver is the default resolver type. You can use a UNIT resolver to run a GraphQL query against a single data source.<br />+ *PIPELINE*: A PIPELINE resolver type. You can use a PIPELINE resolver to invoke a series of <code>Function</code> objects in a serial manner. You can use a pipeline resolver to run a GraphQL query against multiple data sources.</td></tr>
<tr><td><CopyableCode code="max_batch_size" /></td><td><code>integer</code></td><td>The maximum number of resolver request inputs that will be sent to a single LAMlong function in a <code>BatchInvoke</code> operation.</td></tr>
<tr><td><CopyableCode code="pipeline_config" /></td><td><code>object</code></td><td>Functions linked with the pipeline resolver.</td></tr>
<tr><td><CopyableCode code="request_mapping_template" /></td><td><code>string</code></td><td>The request mapping template.<br />Request mapping templates are optional when using a Lambda data source. For all other data sources, a request mapping template is required.</td></tr>
<tr><td><CopyableCode code="request_mapping_template_s3_location" /></td><td><code>string</code></td><td>The location of a request mapping template in an S3 bucket. Use this if you want to provision with a template file in S3 rather than embedding it in your CFNshort template.</td></tr>
<tr><td><CopyableCode code="resolver_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="response_mapping_template" /></td><td><code>string</code></td><td>The response mapping template.</td></tr>
<tr><td><CopyableCode code="response_mapping_template_s3_location" /></td><td><code>string</code></td><td>The location of a response mapping template in an S3 bucket. Use this if you want to provision with a template file in S3 rather than embedding it in your CFNshort template.</td></tr>
<tr><td><CopyableCode code="runtime" /></td><td><code>object</code></td><td>Describes a runtime used by an APSYlong resolver or APSYlong function. Specifies the name and version of the runtime to use. Note that if a runtime is specified, code must also be specified.</td></tr>
<tr><td><CopyableCode code="sync_config" /></td><td><code>object</code></td><td>The <code>SyncConfig</code> for a resolver attached to a versioned data source.</td></tr>
<tr><td><CopyableCode code="type_name" /></td><td><code>string</code></td><td>The GraphQL type that invokes this resolver.</td></tr>
<tr><td><CopyableCode code="metrics_config" /></td><td><code>string</code></td><td>Enables or disables enhanced resolver metrics for specified resolvers. Note that <code>MetricsConfig</code> won't be used unless the <code>resolverLevelMetricsBehavior</code> value is set to <code>PER_RESOLVER_METRICS</code>. If the <code>resolverLevelMetricsBehavior</code> is set to <code>FULL_REQUEST_RESOLVER_METRICS</code> instead, <code>MetricsConfig</code> will be ignored. However, you can still set its value.</td></tr>
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
    <td><CopyableCode code="TypeName, ApiId, FieldName, region" /></td>
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
List all <code>resolvers</code> in a region.
```sql
SELECT
region,
resolver_arn
FROM aws.appsync.resolvers
WHERE region = 'us-east-1';
```
Gets all properties from a <code>resolver</code>.
```sql
SELECT
region,
api_id,
caching_config,
code,
code_s3_location,
data_source_name,
field_name,
kind,
max_batch_size,
pipeline_config,
request_mapping_template,
request_mapping_template_s3_location,
resolver_arn,
response_mapping_template,
response_mapping_template_s3_location,
runtime,
sync_config,
type_name,
metrics_config
FROM aws.appsync.resolvers
WHERE region = 'us-east-1' AND data__Identifier = '<ResolverArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>resolver</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.appsync.resolvers (
 ApiId,
 FieldName,
 TypeName,
 region
)
SELECT 
'{{ ApiId }}',
 '{{ FieldName }}',
 '{{ TypeName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.appsync.resolvers (
 ApiId,
 CachingConfig,
 Code,
 CodeS3Location,
 DataSourceName,
 FieldName,
 Kind,
 MaxBatchSize,
 PipelineConfig,
 RequestMappingTemplate,
 RequestMappingTemplateS3Location,
 ResponseMappingTemplate,
 ResponseMappingTemplateS3Location,
 Runtime,
 SyncConfig,
 TypeName,
 MetricsConfig,
 region
)
SELECT 
 '{{ ApiId }}',
 '{{ CachingConfig }}',
 '{{ Code }}',
 '{{ CodeS3Location }}',
 '{{ DataSourceName }}',
 '{{ FieldName }}',
 '{{ Kind }}',
 '{{ MaxBatchSize }}',
 '{{ PipelineConfig }}',
 '{{ RequestMappingTemplate }}',
 '{{ RequestMappingTemplateS3Location }}',
 '{{ ResponseMappingTemplate }}',
 '{{ ResponseMappingTemplateS3Location }}',
 '{{ Runtime }}',
 '{{ SyncConfig }}',
 '{{ TypeName }}',
 '{{ MetricsConfig }}',
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
  - name: resolver
    props:
      - name: ApiId
        value: '{{ ApiId }}'
      - name: CachingConfig
        value:
          CachingKeys:
            - '{{ CachingKeys[0] }}'
          Ttl: null
      - name: Code
        value: '{{ Code }}'
      - name: CodeS3Location
        value: '{{ CodeS3Location }}'
      - name: DataSourceName
        value: '{{ DataSourceName }}'
      - name: FieldName
        value: '{{ FieldName }}'
      - name: Kind
        value: '{{ Kind }}'
      - name: MaxBatchSize
        value: '{{ MaxBatchSize }}'
      - name: PipelineConfig
        value:
          Functions:
            - '{{ Functions[0] }}'
      - name: RequestMappingTemplate
        value: '{{ RequestMappingTemplate }}'
      - name: RequestMappingTemplateS3Location
        value: '{{ RequestMappingTemplateS3Location }}'
      - name: ResponseMappingTemplate
        value: '{{ ResponseMappingTemplate }}'
      - name: ResponseMappingTemplateS3Location
        value: '{{ ResponseMappingTemplateS3Location }}'
      - name: Runtime
        value:
          RuntimeVersion: '{{ RuntimeVersion }}'
          Name: '{{ Name }}'
      - name: SyncConfig
        value:
          ConflictHandler: '{{ ConflictHandler }}'
          ConflictDetection: '{{ ConflictDetection }}'
          LambdaConflictHandlerConfig:
            LambdaConflictHandlerArn: '{{ LambdaConflictHandlerArn }}'
      - name: TypeName
        value: '{{ TypeName }}'
      - name: MetricsConfig
        value: '{{ MetricsConfig }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.appsync.resolvers
WHERE data__Identifier = '<ResolverArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>resolvers</code> resource, the following permissions are required:

### Create
```json
s3:GetObject,
appsync:CreateResolver,
appsync:GetResolver
```

### Read
```json
appsync:GetResolver
```

### Update
```json
s3:GetObject,
appsync:UpdateResolver
```

### Delete
```json
appsync:DeleteResolver
```

### List
```json
appsync:ListResolvers
```

