---
title: event_data_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - event_data_stores
  - cloudtrail
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>event_data_stores</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_data_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloudtrail.event_data_stores</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AdvancedEventSelectors</code></td><td><code>array</code></td><td>The advanced event selectors that were used to select events for the data store.</td></tr><tr><td><code>CreatedTimestamp</code></td><td><code>undefined</code></td><td>The timestamp of the event data store's creation.</td></tr><tr><td><code>EventDataStoreArn</code></td><td><code>string</code></td><td>The ARN of the event data store.</td></tr><tr><td><code>MultiRegionEnabled</code></td><td><code>boolean</code></td><td>Indicates whether the event data store includes events from all regions, or only from the region in which it was created.</td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the event data store.</td></tr><tr><td><code>OrganizationEnabled</code></td><td><code>boolean</code></td><td>Indicates that an event data store is collecting logged events for an organization.</td></tr><tr><td><code>RetentionPeriod</code></td><td><code>integer</code></td><td>The retention period, in days.</td></tr><tr><td><code>Status</code></td><td><code>string</code></td><td>The status of an event data store. Values are ENABLED and PENDING_DELETION.</td></tr><tr><td><code>TerminationProtectionEnabled</code></td><td><code>boolean</code></td><td>Indicates whether the event data store is protected from termination.</td></tr><tr><td><code>UpdatedTimestamp</code></td><td><code>undefined</code></td><td>The timestamp showing when an event data store was updated, if applicable. UpdatedTimestamp is always either the same or newer than the time shown in CreatedTimestamp.</td></tr><tr><td><code>KmsKeyId</code></td><td><code>string</code></td><td>Specifies the KMS key ID to use to encrypt the events delivered by CloudTrail. The value can be an alias name prefixed by 'alias/', a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.cloudtrail.event_data_stores
WHERE region = 'us-east-1'
```
