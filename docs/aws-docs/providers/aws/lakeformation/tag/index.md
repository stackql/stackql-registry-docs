---
title: tag
hide_title: false
hide_table_of_contents: false
keywords:
  - tag
  - lakeformation
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>tag</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tag</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>tag</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lakeformation.tag</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>CatalogId</code></td><td><code>string</code></td><td>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.</td></tr>
<tr><td><code>TagKey</code></td><td><code>string</code></td><td>The key-name for the LF-tag.</td></tr>
<tr><td><code>TagValues</code></td><td><code>array</code></td><td>A list of possible values an attribute can take.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.lakeformation.tag<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;TagKey&gt;'
</pre>
