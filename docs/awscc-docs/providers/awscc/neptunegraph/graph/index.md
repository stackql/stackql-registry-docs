---
title: graph
hide_title: false
hide_table_of_contents: false
keywords:
  - graph
  - neptunegraph
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>graph</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>graph</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>graph</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.neptunegraph.graph</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>deletion_protection</code></td><td><code>boolean</code></td><td>Value that indicates whether the Graph has deletion protection enabled. The graph can't be deleted when deletion protection is enabled.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;_Default_: If not specified, the default value is true.</td></tr>
<tr><td><code>graph_name</code></td><td><code>string</code></td><td>Contains a user-supplied name for the Graph. &lt;br&#x2F;&gt;&lt;br&#x2F;&gt;If you don't specify a name, we generate a unique Graph Name using a combination of Stack Name and a UUID comprising of 4 characters.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;_Important_: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
<tr><td><code>provisioned_memory</code></td><td><code>integer</code></td><td>Memory for the Graph.</td></tr>
<tr><td><code>public_connectivity</code></td><td><code>boolean</code></td><td>Specifies whether the Graph can be reached over the internet. Access to all graphs requires IAM authentication.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;When the Graph is publicly reachable, its Domain Name System (DNS) endpoint resolves to the public IP address from the internet.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;When the Graph isn't publicly reachable, you need to create a PrivateGraphEndpoint in a given VPC to ensure the DNS name resolves to a private IP address that is reachable from the VPC.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;_Default_: If not specified, the default value is false.</td></tr>
<tr><td><code>replica_count</code></td><td><code>integer</code></td><td>Specifies the number of replicas you want when finished. All replicas will be provisioned in different availability zones.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;Replica Count should always be less than or equal to 2.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;_Default_: If not specified, the default value is 1.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags associated with this graph.</td></tr>
<tr><td><code>vector_search_configuration</code></td><td><code>object</code></td><td>Vector Search Configuration</td></tr>
<tr><td><code>endpoint</code></td><td><code>string</code></td><td>The connection endpoint for the graph. For example: `g-12a3bcdef4.us-east-1.neptune-graph.amazonaws.com`</td></tr>
<tr><td><code>graph_arn</code></td><td><code>string</code></td><td>Graph resource ARN</td></tr>
<tr><td><code>graph_id</code></td><td><code>string</code></td><td>The auto-generated id assigned by the service.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>graph</code> resource, the following permissions are required:

### Read
<pre>
neptune-graph:GetGraph,
neptune-graph:ListTagsForResource,
kms:DescribeKey,
kms:CreateGrant,
kms:Decrypt</pre>

### Update
<pre>
iam:PassRole,
neptune-graph:GetGraph,
neptune-graph:ListTagsForResource,
neptune-graph:TagResource,
neptune-graph:UntagResource,
neptune-graph:UpdateGraph,
kms:DescribeKey,
kms:CreateGrant,
kms:Decrypt</pre>

### Delete
<pre>
neptune-graph:DeleteGraph,
neptune-graph:GetGraph,
kms:DescribeKey,
kms:CreateGrant,
kms:Decrypt</pre>


## Example
```sql
SELECT
region,
deletion_protection,
graph_name,
provisioned_memory,
public_connectivity,
replica_count,
tags,
vector_search_configuration,
endpoint,
graph_arn,
graph_id
FROM awscc.neptunegraph.graph
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;GraphId&gt;'
```
