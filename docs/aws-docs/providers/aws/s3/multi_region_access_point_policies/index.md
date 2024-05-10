---
title: multi_region_access_point_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - multi_region_access_point_policies
  - s3
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


Used to retrieve a list of <code>multi_region_access_point_policies</code> in a region or to create or delete a <code>multi_region_access_point_policies</code> resource, use <code>multi_region_access_point_policy</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>multi_region_access_point_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The policy to be attached to a Multi Region Access Point</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3.multi_region_access_point_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="mrap_name" /></td><td><code>string</code></td><td>The name of the Multi Region Access Point to apply policy</td></tr>
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
mrap_name
FROM aws.s3.multi_region_access_point_policies
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>multi_region_access_point_policy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- multi_region_access_point_policy.iql (required properties only)
INSERT INTO aws.s3.multi_region_access_point_policies (
 MrapName,
 Policy,
 region
)
SELECT 
'{{ MrapName }}',
 '{{ Policy }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- multi_region_access_point_policy.iql (all properties)
INSERT INTO aws.s3.multi_region_access_point_policies (
 MrapName,
 Policy,
 region
)
SELECT 
 '{{ MrapName }}',
 '{{ Policy }}',
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
  - name: multi_region_access_point_policy
    props:
      - name: MrapName
        value: '{{ MrapName }}'
      - name: Policy
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.s3.multi_region_access_point_policies
WHERE data__Identifier = '<MrapName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>multi_region_access_point_policies</code> resource, the following permissions are required:

### Delete
```json
s3:GetMultiRegionAccessPointPolicy,
s3:GetMultiRegionAccessPoint
```

### Create
```json
s3:PutMultiRegionAccessPointPolicy,
s3:DescribeMultiRegionAccessPointOperation
```

