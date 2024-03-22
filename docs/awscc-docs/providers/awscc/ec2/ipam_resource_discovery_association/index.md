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
Gets an individual <code>ipam_resource_discovery_association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ipam_resource_discovery_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>ipam_resource_discovery_association</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.ipam_resource_discovery_association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ipam_arn</code></td><td><code>string</code></td><td>Arn of the IPAM.</td></tr>
<tr><td><code>ipam_region</code></td><td><code>string</code></td><td>The home region of the IPAM.</td></tr>
<tr><td><code>ipam_resource_discovery_association_id</code></td><td><code>string</code></td><td>Id of the IPAM Resource Discovery Association.</td></tr>
<tr><td><code>ipam_resource_discovery_id</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IPAM Resource Discovery Association.</td></tr>
<tr><td><code>ipam_id</code></td><td><code>string</code></td><td>The Id of the IPAM this Resource Discovery is associated to.</td></tr>
<tr><td><code>ipam_resource_discovery_association_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the resource discovery association is a part of.</td></tr>
<tr><td><code>is_default</code></td><td><code>boolean</code></td><td>If the Resource Discovery Association exists due as part of CreateIpam.</td></tr>
<tr><td><code>owner_id</code></td><td><code>string</code></td><td>The AWS Account ID for the account where the shared IPAM exists.</td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td>The operational state of the Resource Discovery Association. Related to Create&#x2F;Delete activities.</td></tr>
<tr><td><code>resource_discovery_status</code></td><td><code>string</code></td><td>The status of the resource discovery.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.ec2.ipam_resource_discovery_association
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

