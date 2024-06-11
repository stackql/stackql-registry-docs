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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>configuration_set_event_destination</code> resource or lists <code>configuration_set_event_destinations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_set_event_destinations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SES::ConfigurationSetEventDestination</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ses.configuration_set_event_destinations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="ConfigurationSetName, EventDestination, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from a <code>configuration_set_event_destination</code>.
```sql
SELECT
region,
id,
configuration_set_name,
event_destination
FROM aws.ses.configuration_set_event_destinations
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>configuration_set_event_destination</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.ses.configuration_set_event_destinations (
 ConfigurationSetName,
 EventDestination,
 region
)
SELECT 
'{{ ConfigurationSetName }}',
 '{{ EventDestination }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ses.configuration_set_event_destinations (
 ConfigurationSetName,
 EventDestination,
 region
)
SELECT 
 '{{ ConfigurationSetName }}',
 '{{ EventDestination }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: configuration_set_event_destination
    props:
      - name: ConfigurationSetName
        value: '{{ ConfigurationSetName }}'
      - name: EventDestination
        value:
          Name: '{{ Name }}'
          Enabled: '{{ Enabled }}'
          MatchingEventTypes:
            - '{{ MatchingEventTypes[0] }}'
          CloudWatchDestination:
            DimensionConfigurations:
              - DimensionValueSource: '{{ DimensionValueSource }}'
                DefaultDimensionValue: '{{ DefaultDimensionValue }}'
                DimensionName: '{{ DimensionName }}'
          KinesisFirehoseDestination:
            IAMRoleARN: '{{ IAMRoleARN }}'
            DeliveryStreamARN: '{{ DeliveryStreamARN }}'
          SnsDestination:
            TopicARN: '{{ TopicARN }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ses.configuration_set_event_destinations
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>configuration_set_event_destinations</code> resource, the following permissions are required:

### Create
```json
ses:CreateConfigurationSetEventDestination,
ses:GetConfigurationSetEventDestinations,
ses:DescribeConfigurationSet
```

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

