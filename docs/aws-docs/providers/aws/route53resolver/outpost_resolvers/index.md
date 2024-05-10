---
title: outpost_resolvers
hide_title: false
hide_table_of_contents: false
keywords:
  - outpost_resolvers
  - route53resolver
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


Used to retrieve a list of <code>outpost_resolvers</code> in a region or to create or delete a <code>outpost_resolvers</code> resource, use <code>outpost_resolver</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>outpost_resolvers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Route53Resolver::OutpostResolver.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53resolver.outpost_resolvers" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Id</td></tr>
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
FROM aws.route53resolver.outpost_resolvers
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>outpost_resolver</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- outpost_resolver.iql (required properties only)
INSERT INTO aws.route53resolver.outpost_resolvers (
 Name,
 OutpostArn,
 PreferredInstanceType,
 region
)
SELECT 
'{{ Name }}',
 '{{ OutpostArn }}',
 '{{ PreferredInstanceType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- outpost_resolver.iql (all properties)
INSERT INTO aws.route53resolver.outpost_resolvers (
 Name,
 OutpostArn,
 PreferredInstanceType,
 InstanceCount,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ OutpostArn }}',
 '{{ PreferredInstanceType }}',
 '{{ InstanceCount }}',
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
  - name: outpost_resolver
    props:
      - name: Name
        value: '{{ Name }}'
      - name: OutpostArn
        value: '{{ OutpostArn }}'
      - name: PreferredInstanceType
        value: '{{ PreferredInstanceType }}'
      - name: InstanceCount
        value: '{{ InstanceCount }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.route53resolver.outpost_resolvers
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>outpost_resolvers</code> resource, the following permissions are required:

### Create
```json
route53resolver:CreateOutpostResolver,
route53resolver:GetOutpostResolver,
route53resolver:ListTagsForResource,
outposts:GetOutpost
```

### Delete
```json
route53resolver:DeleteOutpostResolver,
route53resolver:GetOutpostResolver,
route53resolver:ListOutpostResolvers,
route53resolver:ListResolverEndpoints
```

### List
```json
route53resolver:ListOutpostResolvers,
route53resolver:ListTagsForResource
```

