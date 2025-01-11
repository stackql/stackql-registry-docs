---
title: license_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - license_endpoints
  - deadline
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

Creates, updates, deletes or gets a <code>license_endpoint</code> resource or lists <code>license_endpoints</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>license_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Deadline::LicenseEndpoint Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.deadline.license_endpoints" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="dns_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="license_endpoint_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="security_group_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status_message" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="subnet_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-licenseendpoint.html"><code>AWS::Deadline::LicenseEndpoint</code></a>.

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
    <td><CopyableCode code="SecurityGroupIds, SubnetIds, VpcId, region" /></td>
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
Gets all <code>license_endpoints</code> in a region.
```sql
SELECT
region,
dns_name,
license_endpoint_id,
security_group_ids,
status,
status_message,
subnet_ids,
vpc_id,
arn,
tags
FROM aws.deadline.license_endpoints
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>license_endpoint</code>.
```sql
SELECT
region,
dns_name,
license_endpoint_id,
security_group_ids,
status,
status_message,
subnet_ids,
vpc_id,
arn,
tags
FROM aws.deadline.license_endpoints
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>license_endpoint</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.deadline.license_endpoints (
 SecurityGroupIds,
 SubnetIds,
 VpcId,
 region
)
SELECT 
'{{ SecurityGroupIds }}',
 '{{ SubnetIds }}',
 '{{ VpcId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.deadline.license_endpoints (
 SecurityGroupIds,
 SubnetIds,
 VpcId,
 Tags,
 region
)
SELECT 
 '{{ SecurityGroupIds }}',
 '{{ SubnetIds }}',
 '{{ VpcId }}',
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
  - name: license_endpoint
    props:
      - name: SecurityGroupIds
        value:
          - '{{ SecurityGroupIds[0] }}'
      - name: SubnetIds
        value:
          - '{{ SubnetIds[0] }}'
      - name: VpcId
        value: '{{ VpcId }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.deadline.license_endpoints
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>license_endpoints</code> resource, the following permissions are required:

### Create
```json
deadline:CreateLicenseEndpoint,
deadline:GetLicenseEndpoint,
ec2:CreateTags,
ec2:CreateVpcEndpoint,
ec2:DescribeVpcEndpoints,
deadline:TagResource,
deadline:ListTagsForResource
```

### Read
```json
deadline:GetLicenseEndpoint,
deadline:ListTagsForResource
```

### Update
```json
deadline:TagResource,
deadline:UntagResource,
deadline:ListTagsForResource,
deadline:GetLicenseEndpoint
```

### Delete
```json
deadline:GetLicenseEndpoint,
deadline:DeleteLicenseEndpoint,
ec2:DeleteVpcEndpoints,
ec2:DescribeVpcEndpoints
```

### List
```json
deadline:ListLicenseEndpoints
```
