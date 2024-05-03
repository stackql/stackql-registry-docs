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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>configuration_set_event_destination</code> resource, use <code>configuration_set_event_destinations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_set_event_destination</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SES::ConfigurationSetEventDestination</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ses.configuration_set_event_destination" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="configuration_set_name" /></td><td><code>string</code></td><td>The name of the configuration set that contains the event destination.</td></tr>
<tr><td><CopyableCode code="event_destination" /></td><td><code>object</code></td><td>The event destination object.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id,
configuration_set_name,
event_destination
FROM aws.ses.configuration_set_event_destination
WHERE data__Identifier = '<Id>';
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

