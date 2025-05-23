---
title: base_path_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - base_path_mappings
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

Creates, updates, deletes or gets a <code>base_path_mapping</code> resource or lists <code>base_path_mappings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>base_path_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGateway::BasePathMapping</code> resource creates a base path that clients who call your API must use in the invocation URL.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.base_path_mappings" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="base_path" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rest_api_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stage" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-basepathmapping.html"><code>AWS::ApiGateway::BasePathMapping</code></a>.

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
    <td><CopyableCode code="DomainName, region" /></td>
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
Gets all <code>base_path_mappings</code> in a region.
```sql
SELECT
region,
base_path,
domain_name,
rest_api_id,
stage
FROM aws.apigateway.base_path_mappings
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>base_path_mapping</code>.
```sql
SELECT
region,
base_path,
domain_name,
rest_api_id,
stage
FROM aws.apigateway.base_path_mappings
WHERE region = 'us-east-1' AND data__Identifier = '<DomainName>|<BasePath>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>base_path_mapping</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.apigateway.base_path_mappings (
 DomainName,
 region
)
SELECT 
'{{ DomainName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.apigateway.base_path_mappings (
 BasePath,
 DomainName,
 RestApiId,
 Stage,
 region
)
SELECT 
 '{{ BasePath }}',
 '{{ DomainName }}',
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
  - name: base_path_mapping
    props:
      - name: BasePath
        value: '{{ BasePath }}'
      - name: DomainName
        value: '{{ DomainName }}'
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
DELETE FROM aws.apigateway.base_path_mappings
WHERE data__Identifier = '<DomainName|BasePath>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>base_path_mappings</code> resource, the following permissions are required:

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
