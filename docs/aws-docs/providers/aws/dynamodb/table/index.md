---
title: table
hide_title: false
hide_table_of_contents: false
keywords:
  - table
  - dynamodb
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>table</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>table</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.dynamodb.table</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>StreamArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>AttributeDefinitions</code></td><td><code>array</code></td><td></td></tr><tr><td><code>BillingMode</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DeletionProtectionEnabled</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>GlobalSecondaryIndexes</code></td><td><code>array</code></td><td></td></tr><tr><td><code>KeySchema</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>LocalSecondaryIndexes</code></td><td><code>array</code></td><td></td></tr><tr><td><code>PointInTimeRecoverySpecification</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>TableClass</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ProvisionedThroughput</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>SSESpecification</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>StreamSpecification</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>TableName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr><tr><td><code>TimeToLiveSpecification</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ContributorInsightsSpecification</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>KinesisStreamSpecification</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ImportSourceSpecification</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.dynamodb.table
WHERE region = 'us-east-1' AND data__Identifier = '{TableName}'
</pre>
