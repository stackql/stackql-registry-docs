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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>service_network_vpc_association</code> resource, use <code>service_network_vpc_associations</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_network_vpc_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Associates a VPC with a service network.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.vpclattice.service_network_vpc_association" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="security_group_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_network_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_network_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_network_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_network_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.vpclattice.service_network_vpc_association
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
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

