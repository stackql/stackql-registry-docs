---
title: service_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - service_actions
  - servicecatalog
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>service_actions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>service_actions</td></tr>
<tr><td><b>Id</b></td><td><code>aws.servicecatalog.service_actions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AcceptLanguage</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DefinitionType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Definition</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.servicecatalog.service_actions<br/>WHERE region = 'us-east-1'
</pre>
