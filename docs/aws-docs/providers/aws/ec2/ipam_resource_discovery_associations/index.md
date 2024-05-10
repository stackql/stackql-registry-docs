---
title: ipam_resource_discovery_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - ipam_resource_discovery_associations
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


Used to retrieve a list of <code>ipam_resource_discovery_associations</code> in a region or to create or delete a <code>ipam_resource_discovery_associations</code> resource, use <code>ipam_resource_discovery_association</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ipam_resource_discovery_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema of AWS::EC2::IPAMResourceDiscoveryAssociation Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.ipam_resource_discovery_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="ipam_resource_discovery_association_id" /></td><td><code>string</code></td><td>Id of the IPAM Resource Discovery Association.</td></tr>
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
ipam_resource_discovery_association_id
FROM aws.ec2.ipam_resource_discovery_associations
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
 "IpamResourceDiscoveryId": "{{ IpamResourceDiscoveryId }}",
 "IpamId": "{{ IpamId }}"
}
>>>
--required properties only
INSERT INTO aws.ec2.ipam_resource_discovery_associations (
 IpamResourceDiscoveryId,
 IpamId,
 region
)
SELECT 
{{ IpamResourceDiscoveryId }},
 {{ IpamId }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "IpamResourceDiscoveryId": "{{ IpamResourceDiscoveryId }}",
 "IpamId": "{{ IpamId }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.ec2.ipam_resource_discovery_associations (
 IpamResourceDiscoveryId,
 IpamId,
 Tags,
 region
)
SELECT 
 {{ IpamResourceDiscoveryId }},
 {{ IpamId }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ec2.ipam_resource_discovery_associations
WHERE data__Identifier = '<IpamResourceDiscoveryAssociationId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>ipam_resource_discovery_associations</code> resource, the following permissions are required:

### Create
```json
ec2:AssociateIpamResourceDiscovery,
ec2:DescribeIpamResourceDiscoveryAssociations,
ec2:CreateTags
```

### Delete
```json
ec2:DisassociateIpamResourceDiscovery,
ec2:DescribeIpamResourceDiscoveryAssociations,
ec2:DeleteTags
```

### List
```json
ec2:DescribeIpamResourceDiscoveryAssociations
```

