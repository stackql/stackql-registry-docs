---
title: document
hide_title: false
hide_table_of_contents: false
keywords:
  - document
  - ssm
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>document</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>document</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>document</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ssm.document</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Content</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Attachments</code></td><td><code>array</code></td><td>A list of key and value pairs that describe attachments to a version of a document.</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>A name for the Systems Manager document.</td></tr>
<tr><td><code>VersionName</code></td><td><code>string</code></td><td>An optional field specifying the version of the artifact you are creating with the document. This value is unique across all versions of a document, and cannot be changed.</td></tr>
<tr><td><code>DocumentType</code></td><td><code>string</code></td><td>The type of document to create.</td></tr>
<tr><td><code>DocumentFormat</code></td><td><code>string</code></td><td>Specify the document format for the request. The document format can be either JSON or YAML. JSON is the default format.</td></tr>
<tr><td><code>TargetType</code></td><td><code>string</code></td><td>Specify a target type to define the kinds of resources the document can run on.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment.</td></tr>
<tr><td><code>Requires</code></td><td><code>array</code></td><td>A list of SSM documents required by a document. For example, an ApplicationConfiguration document requires an ApplicationConfigurationSchema document.</td></tr>
<tr><td><code>UpdateMethod</code></td><td><code>string</code></td><td>Update method - when set to 'Replace', the update will replace the existing document; when set to 'NewVersion', the update will create a new version.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.ssm.document
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Name&gt;'
</pre>
