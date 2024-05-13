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


Used to retrieve a list of <code>authorizers</code> in a region or to create or delete a <code>authorizers</code> resource, use <code>authorizer</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorizers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates an authorizer.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.authorizers" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="authorizer_name" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
authorizer_name
FROM aws.iot.authorizers
WHERE region = 'us-east-1';
```

## `INSERT` Example

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

## `DELETE` Example

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

