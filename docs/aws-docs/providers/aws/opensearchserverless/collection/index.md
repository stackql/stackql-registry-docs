---
title: collection
hide_title: false
hide_table_of_contents: false
keywords:
  - collection
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
Gets an individual <code>collection</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>collection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>collection</td></tr>
<tr><td><b>Id</b></td><td><code>aws.opensearchserverless.collection</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>The description of the collection</td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td>The identifier of the collection</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the collection.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;The name must meet the following criteria:&lt;br&#x2F;&gt;Unique to your account and AWS Region&lt;br&#x2F;&gt;Starts with a lowercase letter&lt;br&#x2F;&gt;Contains only lowercase letters a-z, the numbers 0-9 and the hyphen (-)&lt;br&#x2F;&gt;Contains between 3 and 32 characters&lt;br&#x2F;&gt;</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>List of tags to be added to the resource</td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the collection.</td></tr>
<tr><td><code>CollectionEndpoint</code></td><td><code>string</code></td><td>The endpoint for the collection.</td></tr>
<tr><td><code>DashboardEndpoint</code></td><td><code>string</code></td><td>The OpenSearch Dashboards endpoint for the collection.</td></tr>
<tr><td><code>Type</code></td><td><code>undefined</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.opensearchserverless.collection<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Id&gt;'
</pre>
