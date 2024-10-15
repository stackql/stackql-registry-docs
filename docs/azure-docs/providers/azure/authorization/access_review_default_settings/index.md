---
title: access_review_default_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - access_review_default_settings
  - authorization
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

Creates, updates, deletes, gets or lists a <code>access_review_default_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_review_default_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.access_review_default_settings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_access_review_default_settings', value: 'view', },
        { label: 'access_review_default_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The access review default settings id. This is only going to be default |
| <CopyableCode code="name" /> | `text` | The access review default settings name. This is always going to be Access Review Default Settings |
| <CopyableCode code="auto_apply_decisions_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_decision" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_decision_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="instance_duration_in_days" /> | `text` | field from the `properties` object |
| <CopyableCode code="justification_required_on_approval" /> | `text` | field from the `properties` object |
| <CopyableCode code="mail_notifications_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="recommendation_look_back_duration" /> | `text` | field from the `properties` object |
| <CopyableCode code="recommendations_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="recurrence" /> | `text` | field from the `properties` object |
| <CopyableCode code="reminder_notifications_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The access review default settings id. This is only going to be default |
| <CopyableCode code="name" /> | `string` | The access review default settings name. This is always going to be Access Review Default Settings |
| <CopyableCode code="properties" /> | `object` | Settings of an Access Review. |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get access review default settings for the subscription |
| <CopyableCode code="put" /> | `REPLACE` | <CopyableCode code="subscriptionId" /> | Get access review default settings for the subscription |

## `SELECT` examples

Get access review default settings for the subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_access_review_default_settings', value: 'view', },
        { label: 'access_review_default_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
auto_apply_decisions_enabled,
default_decision,
default_decision_enabled,
instance_duration_in_days,
justification_required_on_approval,
mail_notifications_enabled,
recommendation_look_back_duration,
recommendations_enabled,
recurrence,
reminder_notifications_enabled,
subscriptionId,
type
FROM azure.authorization.vw_access_review_default_settings
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
FROM azure.authorization.access_review_default_settings
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `REPLACE` example

Replaces all fields in the specified <code>access_review_default_settings</code> resource.

```sql
/*+ update */
REPLACE azure.authorization.access_review_default_settings
SET 
mailNotificationsEnabled = true|false,
reminderNotificationsEnabled = true|false,
defaultDecisionEnabled = true|false,
justificationRequiredOnApproval = true|false,
defaultDecision = '{{ defaultDecision }}',
autoApplyDecisionsEnabled = true|false,
recommendationsEnabled = true|false,
recommendationLookBackDuration = '{{ recommendationLookBackDuration }}',
instanceDurationInDays = '{{ instanceDurationInDays }}',
recurrence = '{{ recurrence }}'
WHERE 
subscriptionId = '{{ subscriptionId }}';
```
