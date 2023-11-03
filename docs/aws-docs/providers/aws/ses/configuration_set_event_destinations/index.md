---
title: configuration_set_event_destinations
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_set_event_destinations
  - ses
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>configuration_set_event_destinations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_set_event_destinations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ses.configuration_set_event_destinations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ConfigurationSetName</code></td><td><code>string</code></td><td>The name of the configuration set that contains the event destination.</td></tr><tr><td><code>EventDestination</code></td><td><code>undefined</code></td><td>The event destination object.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.ses.configuration_set_event_destinations
WHERE region = 'us-east-1'
```
