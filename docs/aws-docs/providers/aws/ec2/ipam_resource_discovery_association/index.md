---
title: ipam_resource_discovery_association
hide_title: false
hide_table_of_contents: false
keywords:
  - ipam_resource_discovery_association
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

Gets or operates on an individual <code>ipam_resource_discovery_association</code> resource, use <code>ipam_resource_discovery_associations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ipam_resource_discovery_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema of AWS::EC2::IPAMResourceDiscoveryAssociation Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.ipam_resource_discovery_association" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="ipam_arn" /></td><td><code>string</code></td><td>Arn of the IPAM.</td></tr>
<tr><td><CopyableCode code="ipam_region" /></td><td><code>string</code></td><td>The home region of the IPAM.</td></tr>
<tr><td><CopyableCode code="ipam_resource_discovery_association_id" /></td><td><code>string</code></td><td>Id of the IPAM Resource Discovery Association.</td></tr>
<tr><td><CopyableCode code="ipam_resource_discovery_id" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IPAM Resource Discovery Association.</td></tr>
<tr><td><CopyableCode code="ipam_id" /></td><td><code>string</code></td><td>The Id of the IPAM this Resource Discovery is associated to.</td></tr>
<tr><td><CopyableCode code="ipam_resource_discovery_association_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the resource discovery association is a part of.</td></tr>
<tr><td><CopyableCode code="is_default" /></td><td><code>boolean</code></td><td>If the Resource Discovery Association exists due as part of CreateIpam.</td></tr>
<tr><td><CopyableCode code="owner_id" /></td><td><code>string</code></td><td>The AWS Account ID for the account where the shared IPAM exists.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The operational state of the Resource Discovery Association. Related to Create&#x2F;Delete activities.</td></tr>
<tr><td><CopyableCode code="resource_discovery_status" /></td><td><code>string</code></td><td>The status of the resource discovery.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
ipam_arn,
ipam_region,
ipam_resource_discovery_association_id,
ipam_resource_discovery_id,
ipam_id,
ipam_resource_discovery_association_arn,
is_default,
owner_id,
state,
resource_discovery_status,
tags
FROM aws.ec2.ipam_resource_discovery_association
WHERE data__Identifier = '<IpamResourceDiscoveryAssociationId>';
```

## Permissions

To operate on the <code>ipam_resource_discovery_association</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeIpamResourceDiscoveryAssociations
```

### Update
```json
ec2:DescribeIpamResourceDiscoveryAssociations,
ec2:CreateTags,
ec2:DeleteTags
```

### Delete
```json
ec2:DisassociateIpamResourceDiscovery,
ec2:DescribeIpamResourceDiscoveryAssociations,
ec2:DeleteTags
```

