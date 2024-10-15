---
title: alerts_suppression_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts_suppression_rules
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

Creates, updates, deletes, gets or lists a <code>alerts_suppression_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alerts_suppression_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.alerts_suppression_rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_alerts_suppression_rules', value: 'view', },
        { label: 'alerts_suppression_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="alert_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="alertsSuppressionRuleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="comment" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiration_date_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="reason" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="suppression_alerts_scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | describes AlertsSuppressionRule properties |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="alertsSuppressionRuleName, subscriptionId" /> | Get dismiss rule, with name: {alertsSuppressionRuleName}, for the given subscription |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List of all the dismiss rules for the given subscription |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="alertsSuppressionRuleName, subscriptionId" /> | Delete dismiss alert rule for this subscription. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="alertsSuppressionRuleName, subscriptionId" /> | Update existing rule or create new rule if it doesn't exist |

## `SELECT` examples

List of all the dismiss rules for the given subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_alerts_suppression_rules', value: 'view', },
        { label: 'alerts_suppression_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
alert_type,
alertsSuppressionRuleName,
comment,
expiration_date_utc,
last_modified_utc,
reason,
state,
subscriptionId,
suppression_alerts_scope,
type
FROM azure.security.vw_alerts_suppression_rules
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.alerts_suppression_rules
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `REPLACE` example

Replaces all fields in the specified <code>alerts_suppression_rules</code> resource.

```sql
/*+ update */
REPLACE azure.security.alerts_suppression_rules
SET 
properties = '{{ properties }}'
WHERE 
alertsSuppressionRuleName = '{{ alertsSuppressionRuleName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>alerts_suppression_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.security.alerts_suppression_rules
WHERE alertsSuppressionRuleName = '{{ alertsSuppressionRuleName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
