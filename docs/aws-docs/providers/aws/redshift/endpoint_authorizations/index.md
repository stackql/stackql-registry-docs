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
Retrieves a list of <code>endpoint_authorizations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint_authorizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.redshift.endpoint_authorizations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Grantor</code></td><td><code>undefined</code></td><td>The AWS account ID of the cluster owner.</td></tr>
<tr><td><code>Grantee</code></td><td><code>undefined</code></td><td>The AWS account ID of the grantee of the cluster.</td></tr>
<tr><td><code>ClusterIdentifier</code></td><td><code>string</code></td><td>The cluster identifier.</td></tr>
<tr><td><code>AuthorizeTime</code></td><td><code>string</code></td><td>The time (UTC) when the authorization was created.</td></tr>
<tr><td><code>ClusterStatus</code></td><td><code>string</code></td><td>The status of the cluster.</td></tr>
<tr><td><code>Status</code></td><td><code>string</code></td><td>The status of the authorization action.</td></tr>
<tr><td><code>AllowedAllVPCs</code></td><td><code>boolean</code></td><td>Indicates whether all VPCs in the grantee account are allowed access to the cluster.</td></tr>
<tr><td><code>AllowedVPCs</code></td><td><code>array</code></td><td>The VPCs allowed access to the cluster.</td></tr>
<tr><td><code>EndpointCount</code></td><td><code>integer</code></td><td>The number of Redshift-managed VPC endpoints created for the authorization.</td></tr>
<tr><td><code>Account</code></td><td><code>undefined</code></td><td>The target AWS account ID to grant or revoke access for.</td></tr>
<tr><td><code>VpcIds</code></td><td><code>array</code></td><td>The virtual private cloud (VPC) identifiers to grant or revoke access to.</td></tr>
<tr><td><code>Force</code></td><td><code>boolean</code></td><td> Indicates whether to force the revoke action. If true, the Redshift-managed VPC endpoints associated with the endpoint authorization are also deleted.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.redshift.endpoint_authorizations
WHERE region = 'us-east-1'
</pre>
