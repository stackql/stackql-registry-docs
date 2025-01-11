---
title: base_path_mapping_v2s
hide_title: false
hide_table_of_contents: false
keywords:
  - base_path_mapping_v2s
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

Creates, updates, deletes or gets a <code>base_path_mapping_v2</code> resource or lists <code>base_path_mapping_v2s</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>base_path_mapping_v2s</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ApiGateway::BasePathMappingV2</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.base_path_mapping_v2s" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="base_path" /></td><td><code>string</code></td><td>The base path name that callers of the API must provide in the URL after the domain name.</td></tr>
<tr><td><CopyableCode code="domain_name_arn" /></td><td><code>string</code></td><td>The Arn of an AWS::ApiGateway::DomainNameV2 resource.</td></tr>
<tr><td><CopyableCode code="rest_api_id" /></td><td><code>string</code></td><td>The ID of the API.</td></tr>
<tr><td><CopyableCode code="stage" /></td><td><code>string</code></td><td>The name of the API's stage.</td></tr>
<tr><td><CopyableCode code="base_path_mapping_arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-basepathmappingv2.html"><code>AWS::ApiGateway::BasePathMappingV2</code></a>.

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
    <td><CopyableCode code="DomainNameArn, RestApiId, region" /></td>
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
Gets all <code>base_path_mapping_v2s</code> in a region.
```sql
SELECT
region,
base_path,
domain_name_arn,
rest_api_id,
stage,
base_path_mapping_arn
FROM aws.apigateway.base_path_mapping_v2s
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>base_path_mapping_v2</code>.
```sql
SELECT
region,
base_path,
domain_name_arn,
rest_api_id,
stage,
base_path_mapping_arn
FROM aws.apigateway.base_path_mapping_v2s
WHERE region = 'us-east-1' AND data__Identifier = '<BasePathMappingArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>base_path_mapping_v2</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.apigateway.base_path_mapping_v2s (
 DomainNameArn,
 RestApiId,
 region
)
SELECT 
'{{ DomainNameArn }}',
 '{{ RestApiId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.apigateway.base_path_mapping_v2s (
 BasePath,
 DomainNameArn,
 RestApiId,
 Stage,
 region
)
SELECT 
 '{{ BasePath }}',
 '{{ DomainNameArn }}',
 '{{ RestApiId }}',
 '{{ Stage }}',
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
  - name: base_path_mapping_v2
    props:
      - name: BasePath
        value: '{{ BasePath }}'
      - name: DomainNameArn
        value: '{{ DomainNameArn }}'
      - name: RestApiId
        value: '{{ RestApiId }}'
      - name: Stage
        value: '{{ Stage }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.apigateway.base_path_mapping_v2s
WHERE data__Identifier = '<BasePathMappingArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>base_path_mapping_v2s</code> resource, the following permissions are required:

### Create
```json
apigateway:POST,
apigateway:GET
```

### Read
```json
apigateway:GET
```

### Update
```json
apigateway:GET,
apigateway:DELETE,
apigateway:PATCH
```

### Delete
```json
apigateway:DELETE
```

### List
```json
apigateway:GET
```
