---
title: ipam_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - ipam_pools
  - ec2
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


Used to retrieve a list of <code>ipam_pools</code> in a region or to create or delete a <code>ipam_pools</code> resource, use <code>ipam_pool</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ipam_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema of AWS::EC2::IPAMPool Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.ipam_pools" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="ipam_pool_id" /></td><td><code>string</code></td><td>Id of the IPAM Pool.</td></tr>
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
    <td><CopyableCode code="IpamScopeId, AddressFamily, region" /></td>
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
ipam_pool_id
FROM aws.ec2.ipam_pools
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>ipam_pool</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.ipam_pools (
 AddressFamily,
 IpamScopeId,
 region
)
SELECT 
'{{ AddressFamily }}',
 '{{ IpamScopeId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.ipam_pools (
 AddressFamily,
 AllocationMinNetmaskLength,
 AllocationDefaultNetmaskLength,
 AllocationMaxNetmaskLength,
 AllocationResourceTags,
 AutoImport,
 AwsService,
 Description,
 IpamScopeId,
 Locale,
 ProvisionedCidrs,
 PublicIpSource,
 PubliclyAdvertisable,
 SourceIpamPoolId,
 SourceResource,
 Tags,
 region
)
SELECT 
 '{{ AddressFamily }}',
 '{{ AllocationMinNetmaskLength }}',
 '{{ AllocationDefaultNetmaskLength }}',
 '{{ AllocationMaxNetmaskLength }}',
 '{{ AllocationResourceTags }}',
 '{{ AutoImport }}',
 '{{ AwsService }}',
 '{{ Description }}',
 '{{ IpamScopeId }}',
 '{{ Locale }}',
 '{{ ProvisionedCidrs }}',
 '{{ PublicIpSource }}',
 '{{ PubliclyAdvertisable }}',
 '{{ SourceIpamPoolId }}',
 '{{ SourceResource }}',
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
  - name: ipam_pool
    props:
      - name: AddressFamily
        value: '{{ AddressFamily }}'
      - name: AllocationMinNetmaskLength
        value: '{{ AllocationMinNetmaskLength }}'
      - name: AllocationDefaultNetmaskLength
        value: '{{ AllocationDefaultNetmaskLength }}'
      - name: AllocationMaxNetmaskLength
        value: '{{ AllocationMaxNetmaskLength }}'
      - name: AllocationResourceTags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: AutoImport
        value: '{{ AutoImport }}'
      - name: AwsService
        value: '{{ AwsService }}'
      - name: Description
        value: '{{ Description }}'
      - name: IpamScopeId
        value: '{{ IpamScopeId }}'
      - name: Locale
        value: '{{ Locale }}'
      - name: ProvisionedCidrs
        value:
          - Cidr: '{{ Cidr }}'
      - name: PublicIpSource
        value: '{{ PublicIpSource }}'
      - name: PubliclyAdvertisable
        value: '{{ PubliclyAdvertisable }}'
      - name: SourceIpamPoolId
        value: '{{ SourceIpamPoolId }}'
      - name: SourceResource
        value:
          ResourceId: '{{ ResourceId }}'
          ResourceType: '{{ ResourceType }}'
          ResourceRegion: '{{ ResourceRegion }}'
          ResourceOwner: '{{ ResourceOwner }}'
      - name: Tags
        value:
          - null

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.ec2.ipam_pools
WHERE data__Identifier = '<IpamPoolId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>ipam_pools</code> resource, the following permissions are required:

### Create
```json
ec2:CreateIpamPool,
ec2:DescribeIpamPools,
ec2:ProvisionIpamPoolCidr,
ec2:GetIpamPoolCidrs,
ec2:CreateTags
```

### Delete
```json
ec2:DeleteIpamPool,
ec2:DescribeIpamPools,
ec2:GetIpamPoolCidrs,
ec2:DeprovisionIpamPoolCidr,
ec2:DeleteTags
```

### List
```json
ec2:DescribeIpamPools
```

