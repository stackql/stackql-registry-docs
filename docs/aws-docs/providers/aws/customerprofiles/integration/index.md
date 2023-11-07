---
title: integration
hide_title: false
hide_table_of_contents: false
keywords:
  - integration
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
Gets an individual <code>integration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>integration</td></tr>
<tr><td><b>Id</b></td><td><code>aws.customerprofiles.integration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>DomainName</code></td><td><code>string</code></td><td>The unique name of the domain.</td></tr>
<tr><td><code>Uri</code></td><td><code>string</code></td><td>The URI of the S3 bucket or any other type of data source.</td></tr>
<tr><td><code>FlowDefinition</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ObjectTypeName</code></td><td><code>string</code></td><td>The name of the ObjectType defined for the 3rd party data in Profile Service</td></tr>
<tr><td><code>CreatedAt</code></td><td><code>string</code></td><td>The time of this integration got created</td></tr>
<tr><td><code>LastUpdatedAt</code></td><td><code>string</code></td><td>The time of this integration got last updated at</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>The tags (keys and values) associated with the integration</td></tr>
<tr><td><code>ObjectTypeNames</code></td><td><code>array</code></td><td>The mapping between 3rd party event types and ObjectType names</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.customerprofiles.integration<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;DomainName&gt;'<br/>AND data__Identifier = '&lt;Uri&gt;'
</pre>
