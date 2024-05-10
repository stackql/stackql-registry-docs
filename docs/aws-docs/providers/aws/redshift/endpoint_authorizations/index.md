---
title: endpoint_authorizations
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint_authorizations
  - redshift
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


Used to retrieve a list of <code>endpoint_authorizations</code> in a region or to create or delete a <code>endpoint_authorizations</code> resource, use <code>endpoint_authorization</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint_authorizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Describes an endpoint authorization for authorizing Redshift-managed VPC endpoint access to a cluster across AWS accounts.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.redshift.endpoint_authorizations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="cluster_identifier" /></td><td><code>string</code></td><td>The cluster identifier.</td></tr>
<tr><td><CopyableCode code="account" /></td><td><code>undefined</code></td><td>The target AWS account ID to grant or revoke access for.</td></tr>
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
cluster_identifier,
account
FROM aws.redshift.endpoint_authorizations
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
 "ClusterIdentifier": "{{ ClusterIdentifier }}",
 "Account": "{{ Account }}"
}
>>>
--required properties only
INSERT INTO aws.redshift.endpoint_authorizations (
 ClusterIdentifier,
 Account,
 region
)
SELECT 
{{ ClusterIdentifier }},
 {{ Account }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ClusterIdentifier": "{{ ClusterIdentifier }}",
 "Account": "{{ Account }}",
 "VpcIds": [
  "{{ VpcIds[0] }}"
 ],
 "Force": "{{ Force }}"
}
>>>
--all properties
INSERT INTO aws.redshift.endpoint_authorizations (
 ClusterIdentifier,
 Account,
 VpcIds,
 Force,
 region
)
SELECT 
 {{ ClusterIdentifier }},
 {{ Account }},
 {{ VpcIds }},
 {{ Force }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.redshift.endpoint_authorizations
WHERE data__Identifier = '<ClusterIdentifier|Account>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>endpoint_authorizations</code> resource, the following permissions are required:

### Create
```json
redshift:AuthorizeEndpointAccess,
redshift:DescribeEndpointAuthorization
```

### Delete
```json
redshift:RevokeEndpointAccess,
redshift:DeleteEndpointAccess,
redshift:DescribeEndpointAuthorization,
ec2:DeleteClientVpnEndpoint,
ec2:DescribeVpcAttribute,
ec2:DescribeSecurityGroups,
ec2:DescribeAddresses,
ec2:DescribeInternetGateways,
ec2:DescribeSubnets
```

### List
```json
redshift:DescribeEndpointAuthorization
```

