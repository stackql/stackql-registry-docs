---
title: email_events
hide_title: false
hide_table_of_contents: false
keywords:
  - email_events
  - test_base
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

Creates, updates, deletes, gets or lists a <code>email_events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>email_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.email_events" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_email_events', value: 'view', },
        { label: 'email_events', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="emailEventResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="event_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="event_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="testBaseAccountName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The Email Event properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="emailEventResourceName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Gets a email event of a Test Base Account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists all the email events of a Test Base Account. |

## `SELECT` examples

Lists all the email events of a Test Base Account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_email_events', value: 'view', },
        { label: 'email_events', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
display_name,
emailEventResourceName,
event_id,
event_name,
resourceGroupName,
subscriptionId,
testBaseAccountName
FROM azure_extras.test_base.vw_email_events
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.test_base.email_events
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem></Tabs>

