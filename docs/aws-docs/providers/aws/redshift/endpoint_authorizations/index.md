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

Creates, updates, deletes or gets an <code>endpoint_authorization</code> resource or lists <code>endpoint_authorizations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint_authorizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Describes an endpoint authorization for authorizing Redshift-managed VPC endpoint access to a cluster across AWS accounts.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.redshift.endpoint_authorizations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the authorization action.</td></tr>
<tr><td><CopyableCode code="grantee" /></td><td><code>string</code></td><td>The AWS account ID of the grantee of the cluster.</td></tr>
<tr><td><CopyableCode code="account" /></td><td><code>string</code></td><td>The target AWS account ID to grant or revoke access for.</td></tr>
<tr><td><CopyableCode code="grantor" /></td><td><code>string</code></td><td>The AWS account ID of the cluster owner.</td></tr>
<tr><td><CopyableCode code="endpoint_count" /></td><td><code>integer</code></td><td>The number of Redshift-managed VPC endpoints created for the authorization.</td></tr>
<tr><td><CopyableCode code="authorize_time" /></td><td><code>string</code></td><td>The time (UTC) when the authorization was created.</td></tr>
<tr><td><CopyableCode code="allowed_vpcs" /></td><td><code>array</code></td><td>The VPCs allowed access to the cluster.</td></tr>
<tr><td><CopyableCode code="force" /></td><td><code>boolean</code></td><td>Indicates whether to force the revoke action. If true, the Redshift-managed VPC endpoints associated with the endpoint authorization are also deleted.</td></tr>
<tr><td><CopyableCode code="allowed_all_vpcs" /></td><td><code>boolean</code></td><td>Indicates whether all VPCs in the grantee account are allowed access to the cluster.</td></tr>
<tr><td><CopyableCode code="vpc_ids" /></td><td><code>array</code></td><td>The virtual private cloud (VPC) identifiers to grant or revoke access to.</td></tr>
<tr><td><CopyableCode code="cluster_identifier" /></td><td><code>string</code></td><td>The cluster identifier.</td></tr>
<tr><td><CopyableCode code="cluster_status" /></td><td><code>string</code></td><td>The status of the cluster.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointauthorization.html"><code>AWS::Redshift::EndpointAuthorization</code></a>.

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
    <td><CopyableCode code="ClusterIdentifier, Account, region" /></td>
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
Gets all <code>endpoint_authorizations</code> in a region.
```sql
SELECT
region,
status,
grantee,
account,
grantor,
endpoint_count,
authorize_time,
allowed_vpcs,
force,
allowed_all_vpcs,
vpc_ids,
cluster_identifier,
cluster_status
FROM aws.redshift.endpoint_authorizations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>endpoint_authorization</code>.
```sql
SELECT
region,
status,
grantee,
account,
grantor,
endpoint_count,
authorize_time,
allowed_vpcs,
force,
allowed_all_vpcs,
vpc_ids,
cluster_identifier,
cluster_status
FROM aws.redshift.endpoint_authorizations
WHERE region = 'us-east-1' AND data__Identifier = '<ClusterIdentifier>|<Account>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>endpoint_authorization</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.redshift.endpoint_authorizations (
 Account,
 ClusterIdentifier,
 region
)
SELECT 
'{{ Account }}',
 '{{ ClusterIdentifier }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.redshift.endpoint_authorizations (
 Account,
 Force,
 VpcIds,
 ClusterIdentifier,
 region
)
SELECT 
 '{{ Account }}',
 '{{ Force }}',
 '{{ VpcIds }}',
 '{{ ClusterIdentifier }}',
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
  - name: endpoint_authorization
    props:
      - name: Account
        value: '{{ Account }}'
      - name: Force
        value: '{{ Force }}'
      - name: VpcIds
        value:
          - '{{ VpcIds[0] }}'
      - name: ClusterIdentifier
        value: '{{ ClusterIdentifier }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.redshift.endpoint_authorizations
WHERE data__Identifier = '<ClusterIdentifier|Account>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>endpoint_authorizations</code> resource, the following permissions are required:

### Read
```json
redshift:DescribeEndpointAuthorization
```

### Create
```json
redshift:AuthorizeEndpointAccess,
redshift:DescribeEndpointAuthorization
```

### Update
```json
redshift:AuthorizeEndpointAccess,
redshift:DescribeEndpointAuthorization,
redshift:RevokeEndpointAccess
```

### List
```json
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
