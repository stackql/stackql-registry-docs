---
title: alerts_subscription_levels
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts_subscription_levels
  - security
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>alerts_subscription_levels</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alerts_subscription_levels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.alerts_subscription_levels" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_alerts_subscription_levels', value: 'view', },
        { label: 'alerts_subscription_levels', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="alertName" /> | `text` | field from the `properties` object |
| <CopyableCode code="alert_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="alert_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="alert_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="ascLocation" /> | `text` | field from the `properties` object |
| <CopyableCode code="compromised_entity" /> | `text` | field from the `properties` object |
| <CopyableCode code="correlation_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="entities" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_links" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="intent" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_incident" /> | `text` | field from the `properties` object |
| <CopyableCode code="processing_end_time_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="product_component_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="product_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="remediation_steps" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_identifiers" /> | `text` | field from the `properties` object |
| <CopyableCode code="severity" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="sub_techniques" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="supporting_evidence" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_alert_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="techniques" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_generated_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="vendor_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | describes security alert properties. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="alertName, ascLocation, subscriptionId" /> | Get an alert that is associated with a subscription |

## `SELECT` examples

Get an alert that is associated with a subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_alerts_subscription_levels', value: 'view', },
        { label: 'alerts_subscription_levels', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
alertName,
alert_display_name,
alert_type,
alert_uri,
ascLocation,
compromised_entity,
correlation_key,
end_time_utc,
entities,
extended_links,
extended_properties,
intent,
is_incident,
processing_end_time_utc,
product_component_name,
product_name,
remediation_steps,
resource_identifiers,
severity,
start_time_utc,
status,
sub_techniques,
subscriptionId,
supporting_evidence,
system_alert_id,
techniques,
time_generated_utc,
type,
vendor_name,
version
FROM azure.security.vw_alerts_subscription_levels
WHERE alertName = '{{ alertName }}'
AND ascLocation = '{{ ascLocation }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.alerts_subscription_levels
WHERE alertName = '{{ alertName }}'
AND ascLocation = '{{ ascLocation }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

