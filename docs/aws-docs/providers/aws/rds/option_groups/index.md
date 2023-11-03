---
title: option_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - option_groups
  - rds
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>option_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>option_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.rds.option_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>OptionGroupName</code></td><td><code>string</code></td><td>Specifies the name of the option group.</td></tr><tr><td><code>OptionGroupDescription</code></td><td><code>string</code></td><td>Provides a description of the option group.</td></tr><tr><td><code>EngineName</code></td><td><code>string</code></td><td>Indicates the name of the engine that this option group can be applied to.</td></tr><tr><td><code>MajorEngineVersion</code></td><td><code>string</code></td><td>Indicates the major engine version associated with this option group.</td></tr><tr><td><code>OptionConfigurations</code></td><td><code>array</code></td><td>Indicates what options are available in the option group.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.rds.option_groups
WHERE region = 'us-east-1'
</pre>
