---
title: webhooks
hide_title: false
hide_table_of_contents: false
keywords:
  - webhooks
  - app_compliance_automation
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.app_compliance_automation.webhooks" /></td></tr>
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
| <CopyableCode code="content_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="delivery_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_ssl_verification" /> | `text` | field from the `properties` object |
| <CopyableCode code="events" /> | `text` | field from the `properties` object |
| <CopyableCode code="payload_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="reportName" /> | `text` | field from the `properties` object |
| <CopyableCode code="send_all_events" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="update_webhook_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="webhookName" /> | `text` | field from the `properties` object |
| <CopyableCode code="webhook_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="webhook_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="webhook_key_enabled" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Webhook properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="reportName, webhookName" /> | Get the AppComplianceAutomation webhook and its properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="reportName" /> | Get the AppComplianceAutomation webhook list. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="reportName, webhookName, data__properties" /> | Create a new AppComplianceAutomation webhook or update an exiting AppComplianceAutomation webhook. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="reportName, webhookName" /> | Delete an AppComplianceAutomation webhook. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="reportName, webhookName" /> | Update an exiting AppComplianceAutomation webhook. |

## `SELECT` examples

Get the AppComplianceAutomation webhook list.

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
content_type,
delivery_status,
enable_ssl_verification,
events,
payload_url,
provisioning_state,
reportName,
send_all_events,
status,
tenant_id,
update_webhook_key,
webhookName,
webhook_id,
webhook_key,
webhook_key_enabled
FROM azure_extras.app_compliance_automation.vw_webhooks
WHERE reportName = '{{ reportName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.app_compliance_automation.webhooks
WHERE reportName = '{{ reportName }}';
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
INSERT INTO azure_extras.app_compliance_automation.webhooks (
reportName,
webhookName,
data__properties,
properties
)
SELECT 
'{{ reportName }}',
'{{ webhookName }}',
'{{ data__properties }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: webhookId
          value: string
        - name: status
          value: []
        - name: tenantId
          value: string
        - name: sendAllEvents
          value: []
        - name: events
          value:
            - []
        - name: payloadUrl
          value: string
        - name: contentType
          value: []
        - name: webhookKey
          value: string
        - name: updateWebhookKey
          value: []
        - name: webhookKeyEnabled
          value: []
        - name: enableSslVerification
          value: []
        - name: deliveryStatus
          value: []
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>webhooks</code> resource.

```sql
/*+ update */
UPDATE azure_extras.app_compliance_automation.webhooks
SET 
properties = '{{ properties }}'
WHERE 
reportName = '{{ reportName }}'
AND webhookName = '{{ webhookName }}';
```

## `DELETE` example

Deletes the specified <code>webhooks</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.app_compliance_automation.webhooks
WHERE reportName = '{{ reportName }}'
AND webhookName = '{{ webhookName }}';
```
