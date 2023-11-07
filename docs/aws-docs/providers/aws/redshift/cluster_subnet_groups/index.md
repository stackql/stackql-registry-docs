---
title: cluster_subnet_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_subnet_groups
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
Retrieves a list of <code>cluster_subnet_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_subnet_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.redshift.cluster_subnet_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>The description of the parameter group.</td></tr>
<tr><td><code>SubnetIds</code></td><td><code>array</code></td><td>The list of VPC subnet IDs</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>The list of tags for the cluster parameter group.</td></tr>
<tr><td><code>ClusterSubnetGroupName</code></td><td><code>string</code></td><td>This name must be unique for all subnet groups that are created by your AWS account. If costumer do not provide it, cloudformation will generate it. Must not be "Default". </td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.redshift.cluster_subnet_groups
WHERE region = 'us-east-1'
</pre>
