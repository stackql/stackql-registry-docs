---
title: collections
hide_title: false
hide_table_of_contents: false
keywords:
  - collections
  - opensearchserverless
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>collections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>collections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.opensearchserverless.collections</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>The description of the collection</td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td>The identifier of the collection</td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the collection.

The name must meet the following criteria:
Unique to your account and AWS Region
Starts with a lowercase letter
Contains only lowercase letters a-z, the numbers 0-9 and the hyphen (-)
Contains between 3 and 32 characters
</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>List of tags to be added to the resource</td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the collection.</td></tr><tr><td><code>CollectionEndpoint</code></td><td><code>string</code></td><td>The endpoint for the collection.</td></tr><tr><td><code>DashboardEndpoint</code></td><td><code>string</code></td><td>The OpenSearch Dashboards endpoint for the collection.</td></tr><tr><td><code>Type</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.opensearchserverless.collections
WHERE region = 'us-east-1'
</pre>
