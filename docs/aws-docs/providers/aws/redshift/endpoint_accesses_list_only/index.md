---
title: endpoint_accesses_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint_accesses_list_only
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

Lists <code>endpoint_accesses</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/endpoint_accesses/"><code>endpoint_accesses</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint_accesses_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for a Redshift-managed VPC endpoint.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.redshift.endpoint_accesses_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="endpoint_status" /></td><td><code>string</code></td><td>The status of the endpoint.</td></tr>
<tr><td><CopyableCode code="vpc_endpoint" /></td><td><code>object</code></td><td>The connection endpoint for connecting to an Amazon Redshift cluster through the proxy.</td></tr>
<tr><td><CopyableCode code="address" /></td><td><code>string</code></td><td>The DNS address of the endpoint.</td></tr>
<tr><td><CopyableCode code="endpoint_name" /></td><td><code>string</code></td><td>The name of the endpoint.</td></tr>
<tr><td><CopyableCode code="vpc_security_group_ids" /></td><td><code>array</code></td><td>A list of vpc security group ids to apply to the created endpoint access.</td></tr>
<tr><td><CopyableCode code="resource_owner" /></td><td><code>string</code></td><td>The AWS account ID of the owner of the cluster.</td></tr>
<tr><td><CopyableCode code="subnet_group_name" /></td><td><code>string</code></td><td>The subnet group name where Amazon Redshift chooses to deploy the endpoint.</td></tr>
<tr><td><CopyableCode code="port" /></td><td><code>integer</code></td><td>The port number on which the cluster accepts incoming connections.</td></tr>
<tr><td><CopyableCode code="endpoint_create_time" /></td><td><code>string</code></td><td>The time (UTC) that the endpoint was created.</td></tr>
<tr><td><CopyableCode code="cluster_identifier" /></td><td><code>string</code></td><td>A unique identifier for the cluster. You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. All alphabetical characters must be lower case, no hypens at the end, no two consecutive hyphens. Cluster name should be unique for all clusters within an AWS account</td></tr>
<tr><td><CopyableCode code="vpc_security_groups" /></td><td><code>array</code></td><td>A list of Virtual Private Cloud (VPC) security groups to be associated with the endpoint.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>endpoint_accesses</code> in a region.
```sql
SELECT
region,
endpoint_name
FROM aws.redshift.endpoint_accesses_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>endpoint_accesses_list_only</code> resource, see <a href="/providers/aws/redshift/endpoint_accesses/#permissions"><code>endpoint_accesses</code></a>


