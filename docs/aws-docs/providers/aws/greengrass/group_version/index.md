---
title: group_version
hide_title: false
hide_table_of_contents: false
keywords:
  - group_version
  - greengrass
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>group_version</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>group_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.greengrass.group_version</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>LoggerDefinitionVersionArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DeviceDefinitionVersionArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>FunctionDefinitionVersionArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>CoreDefinitionVersionArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ResourceDefinitionVersionArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ConnectorDefinitionVersionArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SubscriptionDefinitionVersionArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>GroupId</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.greengrass.group_version
WHERE region = 'us-east-1' AND data__Identifier = '{Id}'
```
