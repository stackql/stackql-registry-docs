---
title: cluster_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_policies
  - msk
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


Used to retrieve a list of <code>cluster_policies</code> in a region or to create or delete a <code>cluster_policies</code> resource, use <code>cluster_policy</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::MSK::ClusterPolicy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.msk.cluster_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="cluster_arn" /></td><td><code>string</code></td><td>The arn of the cluster for the resource policy.</td></tr>
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
cluster_arn
FROM aws.msk.cluster_policies
WHERE region = 'us-east-1';
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
 "Policy": {},
 "ClusterArn": "{{ ClusterArn }}"
}
>>>
--required properties only
INSERT INTO aws.msk.cluster_policies (
 Policy,
 ClusterArn,
 region
)
SELECT 
{{ Policy }},
 {{ ClusterArn }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Policy": {},
 "ClusterArn": "{{ ClusterArn }}"
}
>>>
--all properties
INSERT INTO aws.msk.cluster_policies (
 Policy,
 ClusterArn,
 region
)
SELECT 
 {{ Policy }},
 {{ ClusterArn }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.msk.cluster_policies
WHERE data__Identifier = '<ClusterArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>cluster_policies</code> resource, the following permissions are required:

### Create
```json
kafka:PutClusterPolicy,
kafka:GetClusterPolicy
```

### List
```json
kafka:GetClusterPolicy
```

### Delete
```json
kafka:DeleteClusterPolicy,
kafka:GetClusterPolicy
```

