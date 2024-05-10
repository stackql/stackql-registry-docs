---
title: cidr_collections
hide_title: false
hide_table_of_contents: false
keywords:
  - cidr_collections
  - route53
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


Used to retrieve a list of <code>cidr_collections</code> in a region or to create or delete a <code>cidr_collections</code> resource, use <code>cidr_collection</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cidr_collections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Route53::CidrCollection.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53.cidr_collections" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>UUID of the CIDR collection.</td></tr>
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
FROM aws.route53.cidr_collections
;
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>cidr_collection</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- cidr_collection.iql (required properties only)
INSERT INTO aws.route53.cidr_collections (
 Name,
 region
)
SELECT 
'{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- cidr_collection.iql (all properties)
INSERT INTO aws.route53.cidr_collections (
 Name,
 Locations,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Locations }}',
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
  - name: cidr_collection
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Locations
        value:
          - LocationName: '{{ LocationName }}'
            CidrList:
              - '{{ CidrList[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.route53.cidr_collections
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>cidr_collections</code> resource, the following permissions are required:

### Create
```json
route53:CreateCidrCollection,
route53:ChangeCidrCollection
```

### Delete
```json
route53:DeleteCidrCollection,
route53:ChangeCidrCollection
```

### List
```json
route53:ListCidrCollections,
route53:ListCidrBlocks
```

