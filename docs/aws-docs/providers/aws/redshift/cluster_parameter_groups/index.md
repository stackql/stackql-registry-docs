---
title: cluster_parameter_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_parameter_groups
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
Retrieves a list of <code>cluster_parameter_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_parameter_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>cluster_parameter_groups</td></tr>
<tr><td><b>Id</b></td><td><code>aws.redshift.cluster_parameter_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ParameterGroupName</code></td><td><code>string</code></td><td>The name of the cluster parameter group.</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>A description of the parameter group.</td></tr>
<tr><td><code>ParameterGroupFamily</code></td><td><code>string</code></td><td>The Amazon Redshift engine version to which the cluster parameter group applies. The cluster engine version determines the set of parameters.</td></tr>
<tr><td><code>Parameters</code></td><td><code>array</code></td><td>An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.redshift.cluster_parameter_groups
WHERE region = 'us-east-1'
</pre>
