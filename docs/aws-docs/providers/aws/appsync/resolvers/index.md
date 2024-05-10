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


Used to retrieve a list of <code>resolvers</code> in a region or to create or delete a <code>resolvers</code> resource, use <code>resolver</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolvers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::AppSync::Resolver`` resource defines the logical GraphQL resolver that you attach to fields in a schema. Request and response templates for resolvers are written in Apache Velocity Template Language (VTL) format. For more information about resolvers, see &#91;Resolver Mapping Template Reference&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;appsync&#x2F;latest&#x2F;devguide&#x2F;resolver-mapping-template-reference.html).&lt;br&#x2F;&gt;  When you submit an update, CFNLong updates resources based on differences between what you submit and the stack's current template. To cause this resource to be updated you must change a property value for this resource in the CFNshort template. Changing the S3 file content without changing a property value will not result in an update operation.&lt;br&#x2F;&gt; See &#91;Update Behaviors of Stack Resources&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;using-cfn-updating-stacks-update-behaviors.html) in the *User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appsync.resolvers" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="resolver_arn" /></td><td><code>string</code></td><td></td></tr>
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
resolver_arn
FROM aws.appsync.resolvers
WHERE region = 'us-east-1';
```

## `INSERT` Example

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
-- resolver.iql (required properties only)
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
-- resolver.iql (all properties)
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

## `DELETE` Example

```sql
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

### Delete
```json
appsync:DeleteResolver
```

### List
```json
appsync:ListResolvers
```

