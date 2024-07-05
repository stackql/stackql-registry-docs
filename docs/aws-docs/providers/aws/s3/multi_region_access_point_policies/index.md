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

Creates, updates, deletes or gets a <code>multi_region_access_point_policy</code> resource or lists <code>multi_region_access_point_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>multi_region_access_point_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The policy to be attached to a Multi Region Access Point</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3.multi_region_access_point_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="mrap_name" /></td><td><code>string</code></td><td>The name of the Multi Region Access Point to apply policy</td></tr>
<tr><td><CopyableCode code="policy" /></td><td><code>object</code></td><td>Policy document to apply to a Multi Region Access Point</td></tr>
<tr><td><CopyableCode code="policy_status" /></td><td><code>object</code></td><td>The Policy Status associated with this Multi Region Access Point</td></tr>
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
    <td><CopyableCode code="Policy, MrapName, region" /></td>
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
Gets all <code>multi_region_access_point_policies</code> in a region.
```sql
SELECT
region,
mrap_name,
policy,
policy_status
FROM aws.s3.multi_region_access_point_policies
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>multi_region_access_point_policy</code>.
```sql
SELECT
region,
mrap_name,
policy,
policy_status
FROM aws.s3.multi_region_access_point_policies
WHERE region = 'us-east-1' AND data__Identifier = '<MrapName>';
```

## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.s3.multi_region_access_point_policies
WHERE data__Identifier = '<MrapName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>multi_region_access_point_policies</code> resource, the following permissions are required:

### Update
```json
s3:PutMultiRegionAccessPointPolicy,
s3:DescribeMultiRegionAccessPointOperation
```

### Read
```json
s3:GetMultiRegionAccessPointPolicy,
s3:GetMultiRegionAccessPointPolicyStatus
```

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

