---
title: models
hide_title: false
hide_table_of_contents: false
keywords:
  - models
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

Creates, updates, deletes or gets a <code>model</code> resource or lists <code>models</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGateway::Model</code> resource defines the structure of a request or response payload for an API method.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.models" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="content_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name for the model. If you don't specify a name, CFN generates a unique physical ID and uses that ID for the model name. For more information, see &#91;Name Type&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html).<br />If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
<tr><td><CopyableCode code="rest_api_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="schema" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-model.html"><code>AWS::ApiGateway::Model</code></a>.

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
Gets all <code>models</code> in a region.
```sql
SELECT
region,
content_type,
description,
name,
rest_api_id,
schema
FROM aws.apigateway.models
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>model</code>.
```sql
SELECT
region,
content_type,
description,
name,
rest_api_id,
schema
FROM aws.apigateway.models
WHERE region = 'us-east-1' AND data__Identifier = '<RestApiId>|<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>model</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.apigateway.models (
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
INSERT INTO aws.apigateway.models (
 ContentType,
 Description,
 Name,
 RestApiId,
 Schema,
 region
)
SELECT 
 '{{ ContentType }}',
 '{{ Description }}',
 '{{ Name }}',
 '{{ RestApiId }}',
 '{{ Schema }}',
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
  - name: model
    props:
      - name: ContentType
        value: '{{ ContentType }}'
      - name: Description
        value: '{{ Description }}'
      - name: Name
        value: '{{ Name }}'
      - name: RestApiId
        value: '{{ RestApiId }}'
      - name: Schema
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.apigateway.models
WHERE data__Identifier = '<RestApiId|Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>models</code> resource, the following permissions are required:

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
apigateway:PATCH,
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
