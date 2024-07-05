---
title: api_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - api_keys
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

Creates, updates, deletes or gets an <code>api_key</code> resource or lists <code>api_keys</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGateway::ApiKey</code> resource creates a unique key that you can distribute to clients who are executing API Gateway <code>Method</code> resources that require an API key. To specify which API key clients must use, map the API key with the <code>RestApi</code> and <code>Stage</code> resources that include the methods that require a key.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.api_keys" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="api_key_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="customer_id" /></td><td><code>string</code></td><td>An MKT customer identifier, when integrating with the AWS SaaS Marketplace.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the ApiKey.</td></tr>
<tr><td><CopyableCode code="enabled" /></td><td><code>boolean</code></td><td>Specifies whether the ApiKey can be used by callers.</td></tr>
<tr><td><CopyableCode code="generate_distinct_id" /></td><td><code>boolean</code></td><td>Specifies whether (<code>true</code>) or not (<code>false</code>) the key identifier is distinct from the created API key value. This parameter is deprecated and should not be used.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name for the API key. If you don't specify a name, CFN generates a unique physical ID and uses that ID for the API key name. For more information, see &#91;Name Type&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html).<br />If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
<tr><td><CopyableCode code="stage_keys" /></td><td><code>array</code></td><td>DEPRECATED FOR USAGE PLANS - Specifies stages associated with the API key.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The key-value map of strings. The valid character set is &#91;a-zA-Z+-=._:/&#93;. The tag key can be up to 128 characters and must not start with <code>aws:</code>. The tag value can be up to 256 characters.</td></tr>
<tr><td><CopyableCode code="value" /></td><td><code>string</code></td><td>Specifies a value of the API key.</td></tr>
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
    <td><CopyableCode code="region" /></td>
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
Gets all <code>api_keys</code> in a region.
```sql
SELECT
region,
api_key_id,
customer_id,
description,
enabled,
generate_distinct_id,
name,
stage_keys,
tags,
value
FROM aws.apigateway.api_keys
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>api_key</code>.
```sql
SELECT
region,
api_key_id,
customer_id,
description,
enabled,
generate_distinct_id,
name,
stage_keys,
tags,
value
FROM aws.apigateway.api_keys
WHERE region = 'us-east-1' AND data__Identifier = '<APIKeyId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>api_key</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.apigateway.api_keys (
 CustomerId,
 Description,
 Enabled,
 GenerateDistinctId,
 Name,
 StageKeys,
 Tags,
 Value,
 region
)
SELECT 
'{{ CustomerId }}',
 '{{ Description }}',
 '{{ Enabled }}',
 '{{ GenerateDistinctId }}',
 '{{ Name }}',
 '{{ StageKeys }}',
 '{{ Tags }}',
 '{{ Value }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.apigateway.api_keys (
 CustomerId,
 Description,
 Enabled,
 GenerateDistinctId,
 Name,
 StageKeys,
 Tags,
 Value,
 region
)
SELECT 
 '{{ CustomerId }}',
 '{{ Description }}',
 '{{ Enabled }}',
 '{{ GenerateDistinctId }}',
 '{{ Name }}',
 '{{ StageKeys }}',
 '{{ Tags }}',
 '{{ Value }}',
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
  - name: api_key
    props:
      - name: CustomerId
        value: '{{ CustomerId }}'
      - name: Description
        value: '{{ Description }}'
      - name: Enabled
        value: '{{ Enabled }}'
      - name: GenerateDistinctId
        value: '{{ GenerateDistinctId }}'
      - name: Name
        value: '{{ Name }}'
      - name: StageKeys
        value:
          - RestApiId: '{{ RestApiId }}'
            StageName: '{{ StageName }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: Value
        value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.apigateway.api_keys
WHERE data__Identifier = '<APIKeyId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>api_keys</code> resource, the following permissions are required:

### Create
```json
apigateway:POST,
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
apigateway:DELETE,
apigateway:GET
```

### List
```json
apigateway:GET
```

