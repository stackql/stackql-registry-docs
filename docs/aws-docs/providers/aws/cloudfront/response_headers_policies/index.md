---
title: response_headers_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - response_headers_policies
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


Used to retrieve a list of <code>response_headers_policies</code> in a region or to create or delete a <code>response_headers_policies</code> resource, use <code>response_headers_policy</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>response_headers_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::CloudFront::ResponseHeadersPolicy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudfront.response_headers_policies" /></td></tr>
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
FROM aws.cloudfront.response_headers_policies
;
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>response_headers_policy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- response_headers_policy.iql (required properties only)
INSERT INTO aws.cloudfront.response_headers_policies (
 ResponseHeadersPolicyConfig,
 region
)
SELECT 
'{{ ResponseHeadersPolicyConfig }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- response_headers_policy.iql (all properties)
INSERT INTO aws.cloudfront.response_headers_policies (
 ResponseHeadersPolicyConfig,
 region
)
SELECT 
 '{{ ResponseHeadersPolicyConfig }}',
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
  - name: response_headers_policy
    props:
      - name: ResponseHeadersPolicyConfig
        value:
          Comment: '{{ Comment }}'
          CorsConfig:
            AccessControlAllowCredentials: '{{ AccessControlAllowCredentials }}'
            AccessControlAllowHeaders:
              Items:
                - '{{ Items[0] }}'
            AccessControlAllowMethods:
              Items:
                - '{{ Items[0] }}'
            AccessControlAllowOrigins:
              Items:
                - '{{ Items[0] }}'
            AccessControlExposeHeaders:
              Items:
                - '{{ Items[0] }}'
            AccessControlMaxAgeSec: '{{ AccessControlMaxAgeSec }}'
            OriginOverride: '{{ OriginOverride }}'
          CustomHeadersConfig:
            Items:
              - Header: '{{ Header }}'
                Override: '{{ Override }}'
                Value: '{{ Value }}'
          Name: '{{ Name }}'
          RemoveHeadersConfig:
            Items:
              - Header: '{{ Header }}'
          SecurityHeadersConfig:
            ContentSecurityPolicy:
              ContentSecurityPolicy: '{{ ContentSecurityPolicy }}'
              Override: '{{ Override }}'
            ContentTypeOptions:
              Override: '{{ Override }}'
            FrameOptions:
              FrameOption: '{{ FrameOption }}'
              Override: '{{ Override }}'
            ReferrerPolicy:
              Override: '{{ Override }}'
              ReferrerPolicy: '{{ ReferrerPolicy }}'
            StrictTransportSecurity:
              AccessControlMaxAgeSec: '{{ AccessControlMaxAgeSec }}'
              IncludeSubdomains: '{{ IncludeSubdomains }}'
              Override: '{{ Override }}'
              Preload: '{{ Preload }}'
            XSSProtection:
              ModeBlock: '{{ ModeBlock }}'
              Override: '{{ Override }}'
              Protection: '{{ Protection }}'
              ReportUri: '{{ ReportUri }}'
          ServerTimingHeadersConfig:
            Enabled: '{{ Enabled }}'
            SamplingRate: null

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.cloudfront.response_headers_policies
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>response_headers_policies</code> resource, the following permissions are required:

### Create
```json
cloudfront:CreateResponseHeadersPolicy
```

### Delete
```json
cloudfront:DeleteResponseHeadersPolicy,
cloudfront:GetResponseHeadersPolicy
```

### List
```json
cloudfront:ListResponseHeadersPolicies
```

