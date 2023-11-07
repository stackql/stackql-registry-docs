---
title: data_lake_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - data_lake_settings
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
Gets an individual <code>data_lake_settings</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_lake_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>data_lake_settings</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lakeformation.data_lake_settings</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AllowExternalDataFiltering</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>ExternalDataFilteringAllowList</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>CreateTableDefaultPermissions</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Parameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Admins</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>CreateDatabaseDefaultPermissions</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AuthorizedSessionTagValueList</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>TrustedResourceOwners</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.lakeformation.data_lake_settings
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Id&gt;'
</pre>
