---
title: service_network_vpc_association
hide_title: false
hide_table_of_contents: false
keywords:
  - service_network_vpc_association
  - vpclattice
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>service_network_vpc_association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_network_vpc_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>service_network_vpc_association</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.vpclattice.service_network_vpc_association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>security_group_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>service_network_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>service_network_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>service_network_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>service_network_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>vpc_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>vpc_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
created_at,
security_group_ids,
id,
service_network_arn,
service_network_id,
service_network_identifier,
service_network_name,
status,
vpc_id,
vpc_identifier,
tags
FROM awscc.vpclattice.service_network_vpc_association
WHERE region = 'us-east-1'
AND data__Identifier = '{Arn}';
```

## Permissions

To operate on the <code>service_network_vpc_association</code> resource, the following permissions are required:

### Read
```json
vpc-lattice:GetServiceNetworkVpcAssociation,
vpc-lattice:ListTagsForResource
```

### Update
```json
vpc-lattice:TagResource,
vpc-lattice:UntagResource,
vpc-lattice:GetServiceNetworkVpcAssociation,
vpc-lattice:UpdateServiceNetworkVpcAssociation,
ec2:DescribeSecurityGroups,
vpc-lattice:ListTagsForResource
```

### Delete
```json
vpc-lattice:DeleteServiceNetworkVpcAssociation,
vpc-lattice:GetServiceNetworkVpcAssociation
```

