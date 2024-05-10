---
title: endpoint_authorization
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint_authorization
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


Gets or updates an individual <code>endpoint_authorization</code> resource, use <code>endpoint_authorizations</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint_authorization</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Describes an endpoint authorization for authorizing Redshift-managed VPC endpoint access to a cluster across AWS accounts.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.redshift.endpoint_authorization" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="grantor" /></td><td><code>string</code></td><td>The AWS account ID of the cluster owner.</td></tr>
<tr><td><CopyableCode code="grantee" /></td><td><code>string</code></td><td>The AWS account ID of the grantee of the cluster.</td></tr>
<tr><td><CopyableCode code="cluster_identifier" /></td><td><code>string</code></td><td>The cluster identifier.</td></tr>
<tr><td><CopyableCode code="authorize_time" /></td><td><code>string</code></td><td>The time (UTC) when the authorization was created.</td></tr>
<tr><td><CopyableCode code="cluster_status" /></td><td><code>string</code></td><td>The status of the cluster.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the authorization action.</td></tr>
<tr><td><CopyableCode code="allowed_all_vpcs" /></td><td><code>boolean</code></td><td>Indicates whether all VPCs in the grantee account are allowed access to the cluster.</td></tr>
<tr><td><CopyableCode code="allowed_vpcs" /></td><td><code>array</code></td><td>The VPCs allowed access to the cluster.</td></tr>
<tr><td><CopyableCode code="endpoint_count" /></td><td><code>integer</code></td><td>The number of Redshift-managed VPC endpoints created for the authorization.</td></tr>
<tr><td><CopyableCode code="account" /></td><td><code>string</code></td><td>The target AWS account ID to grant or revoke access for.</td></tr>
<tr><td><CopyableCode code="vpc_ids" /></td><td><code>array</code></td><td>The virtual private cloud (VPC) identifiers to grant or revoke access to.</td></tr>
<tr><td><CopyableCode code="force" /></td><td><code>boolean</code></td><td> Indicates whether to force the revoke action. If true, the Redshift-managed VPC endpoints associated with the endpoint authorization are also deleted.</td></tr>
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
grantor,
grantee,
cluster_identifier,
authorize_time,
cluster_status,
status,
allowed_all_vpcs,
allowed_vpcs,
endpoint_count,
account,
vpc_ids,
force
FROM aws.redshift.endpoint_authorization
WHERE region = 'us-east-1' AND data__Identifier = '<ClusterIdentifier>|<Account>';
```


## Permissions

To operate on the <code>endpoint_authorization</code> resource, the following permissions are required:

### Read
```json
redshift:DescribeEndpointAuthorization
```

### Update
```json
redshift:AuthorizeEndpointAccess,
redshift:DescribeEndpointAuthorization,
redshift:RevokeEndpointAccess
```

