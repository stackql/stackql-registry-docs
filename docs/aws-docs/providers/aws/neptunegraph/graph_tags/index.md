---
title: graph_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - graph_tags
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Expands all tag keys and values for <code>graphs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>graph_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::NeptuneGraph::Graph resource creates an Amazon NeptuneGraph Graph.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.neptunegraph.graph_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="deletion_protection" /></td><td><code>boolean</code></td><td>Value that indicates whether the Graph has deletion protection enabled. The graph can't be deleted when deletion protection is enabled.<br />_Default_: If not specified, the default value is true.</td></tr>
<tr><td><CopyableCode code="graph_name" /></td><td><code>string</code></td><td>Contains a user-supplied name for the Graph. <br />If you don't specify a name, we generate a unique Graph Name using a combination of Stack Name and a UUID comprising of 4 characters.<br />_Important_: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
<tr><td><CopyableCode code="provisioned_memory" /></td><td><code>integer</code></td><td>Memory for the Graph.</td></tr>
<tr><td><CopyableCode code="public_connectivity" /></td><td><code>boolean</code></td><td>Specifies whether the Graph can be reached over the internet. Access to all graphs requires IAM authentication.<br />When the Graph is publicly reachable, its Domain Name System (DNS) endpoint resolves to the public IP address from the internet.<br />When the Graph isn't publicly reachable, you need to create a PrivateGraphEndpoint in a given VPC to ensure the DNS name resolves to a private IP address that is reachable from the VPC.<br />_Default_: If not specified, the default value is false.</td></tr>
<tr><td><CopyableCode code="replica_count" /></td><td><code>integer</code></td><td>Specifies the number of replicas you want when finished. All replicas will be provisioned in different availability zones.<br />Replica Count should always be less than or equal to 2.<br />_Default_: If not specified, the default value is 1.</td></tr>
<tr><td><CopyableCode code="vector_search_configuration" /></td><td><code>object</code></td><td>Vector Search Configuration</td></tr>
<tr><td><CopyableCode code="endpoint" /></td><td><code>string</code></td><td>The connection endpoint for the graph. For example: `g-12a3bcdef4.us-east-1.neptune-graph.amazonaws.com`</td></tr>
<tr><td><CopyableCode code="graph_arn" /></td><td><code>string</code></td><td>Graph resource ARN</td></tr>
<tr><td><CopyableCode code="graph_id" /></td><td><code>string</code></td><td>The auto-generated id assigned by the service.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>graphs</code> in a region.
```sql
SELECT
region,
deletion_protection,
graph_name,
provisioned_memory,
public_connectivity,
replica_count,
vector_search_configuration,
endpoint,
graph_arn,
graph_id,
tag_key,
tag_value
FROM aws.neptunegraph.graph_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>graph_tags</code> resource, see <a href="/providers/aws/neptunegraph/graphs/#permissions"><code>graphs</code></a>

