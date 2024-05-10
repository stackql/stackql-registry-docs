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
ipam_pool_id
FROM aws.ec2.ipam_pools
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
 "AddressFamily": "{{ AddressFamily }}",
 "IpamScopeId": "{{ IpamScopeId }}"
}
>>>
--required properties only
INSERT INTO aws.ec2.ipam_pools (
 AddressFamily,
 IpamScopeId,
 region
)
SELECT 
{{ .AddressFamily }},
 {{ .IpamScopeId }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AddressFamily": "{{ AddressFamily }}",
 "AllocationMinNetmaskLength": "{{ AllocationMinNetmaskLength }}",
 "AllocationDefaultNetmaskLength": "{{ AllocationDefaultNetmaskLength }}",
 "AllocationMaxNetmaskLength": "{{ AllocationMaxNetmaskLength }}",
 "AllocationResourceTags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "AutoImport": "{{ AutoImport }}",
 "AwsService": "{{ AwsService }}",
 "Description": "{{ Description }}",
 "IpamScopeId": "{{ IpamScopeId }}",
 "Locale": "{{ Locale }}",
 "ProvisionedCidrs": [
  {
   "Cidr": "{{ Cidr }}"
  }
 ],
 "PublicIpSource": "{{ PublicIpSource }}",
 "PubliclyAdvertisable": "{{ PubliclyAdvertisable }}",
 "SourceIpamPoolId": "{{ SourceIpamPoolId }}",
 "SourceResource": {
  "ResourceId": "{{ ResourceId }}",
  "ResourceType": "{{ ResourceType }}",
  "ResourceRegion": "{{ ResourceRegion }}",
  "ResourceOwner": "{{ ResourceOwner }}"
 },
 "Tags": [
  null
 ]
}
>>>
--all properties
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
 {{ .AddressFamily }},
 {{ .AllocationMinNetmaskLength }},
 {{ .AllocationDefaultNetmaskLength }},
 {{ .AllocationMaxNetmaskLength }},
 {{ .AllocationResourceTags }},
 {{ .AutoImport }},
 {{ .AwsService }},
 {{ .Description }},
 {{ .IpamScopeId }},
 {{ .Locale }},
 {{ .ProvisionedCidrs }},
 {{ .PublicIpSource }},
 {{ .PubliclyAdvertisable }},
 {{ .SourceIpamPoolId }},
 {{ .SourceResource }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

