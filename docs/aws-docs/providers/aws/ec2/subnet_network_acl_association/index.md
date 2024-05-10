---
title: subnet_network_acl_association
hide_title: false
hide_table_of_contents: false
keywords:
  - subnet_network_acl_association
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


Gets or updates an individual <code>subnet_network_acl_association</code> resource, use <code>subnet_network_acl_associations</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subnet_network_acl_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::SubnetNetworkAclAssociation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.subnet_network_acl_association" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="subnet_id" /></td><td><code>string</code></td><td>The ID of the subnet</td></tr>
<tr><td><CopyableCode code="network_acl_id" /></td><td><code>string</code></td><td>The ID of the network ACL</td></tr>
<tr><td><CopyableCode code="association_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
subnet_id,
network_acl_id,
association_id
FROM aws.ec2.subnet_network_acl_association
WHERE region = 'us-east-1' AND data__Identifier = '<AssociationId>';
```


## Permissions

To operate on the <code>subnet_network_acl_association</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeNetworkAcls
```

