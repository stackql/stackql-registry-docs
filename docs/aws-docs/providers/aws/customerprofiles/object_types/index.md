---
title: object_types
hide_title: false
hide_table_of_contents: false
keywords:
  - object_types
  - customerprofiles
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>object_types</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>object_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.customerprofiles.object_types</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>DomainName</code></td><td><code>string</code></td><td>The unique name of the domain.</td></tr><tr><td><code>ObjectTypeName</code></td><td><code>string</code></td><td>The name of the profile object type.</td></tr><tr><td><code>AllowProfileCreation</code></td><td><code>boolean</code></td><td>Indicates whether a profile should be created when data is received.</td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>Description of the profile object type.</td></tr><tr><td><code>EncryptionKey</code></td><td><code>string</code></td><td>The default encryption key</td></tr><tr><td><code>ExpirationDays</code></td><td><code>integer</code></td><td>The default number of days until the data within the domain expires.</td></tr><tr><td><code>Fields</code></td><td><code>array</code></td><td>A list of the name and ObjectType field.</td></tr><tr><td><code>Keys</code></td><td><code>array</code></td><td>A list of unique keys that can be used to map data to the profile.</td></tr><tr><td><code>CreatedAt</code></td><td><code>string</code></td><td>The time of this integration got created.</td></tr><tr><td><code>LastUpdatedAt</code></td><td><code>string</code></td><td>The time of this integration got last updated at.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>The tags (keys and values) associated with the integration.</td></tr><tr><td><code>TemplateId</code></td><td><code>string</code></td><td>A unique identifier for the object template.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.customerprofiles.object_types
WHERE region = 'us-east-1'
</pre>
