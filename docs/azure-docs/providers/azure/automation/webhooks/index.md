---
title: webhooks
hide_title: false
hide_table_of_contents: false
keywords:
  - webhooks
  - automation
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

Creates, updates, deletes, gets or lists a <code>webhooks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>webhooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.webhooks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_webhooks', value: 'view', },
        { label: 'webhooks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="automationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiry_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_invoked_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="run_on" /> | `text` | field from the `properties` object |
| <CopyableCode code="runbook" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="webhookName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Definition of the webhook properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId, webhookName" /> | Retrieve the webhook identified by webhook name. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of webhooks. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId, webhookName, data__name, data__properties" /> | Create the webhook identified by webhook name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId, webhookName" /> | Delete the webhook by name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId, webhookName" /> | Update the webhook identified by webhook name. |
| <CopyableCode code="generate_uri" /> | `EXEC` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Generates a Uri for use in creating a webhook. |

## `SELECT` examples

Retrieve a list of webhooks.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_webhooks', value: 'view', },
        { label: 'webhooks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
automationAccountName,
creation_time,
expiry_time,
is_enabled,
last_invoked_time,
last_modified_by,
last_modified_time,
parameters,
resourceGroupName,
run_on,
runbook,
subscriptionId,
uri,
webhookName
FROM azure.automation.vw_webhooks
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.automation.webhooks
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>webhooks</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.automation.webhooks (
automationAccountName,
resourceGroupName,
subscriptionId,
webhookName,
data__name,
data__properties,
name,
properties
)
SELECT 
'{{ automationAccountName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ webhookName }}',
'{{ data__name }}',
'{{ data__properties }}',
'{{ name }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: properties
      value:
        - name: isEnabled
          value: boolean
        - name: uri
          value: string
        - name: expiryTime
          value: string
        - name: parameters
          value: object
        - name: runbook
          value:
            - name: name
              value: string
        - name: runOn
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>webhooks</code> resource.

```sql
/*+ update */
UPDATE azure.automation.webhooks
SET 
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND webhookName = '{{ webhookName }}';
```

## `DELETE` example

Deletes the specified <code>webhooks</code> resource.

```sql
/*+ delete */
DELETE FROM azure.automation.webhooks
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND webhookName = '{{ webhookName }}';
```
