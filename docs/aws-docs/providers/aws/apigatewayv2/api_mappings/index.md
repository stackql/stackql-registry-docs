---
title: api_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - api_mappings
  - apigatewayv2
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

Creates, updates, deletes or gets an <code>api_mapping</code> resource or lists <code>api_mappings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGatewayV2::ApiMapping</code> resource contains an API mapping. An API mapping relates a path of your custom domain name to a stage of your API. A custom domain name can have multiple API mappings, but the paths can't overlap. A custom domain can map only to APIs of the same protocol type. For more information, see &#91;CreateApiMapping&#93;(https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/domainnames-domainname-apimappings.html#CreateApiMapping) in the *Amazon API Gateway V2 API Reference*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigatewayv2.api_mappings" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="api_mapping_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The domain name.</td></tr>
<tr><td><CopyableCode code="stage" /></td><td><code>string</code></td><td>The API stage.</td></tr>
<tr><td><CopyableCode code="api_mapping_key" /></td><td><code>string</code></td><td>The API mapping key.</td></tr>
<tr><td><CopyableCode code="api_id" /></td><td><code>string</code></td><td>The identifier of the API.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html"><code>AWS::ApiGatewayV2::ApiMapping</code></a>.

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
    <td><CopyableCode code="DomainName, Stage, ApiId, region" /></td>
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
Gets all <code>api_mappings</code> in a region.
```sql
SELECT
region,
api_mapping_id,
domain_name,
stage,
api_mapping_key,
api_id
FROM aws.apigatewayv2.api_mappings
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>api_mapping</code>.
```sql
SELECT
region,
api_mapping_id,
domain_name,
stage,
api_mapping_key,
api_id
FROM aws.apigatewayv2.api_mappings
WHERE region = 'us-east-1' AND data__Identifier = '<ApiMappingId>|<DomainName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>api_mapping</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.apigatewayv2.api_mappings (
 DomainName,
 Stage,
 ApiId,
 region
)
SELECT 
'{{ DomainName }}',
 '{{ Stage }}',
 '{{ ApiId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.apigatewayv2.api_mappings (
 DomainName,
 Stage,
 ApiMappingKey,
 ApiId,
 region
)
SELECT 
 '{{ DomainName }}',
 '{{ Stage }}',
 '{{ ApiMappingKey }}',
 '{{ ApiId }}',
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
  - name: api_mapping
    props:
      - name: DomainName
        value: '{{ DomainName }}'
      - name: Stage
        value: '{{ Stage }}'
      - name: ApiMappingKey
        value: '{{ ApiMappingKey }}'
      - name: ApiId
        value: '{{ ApiId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.apigatewayv2.api_mappings
WHERE data__Identifier = '<ApiMappingId|DomainName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>api_mappings</code> resource, the following permissions are required:

### Create
```json
apigateway:POST
```

### Update
```json
apigateway:PATCH,
apigateway:GET,
apigateway:PUT
```

### Read
```json
apigateway:GET
```

### Delete
```json
apigateway:DELETE
```

### List
```json
apigateway:GET
```
