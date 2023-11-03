---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
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
Retrieves a list of <code>domains</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.customerprofiles.domains</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>DomainName</code></td><td><code>string</code></td><td>The unique name of the domain.</td></tr><tr><td><code>DeadLetterQueueUrl</code></td><td><code>string</code></td><td>The URL of the SQS dead letter queue</td></tr><tr><td><code>DefaultEncryptionKey</code></td><td><code>string</code></td><td>The default encryption key</td></tr><tr><td><code>DefaultExpirationDays</code></td><td><code>integer</code></td><td>The default number of days until the data within the domain expires.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>The tags (keys and values) associated with the domain</td></tr><tr><td><code>CreatedAt</code></td><td><code>string</code></td><td>The time of this integration got created</td></tr><tr><td><code>LastUpdatedAt</code></td><td><code>string</code></td><td>The time of this integration got last updated at</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.customerprofiles.domains
WHERE region = 'us-east-1'
</pre>
