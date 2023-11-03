---
title: dataset
hide_title: false
hide_table_of_contents: false
keywords:
  - dataset
  - personalize
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>dataset</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dataset</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.personalize.dataset</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name for the dataset</td></tr><tr><td><code>DatasetArn</code></td><td><code>string</code></td><td>The ARN of the dataset</td></tr><tr><td><code>DatasetType</code></td><td><code>string</code></td><td>The type of dataset</td></tr><tr><td><code>DatasetGroupArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the dataset group to add the dataset to</td></tr><tr><td><code>SchemaArn</code></td><td><code>string</code></td><td>The ARN of the schema to associate with the dataset. The schema defines the dataset fields.</td></tr><tr><td><code>DatasetImportJob</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.personalize.dataset
WHERE region = 'us-east-1' AND data__Identifier = '<DatasetArn>'
</pre>
