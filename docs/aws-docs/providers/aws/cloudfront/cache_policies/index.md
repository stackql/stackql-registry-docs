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

Creates, updates, deletes or gets a <code>cache_policy</code> resource or lists <code>cache_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cache_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A cache policy.<br />When it's attached to a cache behavior, the cache policy determines the following:<br />+ The values that CloudFront includes in the cache key. These values can include HTTP headers, cookies, and URL query strings. CloudFront uses the cache key to find an object in its cache that it can return to the viewer.<br />+ The default, minimum, and maximum time to live (TTL) values that you want objects to stay in the CloudFront cache.<br /><br />The headers, cookies, and query strings that are included in the cache key are also included in requests that CloudFront sends to the origin. CloudFront sends a request when it can't find a valid object in its cache that matches the request's cache key. If you want to send values to the origin but *not* include them in the cache key, use <code>OriginRequestPolicy</code>.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudfront.cache_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="cache_policy_config" /></td><td><code>object</code></td><td>The cache policy configuration.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cachepolicy.html"><code>AWS::CloudFront::CachePolicy</code></a>.

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
Gets all <code>cache_policies</code> in a region.
```sql
SELECT
region,
cache_policy_config,
id,
last_modified_time
FROM aws.cloudfront.cache_policies
;
```
Gets all properties from an individual <code>cache_policy</code>.
```sql
SELECT
region,
cache_policy_config,
id,
last_modified_time
FROM aws.cloudfront.cache_policies
WHERE data__Identifier = '<Id>';
```

## `INSERT` example

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

## `DELETE` example

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

### Read
```json
cloudfront:GetCachePolicy
```

### Update
```json
cloudfront:UpdateCachePolicy,
cloudfront:GetCachePolicy
```
