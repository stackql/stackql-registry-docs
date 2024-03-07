---
title: configuration_set_event_destination
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_set_event_destination
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
Gets an individual <code>configuration_set_event_destination</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_set_event_destination</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>configuration_set_event_destination</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ses.configuration_set_event_destination</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>configuration_set_name</code></td><td><code>string</code></td><td>The name of the configuration set that contains the event destination.</td></tr>
<tr><td><code>event_destination</code></td><td><code>object</code></td><td>The event destination object.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
configuration_set_name,
event_destination
FROM awscc.ses.configuration_set_event_destination
WHERE region = 'us-east-1'
AND data__Identifier = '{Id}';
```

## Permissions

To operate on the <code>configuration_set_event_destination</code> resource, the following permissions are required:

### Update
```json
ses:UpdateConfigurationSetEventDestination,
ses:GetConfigurationSetEventDestinations
```

### Delete
```json
ses:DeleteConfigurationSetEventDestination
```

### Read
```json
ses:GetConfigurationSetEventDestinations,
ses:DescribeConfigurationSet
```

