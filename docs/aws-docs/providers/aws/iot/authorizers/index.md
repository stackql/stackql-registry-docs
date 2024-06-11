---
title: authorizers
hide_title: false
hide_table_of_contents: false
keywords:
  - authorizers
  - iot
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

Creates, updates, deletes or gets an <code>authorizer</code> resource or lists <code>authorizers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorizers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates an authorizer.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.authorizers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="authorizer_function_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="authorizer_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="signing_disabled" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="token_key_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="token_signing_public_keys" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="enable_caching_for_http" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="AuthorizerFunctionArn, region" /></td>
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
List all <code>authorizers</code> in a region.
```sql
SELECT
region,
authorizer_name
FROM aws.iot.authorizers
WHERE region = 'us-east-1';
```
Gets all properties from an <code>authorizer</code>.
```sql
SELECT
region,
authorizer_function_arn,
arn,
authorizer_name,
signing_disabled,
status,
token_key_name,
token_signing_public_keys,
enable_caching_for_http,
tags
FROM aws.iot.authorizers
WHERE region = 'us-east-1' AND data__Identifier = '<AuthorizerName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>authorizer</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iot.authorizers (
 AuthorizerFunctionArn,
 region
)
SELECT 
'{{ AuthorizerFunctionArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iot.authorizers (
 AuthorizerFunctionArn,
 AuthorizerName,
 SigningDisabled,
 Status,
 TokenKeyName,
 TokenSigningPublicKeys,
 EnableCachingForHttp,
 Tags,
 region
)
SELECT 
 '{{ AuthorizerFunctionArn }}',
 '{{ AuthorizerName }}',
 '{{ SigningDisabled }}',
 '{{ Status }}',
 '{{ TokenKeyName }}',
 '{{ TokenSigningPublicKeys }}',
 '{{ EnableCachingForHttp }}',
 '{{ Tags }}',
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
  - name: authorizer
    props:
      - name: AuthorizerFunctionArn
        value: '{{ AuthorizerFunctionArn }}'
      - name: AuthorizerName
        value: '{{ AuthorizerName }}'
      - name: SigningDisabled
        value: '{{ SigningDisabled }}'
      - name: Status
        value: '{{ Status }}'
      - name: TokenKeyName
        value: '{{ TokenKeyName }}'
      - name: TokenSigningPublicKeys
        value: {}
      - name: EnableCachingForHttp
        value: '{{ EnableCachingForHttp }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iot.authorizers
WHERE data__Identifier = '<AuthorizerName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>authorizers</code> resource, the following permissions are required:

### Create
```json
iot:CreateAuthorizer,
iot:DescribeAuthorizer,
iot:TagResource,
iot:ListTagsForResource
```

### Read
```json
iot:DescribeAuthorizer,
iot:ListTagsForResource
```

### Update
```json
iot:UpdateAuthorizer,
iot:DescribeAuthorizer,
iot:TagResource,
iot:UntagResource,
iot:ListTagsForResource
```

### Delete
```json
iot:UpdateAuthorizer,
iot:DeleteAuthorizer,
iot:DescribeAuthorizer
```

### List
```json
iot:ListAuthorizers
```

