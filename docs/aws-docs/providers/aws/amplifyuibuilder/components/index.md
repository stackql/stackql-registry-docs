---
title: components
hide_title: false
hide_table_of_contents: false
keywords:
  - components
  - amplifyuibuilder
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>components</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>components</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>components</td></tr>
<tr><td><b>Id</b></td><td><code>aws.amplifyuibuilder.components</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AppId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>BindingProperties</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Children</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>CollectionProperties</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ComponentType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>EnvironmentName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Events</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Overrides</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Properties</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>SchemaVersion</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SourceId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Variants</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.amplifyuibuilder.components<br/>WHERE region = 'us-east-1'
</pre>
