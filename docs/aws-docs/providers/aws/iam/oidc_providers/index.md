---
title: oidc_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - oidc_providers
  - iam
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


Used to retrieve a list of <code>oidc_providers</code> in a region or to create or delete a <code>oidc_providers</code> resource, use <code>oidc_provider</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>oidc_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IAM::OIDCProvider</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam.oidc_providers" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the OIDC provider</td></tr>
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
arn
FROM aws.iam.oidc_providers
;
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>oidc_provider</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- oidc_provider.iql (required properties only)
INSERT INTO aws.iam.oidc_providers (
 ThumbprintList,
 region
)
SELECT 
'{{ ThumbprintList }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- oidc_provider.iql (all properties)
INSERT INTO aws.iam.oidc_providers (
 ClientIdList,
 Url,
 ThumbprintList,
 Tags,
 region
)
SELECT 
 '{{ ClientIdList }}',
 '{{ Url }}',
 '{{ ThumbprintList }}',
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
  - name: oidc_provider
    props:
      - name: ClientIdList
        value:
          - '{{ ClientIdList[0] }}'
      - name: Url
        value: '{{ Url }}'
      - name: ThumbprintList
        value:
          - '{{ ThumbprintList[0] }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iam.oidc_providers
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>oidc_providers</code> resource, the following permissions are required:

### Create
```json
iam:CreateOpenIDConnectProvider,
iam:TagOpenIDConnectProvider,
iam:GetOpenIDConnectProvider
```

### Delete
```json
iam:DeleteOpenIDConnectProvider
```

### List
```json
iam:ListOpenIDConnectProvider,
iam:GetOpenIDConnectProvider
```

