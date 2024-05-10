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


Used to retrieve a list of <code>origin_request_policies</code> in a region or to create or delete a <code>origin_request_policies</code> resource, use <code>origin_request_policy</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>origin_request_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::CloudFront::OriginRequestPolicy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudfront.origin_request_policies" /></td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
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
FROM aws.cloudfront.origin_request_policies
;
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "OriginRequestPolicyConfig": {
  "Comment": "{{ Comment }}",
  "CookiesConfig": {
   "CookieBehavior": "{{ CookieBehavior }}",
   "Cookies": [
    "{{ Cookies[0] }}"
   ]
  },
  "HeadersConfig": {
   "HeaderBehavior": "{{ HeaderBehavior }}",
   "Headers": [
    "{{ Headers[0] }}"
   ]
  },
  "Name": "{{ Name }}",
  "QueryStringsConfig": {
   "QueryStringBehavior": "{{ QueryStringBehavior }}",
   "QueryStrings": [
    "{{ QueryStrings[0] }}"
   ]
  }
 }
}
>>>
--required properties only
INSERT INTO aws.cloudfront.origin_request_policies (
 OriginRequestPolicyConfig,
 region
)
SELECT 
{{ OriginRequestPolicyConfig }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "OriginRequestPolicyConfig": {
  "Comment": "{{ Comment }}",
  "CookiesConfig": {
   "CookieBehavior": "{{ CookieBehavior }}",
   "Cookies": [
    "{{ Cookies[0] }}"
   ]
  },
  "HeadersConfig": {
   "HeaderBehavior": "{{ HeaderBehavior }}",
   "Headers": [
    "{{ Headers[0] }}"
   ]
  },
  "Name": "{{ Name }}",
  "QueryStringsConfig": {
   "QueryStringBehavior": "{{ QueryStringBehavior }}",
   "QueryStrings": [
    "{{ QueryStrings[0] }}"
   ]
  }
 }
}
>>>
--all properties
INSERT INTO aws.cloudfront.origin_request_policies (
 OriginRequestPolicyConfig,
 region
)
SELECT 
 {{ OriginRequestPolicyConfig }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

