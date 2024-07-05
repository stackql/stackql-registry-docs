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

Creates, updates, deletes or gets an <code>ipam_pool</code> resource or lists <code>ipam_pools</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ipam_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema of AWS::EC2::IPAMPool Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.ipam_pools" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="ipam_pool_id" /></td><td><code>string</code></td><td>Id of the IPAM Pool.</td></tr>
<tr><td><CopyableCode code="address_family" /></td><td><code>string</code></td><td>The address family of the address space in this pool. Either IPv4 or IPv6.</td></tr>
<tr><td><CopyableCode code="allocation_min_netmask_length" /></td><td><code>integer</code></td><td>The minimum allowed netmask length for allocations made from this pool.</td></tr>
<tr><td><CopyableCode code="allocation_default_netmask_length" /></td><td><code>integer</code></td><td>The default netmask length for allocations made from this pool. This value is used when the netmask length of an allocation isn't specified.</td></tr>
<tr><td><CopyableCode code="allocation_max_netmask_length" /></td><td><code>integer</code></td><td>The maximum allowed netmask length for allocations made from this pool.</td></tr>
<tr><td><CopyableCode code="allocation_resource_tags" /></td><td><code>array</code></td><td>When specified, an allocation will not be allowed unless a resource has a matching set of tags.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IPAM Pool.</td></tr>
<tr><td><CopyableCode code="auto_import" /></td><td><code>boolean</code></td><td>Determines what to do if IPAM discovers resources that haven't been assigned an allocation. If set to true, an allocation will be made automatically.</td></tr>
<tr><td><CopyableCode code="aws_service" /></td><td><code>string</code></td><td>Limits which service in Amazon Web Services that the pool can be used in.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="ipam_scope_id" /></td><td><code>string</code></td><td>The Id of the scope this pool is a part of.</td></tr>
<tr><td><CopyableCode code="ipam_scope_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the scope this pool is a part of.</td></tr>
<tr><td><CopyableCode code="ipam_scope_type" /></td><td><code>string</code></td><td>Determines whether this scope contains publicly routable space or space for a private network</td></tr>
<tr><td><CopyableCode code="ipam_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IPAM this pool is a part of.</td></tr>
<tr><td><CopyableCode code="locale" /></td><td><code>string</code></td><td>The region of this pool. If not set, this will default to "None" which will disable non-custom allocations. If the locale has been specified for the source pool, this value must match.</td></tr>
<tr><td><CopyableCode code="pool_depth" /></td><td><code>integer</code></td><td>The depth of this pool in the source pool hierarchy.</td></tr>
<tr><td><CopyableCode code="provisioned_cidrs" /></td><td><code>array</code></td><td>A list of cidrs representing the address space available for allocation in this pool.</td></tr>
<tr><td><CopyableCode code="public_ip_source" /></td><td><code>string</code></td><td>The IP address source for pools in the public scope. Only used for provisioning IP address CIDRs to pools in the public scope. Default is `byoip`.</td></tr>
<tr><td><CopyableCode code="publicly_advertisable" /></td><td><code>boolean</code></td><td>Determines whether or not address space from this pool is publicly advertised. Must be set if and only if the pool is IPv6.</td></tr>
<tr><td><CopyableCode code="source_ipam_pool_id" /></td><td><code>string</code></td><td>The Id of this pool's source. If set, all space provisioned in this pool must be free space provisioned in the parent pool.</td></tr>
<tr><td><CopyableCode code="source_resource" /></td><td><code>object</code></td><td>The resource associated with this pool's space. Depending on the ResourceType, setting a SourceResource changes which space can be provisioned in this pool and which types of resources can receive allocations</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of this pool. This can be one of the following values: "create-in-progress", "create-complete", "modify-in-progress", "modify-complete", "delete-in-progress", or "delete-complete"</td></tr>
<tr><td><CopyableCode code="state_message" /></td><td><code>string</code></td><td>An explanation of how the pool arrived at it current state.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
Gets all <code>ipam_pools</code> in a region.
```sql
SELECT
region,
ipam_pool_id,
address_family,
allocation_min_netmask_length,
allocation_default_netmask_length,
allocation_max_netmask_length,
allocation_resource_tags,
arn,
auto_import,
aws_service,
description,
ipam_scope_id,
ipam_scope_arn,
ipam_scope_type,
ipam_arn,
locale,
pool_depth,
provisioned_cidrs,
public_ip_source,
publicly_advertisable,
source_ipam_pool_id,
source_resource,
state,
state_message,
tags
FROM aws.ec2.ipam_pools
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>ipam_pool</code>.
```sql
SELECT
region,
ipam_pool_id,
address_family,
allocation_min_netmask_length,
allocation_default_netmask_length,
allocation_max_netmask_length,
allocation_resource_tags,
arn,
auto_import,
aws_service,
description,
ipam_scope_id,
ipam_scope_arn,
ipam_scope_type,
ipam_arn,
locale,
pool_depth,
provisioned_cidrs,
public_ip_source,
publicly_advertisable,
source_ipam_pool_id,
source_resource,
state,
state_message,
tags
FROM aws.ec2.ipam_pools
WHERE region = 'us-east-1' AND data__Identifier = '<IpamPoolId>';
```

## `INSERT` example

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

## `DELETE` example

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

### Read
```json
ec2:DescribeIpamPools,
ec2:GetIpamPoolCidrs
```

### Update
```json
ec2:ModifyIpamPool,
ec2:DescribeIpamPools,
ec2:GetIpamPoolCidrs,
ec2:ProvisionIpamPoolCidr,
ec2:DeprovisionIpamPoolCidr,
ec2:CreateTags,
ec2:DeleteTags
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

