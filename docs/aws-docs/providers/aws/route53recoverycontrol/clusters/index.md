---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - route53recoverycontrol
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>clusters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53recoverycontrol.clusters</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>Name of a Cluster. You can use any non-white space character in the name</td></tr><tr><td><code>ClusterArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the cluster.</td></tr><tr><td><code>Status</code></td><td><code>string</code></td><td>Deployment status of a resource. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.</td></tr><tr><td><code>ClusterEndpoints</code></td><td><code>array</code></td><td>Endpoints for the cluster.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.route53recoverycontrol.clusters
WHERE region = 'us-east-1'
</pre>
