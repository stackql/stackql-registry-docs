---
title: origin_request_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - origin_request_policies
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

Creates, updates, deletes or gets an <code>origin_request_policy</code> resource or lists <code>origin_request_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>origin_request_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An origin request policy.<br />When it's attached to a cache behavior, the origin request policy determines the values that CloudFront includes in requests that it sends to the origin. Each request that CloudFront sends to the origin includes the following:<br />+ The request body and the URL path (without the domain name) from the viewer request.<br />+ The headers that CloudFront automatically includes in every origin request, including <code>Host</code>, <code>User-Agent</code>, and <code>X-Amz-Cf-Id</code>.<br />+ All HTTP headers, cookies, and URL query strings that are specified in the cache policy or the origin request policy. These can include items from the viewer request and, in the case of headers, additional ones that are added by CloudFront.<br /><br />CloudFront sends a request when it can't find an object in its cache that matches the request. If you want to send values to the origin and also include them in the cache key, use <code>CachePolicy</code>.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudfront.origin_request_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="origin_request_policy_config" /></td><td><code>object</code></td><td>The origin request policy configuration.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-originrequestpolicy.html"><code>AWS::CloudFront::OriginRequestPolicy</code></a>.

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
    <td><CopyableCode code="OriginRequestPolicyConfig, region" /></td>
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
Gets all <code>origin_request_policies</code> in a region.
```sql
SELECT
region,
id,
last_modified_time,
origin_request_policy_config
FROM aws.cloudfront.origin_request_policies
;
```
Gets all properties from an individual <code>origin_request_policy</code>.
```sql
SELECT
region,
id,
last_modified_time,
origin_request_policy_config
FROM aws.cloudfront.origin_request_policies
WHERE data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>origin_request_policy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cloudfront.origin_request_policies (
 OriginRequestPolicyConfig,
 region
)
SELECT 
'{{ OriginRequestPolicyConfig }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cloudfront.origin_request_policies (
 OriginRequestPolicyConfig,
 region
)
SELECT 
 '{{ OriginRequestPolicyConfig }}',
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
  - name: origin_request_policy
    props:
      - name: OriginRequestPolicyConfig
        value:
          Comment: '{{ Comment }}'
          CookiesConfig:
            CookieBehavior: '{{ CookieBehavior }}'
            Cookies:
              - '{{ Cookies[0] }}'
          HeadersConfig:
            HeaderBehavior: '{{ HeaderBehavior }}'
            Headers:
              - '{{ Headers[0] }}'
          Name: '{{ Name }}'
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
DELETE FROM aws.cloudfront.origin_request_policies
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>origin_request_policies</code> resource, the following permissions are required:

### Create
```json
cloudfront:CreateOriginRequestPolicy
```

### Delete
```json
cloudfront:DeleteOriginRequestPolicy,
cloudfront:GetOriginRequestPolicy
```

### List
```json
cloudfront:ListOriginRequestPolicies
```

### Read
```json
cloudfront:GetOriginRequestPolicy
```

### Update
```json
cloudfront:UpdateOriginRequestPolicy,
cloudfront:GetOriginRequestPolicy
```
