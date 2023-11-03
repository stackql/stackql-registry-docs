---
title: project
hide_title: false
hide_table_of_contents: false
keywords:
  - project
  - databrew
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>project</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>project</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.databrew.project</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>DatasetName</code></td><td><code>string</code></td><td>Dataset name</td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td>Project name</td></tr><tr><td><code>RecipeName</code></td><td><code>string</code></td><td>Recipe name</td></tr><tr><td><code>RoleArn</code></td><td><code>string</code></td><td>Role arn</td></tr><tr><td><code>Sample</code></td><td><code>undefined</code></td><td>Sample</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.databrew.project
WHERE region = 'us-east-1' AND data__Identifier = '{Name}'
</pre>
