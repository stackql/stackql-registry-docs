---
title: cache_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - cache_policies
  - cloudfront
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


Used to retrieve a list of <code>cache_policies</code> in a region or to create or delete a <code>cache_policies</code> resource, use <code>cache_policy</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cache_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::CloudFront::CachePolicy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudfront.cache_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="CachePolicyConfig, region" /></td>
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
id
FROM aws.cloudfront.cache_policies
;
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>cache_policy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cloudfront.cache_policies (
 CachePolicyConfig,
 region
)
SELECT 
'{{ CachePolicyConfig }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cloudfront.cache_policies (
 CachePolicyConfig,
 region
)
SELECT 
 '{{ CachePolicyConfig }}',
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
  - name: cache_policy
    props:
      - name: CachePolicyConfig
        value:
          Comment: '{{ Comment }}'
          DefaultTTL: null
          MaxTTL: null
          MinTTL: null
          Name: '{{ Name }}'
          ParametersInCacheKeyAndForwardedToOrigin:
            CookiesConfig:
              CookieBehavior: '{{ CookieBehavior }}'
              Cookies:
                - '{{ Cookies[0] }}'
            EnableAcceptEncodingBrotli: '{{ EnableAcceptEncodingBrotli }}'
            EnableAcceptEncodingGzip: '{{ EnableAcceptEncodingGzip }}'
            HeadersConfig:
              HeaderBehavior: '{{ HeaderBehavior }}'
              Headers:
                - '{{ Headers[0] }}'
            QueryStringsConfig:
              QueryStringBehavior: '{{ QueryStringBehavior }}'
              QueryStrings:
                - '{{ QueryStrings[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.cloudfront.cache_policies
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>cache_policies</code> resource, the following permissions are required:

### Create
```json
cloudfront:CreateCachePolicy
```

### Delete
```json
cloudfront:DeleteCachePolicy,
cloudfront:GetCachePolicy
```

### List
```json
cloudfront:ListCachePolicies
```

